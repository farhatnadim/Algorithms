# portpal — Python → C++/Rust/Lean 4 porting assistant (modeled on cpp2rustpal)

## Context

The user hand-ports the Python reference algorithms in this repo to C++26, Rust, and
Lean 4 (hard rule: the assistant never writes those implementation bodies). They already
built `~/Source/cpp2rustpal` ("Pal") for the C++→Rust direction: a *mentor, not a
transpiler* — on save it sends the source to an LLM (local llama.cpp at `localhost:8001`
or the Anthropic API) and produces a constrained-Markdown `.hints.md` sidecar with
source anchors, a "⚠️ Patterns Not Directly Translatable" section, and a
machine-readable deps trailer; it never emits target code. Pal's gaps: no
verification/compile/test step, no cross-checking, no tests.

This plan builds the successor for the Python→{C++, Rust, Lean 4} direction with the
missing functionality: **verification, cross-language parity, Lean-aware hints
(termination/proof obligations), and progress tracking**. The Algorithms repo is
ready-made as the first consumer: complete Python reference, stub trees (`cpp/` CMake+
gtest, `rust/` workspace, `lean4/` lake with `sorry` bodies), a rich knowledge base
(`docs/porting-notes.md` per-algorithm preconditions/invariants/termination;
`docs/lean4-catchable-bugs.md` 10 real bugs by Lean tier), seeded-RNG deterministic
tests, and per-language CI — but nothing automated connecting them.

**Decisions taken as defaults (user was AFK when asked — revisit if desired):**
new standalone repo at `~/Source/portpal`; v1 surface = CLI watcher (VS Code extension
later); all four feature areas in scope, phased; both Anthropic + local llama.cpp
backends (auto-detect on `ANTHROPIC_API_KEY`, like Pal); the hints-only rule carries
over — the tool never writes target-language implementation code.

## New repo layout — `/home/nadim/Source/portpal`

Pure Python 3.11+; deps: `anthropic`, `openai` (tomllib is stdlib). Own git repo.

```
portpal/
├── pyproject.toml                  # console_script: portpal = portpal.cli:main
├── portpal/
│   ├── cli.py                      # init, hint, watch, verify, parity, status, doctor
│   ├── config.py                   # load/validate .portpal.toml → dataclasses
│   ├── mapping.py                  # file path ↔ unit ↔ per-language paths/symbol names
│   ├── backends.py                 # Anthropic + OpenAI-compatible clients (from Pal)
│   ├── docs_context.py             # extract porting-notes `## <Unit>` section + `### Bug N` entries
│   ├── watch.py                    # mtime-poll watcher (Pal pattern) + debounce
│   ├── hints/
│   │   ├── engine.py               # assemble prompt → backend → validate → .hints.md sidecar
│   │   ├── contract.py             # output validator: reject/redact target-language code blocks
│   │   └── prompts/{common,rust,cpp,lean}.md
│   ├── verify.py                   # run configured build/test commands per unit/target
│   ├── parity/{fixtures,harness,compare}.py
│   ├── progress.py                 # stub-vs-implemented scanner, status matrix, README updater
│   └── refdocs.py                  # generalizes Pal's Rust Book "Read more" link index
├── data/rust_book_chapters.json    # copied from cpp2rustpal/cli/book_chapters.json
└── tests/                          # pytest: config, mapping, docs_context, contract, compare, progress
```

## Consumer config — `Algorithms/.portpal.toml` (committed)

```toml
[backend]
default = "auto"                       # auto | anthropic | local
local_endpoint = "http://localhost:8001"

[docs]
porting_notes = "docs/porting-notes.md"
lean_bugs = "docs/lean4-catchable-bugs.md"

[targets.cpp]
build = "cmake -S cpp -B cpp/build && cmake --build cpp/build -j"
test  = "ctest --test-dir cpp/build --output-on-failure"
test_filter_flag = "-R {filter}"
stub_markers = ["TODO: User implements"]

[targets.rust]
build = "cargo build --manifest-path rust/Cargo.toml"
test  = "cargo test --manifest-path rust/Cargo.toml"
test_filter_flag = "-p {filter}"
stub_markers = ["TODO: User implements", "Placeholder - user implements", "assert!(true)"]

[targets.lean]
cwd = "lean4"
build = "lake build"                   # compiling IS the test until theorems exist
stub_markers = ["sorry"]

[parity]
fixtures_dir = "parity/fixtures"
[parity.runners]
python = "python parity/python_adapter.py"
# cpp/rust/lean runner commands added in Phase 2

[[units]]                              # one block per family (~9 total)
name = "sort"
python = ["Sort/Sort.py", "Sort/MergeSort.py"]
cpp = "cpp/sort"            cpp_test_filter = "sort_test"
rust = "rust/algorithms-sort"  rust_test_filter = "algorithms-sort"
lean = "lean4/Algorithms/Sort/Basic.lean"
notes_heading = "## Sort"
algorithms = ["insertion_sort", "bubble_sort", "merge_sort", "quick_sort"]
```

`mapping.py` resolves any saved file to its unit by longest-prefix match over the
per-language paths, and carries per-language symbol casing (`merge_sort` /
`mergeSort` etc.).

## Hint generation (v1 core)

**Trigger:** the user saves the *target-language* file they're editing (e.g.
`rust/algorithms-sort/src/lib.rs`). Prompt bundle = Python reference source(s) + the
user's in-progress target file + the unit's `## <Unit>` section of
`docs/porting-notes.md` (split on `^## `) + target-specific extras:
- **Lean**: matching `### Bug N` entries from `docs/lean4-catchable-bugs.md` (match on
  reference path / algorithm name), the tier table, the port-buggy-first exercise.
- **Rust**: `docs/python-rust-type-mapping.md` + Rust Book "Read more" links (reuse
  Pal's `_load_book_chapters`/`_book_reference_section`, cpp_to_rust_hints.py:41-60).

**Prompt templates**: `common.md` = Pal's mentor framing (SYSTEM_PROMPT,
cpp_to_rust_hints.py:65-137; drop the vestigial inotify paragraphs) + hard hints-only
rules (≤3-line comment snippets max, no function bodies) + repo conventions (injectable
RNG, generic element types, Option over sentinels, known preconditions).
`rust.md` = ownership/mutation mapping matching the stub signature, Ord vs PartialOrd,
ValueError→Option/Result, gated crate suggestions, "⚠️ Python Patterns Not Directly
Translatable". `cpp.md` = C++26/concepts, std::optional/span, UB watchlist, injectable
URBG, big-int need for Karatsuba. `lean.md` (flagship) = totality first
(termination_by; why `partial def` forfeits protection), a **Proof Obligations**
section restating the unit's termination argument as concrete obligations, which
historical bugs Lean will/won't catch per tier, theorem *names* only.

**Output contract** (machine-checkable, per target): fixed headings
(`### Reference Semantics Recap` / `### Hints` with `<!-- anchor: sym-<name> -->`
symbol anchors / `### ⚠️ Patterns Not Directly Translatable` / `### Checklist`), plus
`<!-- deps: ... -->` trailer for Rust. Symbol anchors instead of Pal's line anchors —
stable across edits. `contract.py` rejects fenced `rust|cpp|lean` blocks and
body-shaped content; one re-prompt with the violation quoted, then redact. Sink:
`<file>.hints.md` sidecar + terminal stream; content-hash cache in `.portpal-cache/`
skips regeneration when inputs unchanged (fixes Pal's regenerate-every-save gap).
Add `*.hints.md` and `.portpal-cache/` to Algorithms `.gitignore`.

## Verification runner

`portpal verify [unit ...] [--target cpp,rust,lean]`: run each target's configured
build, then test with the unit filter substituted (`ctest -R sort_test`,
`cargo test -p algorithms-sort`, `lake build`); summary table target × (build, test) →
OK/FAIL(first error excerpt)/SKIP; nonzero exit on failure. `portpal watch --verify`
runs the saved file's unit+target after hints and appends a `### Verification` section
to the sidecar.

## Parity harness (Phase 2)

Fixtures in `Algorithms/parity/fixtures/<unit>.<algorithm>.json`: a small closed set of
`kind`s (int_list→int_list sorts; (int_list,k)→int select; bigint decimal *strings* for
Karatsuba; float matrices for Strassen/Gram-Schmidt with `float_tol`; point sets for
closest pair). Compare modes in `compare.py`: `exact`, `float_tol`, `multiset`,
`sorted_permutation` (randomized quicksort — cross-language RNG streams can't match),
`min_over_runs` (Karger, or exclude it). **Expected outputs generated, never
hand-written**: `portpal parity --generate` calls `Algorithms/parity/python_adapter.py`
(assistant-writable Python: algorithm name → callable + numpy↔JSON normalization).

Runner protocol: `runner <fixture.json>` → JSON array of `{name, output|error}` on
stdout (batch per fixture to amortize process startup). Python adapter doubles as the
reference runner. Per-target runners are **user-written glue** (~100–150 lines each)
unless the CLAUDE.md rule gets a carve-out (open question below): `rust/parity-runner/`
workspace member (serde_json), `cpp/parity/` behind `option(PORTPAL_PARITY)` so CI is
unaffected (nlohmann/json), `lean4/Parity/Main.lean` + `lean_exe` (Lean.Data.Json) —
Lean last; the harness must gate on the progress scanner (a `sorry` def panics at
runtime, never run stubs). Output: per-case PASS/FAIL/STUB matrix with first-divergence
detail.

## Progress tracker

`portpal status`: per (algorithm, language) scan using configured `stub_markers`
against the parsed `pub fn`/`def`/`src/<algo>.cpp` bodies → `STUB` → `IMPLEMENTED` →
`VERIFIED` → `PARITY` (last two cached in `.portpal-cache/status.json`). `--json` for
scripting. `--update-readme` (Phase 3, opt-in) replaces only exact `- Coming Soon`
lines under the unit's README language subheadings — never touches existing links.

## CLI UX

```
portpal init | hint <file> | watch <file|unit> [--verify] [--no-hints]
portpal verify [unit ...] [--target ...] [--build-only]
portpal parity [unit ...] [--target ...] [--generate] [--case NAME]
portpal status [--json] [--update-readme] | doctor
global: --config --backend {auto,anthropic,local} --model --endpoint
```

Typical session: `cd ~/Source/Algorithms && portpal watch rust/algorithms-sort/src/lib.rs --verify`.

## Reuse from cpp2rustpal

- **Near-verbatim** → `backends.py` (backend auto-detect + both streaming loops,
  cpp_to_rust_hints.py:142-176, 233-256), mtime watcher (:181-212, + debounce),
  book-index mechanism (:41-60) → `refdocs.py`, `cli/book_chapters.json` → `data/`.
- **Adapted**: mentor SYSTEM_PROMPT; the extension's STRICT OUTPUT CONTRACT +
  anchor + trailer ideas → `contract.py`/templates; `.hints.md` sidecar convention.
- **Referenced only**: `scripts/run-llama-server.sh` — `portpal doctor` points at it
  when localhost:8001 is down. **Not reused**: cargo-mirror (Algorithms already has
  scaffolds), the VS Code extension (Phase 4).

## Phasing

1. **v1**: portpal repo scaffold; config/mapping/backends/docs_context + tests; hint
   engine + 3 prompt templates + contract validator + tests; `hint`/`watch`;
   `verify`; `status` (print-only); `doctor`; write `Algorithms/.portpal.toml`
   (all ~9 units) + `.gitignore` entries.
2. **Parity**: fixture schema, `--generate`, `python_adapter.py`, compare modes;
   Rust runner → C++ runner → Lean runner; parity column in `status`.
3. `--update-readme`; hint caching polish; optional Algorithms `parity.yml` CI;
   thin Claude Code skill in `Algorithms/.claude/skills/portpal/` wrapping the CLI.
4. VS Code extension (multi-target hover, port of Pal's extension).

## Verification (how we'll know it works)

- portpal's own pytest suite (contract validator, docs-section extraction against the
  real Algorithms docs, compare modes, stub scanner against the real stub trees).
- End-to-end: `portpal doctor` in Algorithms; `portpal hint rust/algorithms-sort/src/lib.rs
  --once` produces a contract-conformant sidecar with the Sort porting-notes content;
  `portpal verify sort --target rust,cpp,lean` goes green on the current stubs;
  `portpal status` shows the expected all-STUB matrix (minus legacy one-offs);
  after Phase 2, `portpal parity sort --generate` then a deliberate wrong expected
  value shows FAIL with first-divergence detail.

## Open questions

1. **CLAUDE.md carve-out**: may the assistant write the C++/Rust/Lean *parity runner
   glue* (JSON decode + dispatch, no algorithm bodies)? Recommended: yes, with an
   explicit carve-out sentence in Algorithms/CLAUDE.md; otherwise portpal emits runner
   scaffolds with TODO dispatch arms and the user fills them.
2. Repo name: `portpal` assumed (alternatives: `py2polypal`).
3. Should saving a *Python reference* file trigger anything? Proposed: cache
   invalidation + "N ports affected" notice only, no LLM call.
4. The AFK defaults above (location/surfaces/backends) — confirm or adjust.
