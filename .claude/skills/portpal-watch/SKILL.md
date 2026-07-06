---
name: portpal-watch
description: Generate porting hints with the portpal CLI (hint / watch) for a file in a consumer repo, and check progress (doctor / status / verify). Use when asked to get portpal hints, watch a port file, or see stub-vs-implemented status. portpal is a mentor — it never writes target-language implementation code.
---

# Drive portpal in a consumer repo

portpal is a **Python → C++ / Rust / Lean 4 porting mentor** (not a transpiler): it reads a
consumer repo's `.portpal.toml`, the Python reference, and porting docs, then writes hints to
a `<file>.hints.md` sidecar next to each in-progress port. It never emits target-language
implementation code.

The reference consumer is **`~/Source/Algorithms`** — an "Algorithms Illuminated" / CLRS /
Sedgewick learning repo whose Python implementations are being ported to C++ / Rust / Lean 4
(most ports are still stubs). Its units (sort, search, select, data_structures, graph,
linear_algebra, integer_multiplication, minimum_cut, misc) are defined in its `.portpal.toml`.

## Setup (once per shell)

```bash
source ~/Source/portpal/venv/bin/activate     # NOTE: the venv is "venv", not ".venv"
cd ~/Source/Algorithms                          # or any repo containing a .portpal.toml
```

Use that venv (it has the `portpal` console script + the openai/anthropic extras); the system
`python3` is usually PEP-668 externally-managed. portpal finds its config by walking up from
cwd, like `.git`.

## Backend

`backend.default = "auto"` → Anthropic if `ANTHROPIC_API_KEY` is set, else the local
llama-server at the config's `local_endpoint`. For Algorithms that endpoint is thor's tunnel
on `:8081` — bring it up first with the **portpal-thor-backend** skill, then confirm:

```bash
portpal doctor        # expect [ok ] local backend [localhost] (http://localhost:8081)
```

`doctor`, `status`, `verify`, and `parity` never call an LLM; only `hint` / `watch` do.

## Commands

```bash
portpal status                                   # stub-vs-implemented matrix (no LLM)
portpal hint  cpp/sort/src/merge_sort.cpp        # one-shot hints -> <file>.hints.md
portpal hint  <file> --force                     # ignore the input-hash cache
portpal watch cpp/sort/src/merge_sort.cpp        # re-hint on every save (Ctrl-C to stop)
portpal watch <file> --verify                    # also build+test the file's unit each save
portpal verify sort --target cpp                 # run one unit/target's build + tests
```

- The path you pass must be a real file that maps to a unit in `.portpal.toml` (portpal
  matches by longest path prefix). The sidecar lands beside it, e.g.
  `cpp/sort/src/merge_sort.cpp.hints.md`.
- `watch` is a long-running mtime poller — run it in the background or a dedicated terminal.
- `<file>.hints.md` sidecars and `.portpal-cache/` are generated state (gitignored); never
  hand-edit the cache.

## The one rule

portpal must never produce target-language implementation code — only hints, signatures,
type-mapping guidance, and watch-outs. A contract validator re-prompts and redacts if the
model slips. If you are an agent asked to "use portpal to write the port," stop: portpal
guides the human/agent who writes it; it does not emit the implementation.
