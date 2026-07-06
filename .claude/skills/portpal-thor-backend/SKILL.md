---
name: portpal-thor-backend
description: Connect portpal's local LLM backend to the thor GPU box (llama.cpp llama-server serving qwen3-coder-next) over an SSH tunnel. Use before running portpal hint/watch when the backend should be thor rather than the Anthropic API or a laptop-local server.
---

# Use thor as portpal's local backend

thor runs a llama.cpp `llama-server` serving model **`qwen3-coder-next`** on **thor's own**
`127.0.0.1:8081` (loopback only, not exposed on the LAN). portpal reaches it through an SSH
tunnel and treats it as its `local` backend at `http://localhost:8081`. The Algorithms
consumer repo's `.portpal.toml` is already wired this way (`local_endpoint`, `local_model`),
and with no `ANTHROPIC_API_KEY` set, `backend.default = "auto"` resolves to this local backend.

## Bring it up

1. A human must start the server on thor first (e.g. `./serve-qwen3-coder-next-llamacpp.sh`).
   You cannot start it from here — you only tunnel to it.
2. Open the tunnel in the background and verify it answers:

   ```bash
   ssh -fN -L 8081:localhost:8081 nadim@thor     # -f backgrounds after auth
   curl -s http://localhost:8081/v1/models        # expect an id: qwen3-coder-next
   ```

   Equivalent wrapper: `PORTPAL_LLM_PORT=8081 bash ~/Source/portpal/scripts/run-llama-server-remote.sh nadim@thor --attach` (runs in the foreground — background it or append `&`).

## Verify through portpal

From a consumer repo (see the **portpal-watch** skill for setup):

```bash
portpal doctor    # expect: [ok ] local backend [localhost] (http://localhost:8081)
```

## Gotchas

- **Connect as `nadim@thor`, never the bare `thor` alias.** `~/.ssh/config` forces
  `User root` for `thor`, which is not authorized (`Permission denied (publickey)`). A
  command-line user overrides the alias's `User`.
- The tunnel is ephemeral — it dies on reboot / network drop. Re-open it.
- **Tear down safely** when done. A naive `pkill -f '8081:localhost:8081'` can match its own
  command line and kill the wrong thing; `pgrep` excludes itself, so use it:

  ```bash
  pgrep -af '8081:localhost:8081'                 # inspect: should be just the tunnel
  pgrep -f  '8081:localhost:8081' | xargs -r kill
  ```

- Direct-LAN alternative (no tunnel): have thor bind `0.0.0.0` and set
  `local_endpoint = "http://<thor-ip>:8081"`. The tunnel is preferred (keeps thor private).
