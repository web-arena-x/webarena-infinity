# Evaluation Harness Reference

## Entry Points

### Sequential: `evaluation/run_eval.py`
```bash
python evaluation/run_eval.py --model gpt --task-id task_e1
python evaluation/run_eval.py --model claude --difficulty easy
python evaluation/run_eval.py --model gemini --use-vision
```

### Parallel: `evaluation/run_eval_parallel.py`
```bash
# Local (auto-starts servers on ports 8001-8004)
python evaluation/run_eval_parallel.py --model gpt --workers 4

# Remote env host
python evaluation/run_eval_parallel.py --model gpt --workers 8 \
    --env-host ec2-host --base-port 8001
```

## Available Models
```python
MODELS = {
    "gpt":    ChatOpenAI(model="gpt-4o"),
    "gemini": ChatGoogle(model="gemini-2.0-flash"),
    "claude": ChatAnthropic(model="claude-sonnet-4-5-20250929"),
}
```

## Agent Interface (`evaluation/agents.py`)

```python
class AgentRunner(Protocol):
    async def setup(self, server_url: str) -> None: ...
    async def run(self, task: str, server_url: str, task_dir: Path) -> AgentResult: ...
    async def teardown(self) -> None: ...

@dataclass
class AgentResult:
    elapsed: float
    steps: int
    is_done: bool
    final_result: str | None
    errors: list[str]
```

`BrowserUseAgent` is the built-in implementation. To add a new agent, implement the protocol.

## Execution Flow (per task)

1. `reset_state(server_url)` — POST /api/reset + 0.5s wait
2. `agent_runner.run(task_instruction, server_url, task_dir)` — agent interacts with browser
3. `load_verifier(web_app_dir, verify_path)` — dynamically load verifier module
4. `verify_fn(server_url)` → `(passed, message)`
5. Save result dict to `task_dir/result.json`

## Output Structure
```
{web-app}/results/{model}_{timestamp}/
├── results.json          # Aggregate metrics
├── report.html           # HTML report
└── {task_id}/
    ├── result.json       # Per-task result + verifier message
    ├── history.json      # Agent trajectory
    ├── conversations/    # LLM prompts & responses
    └── screenshots/      # Step-by-step screenshots
```

By default, results are written to `{web-app}/results/`. Override with `--output-dir`.

## Key Functions in `evaluation/tasks.py`

- `load_tasks(web_app_dir)` — reads `{web_app_dir}/tasks.json`
- `filter_tasks(tasks, task_id, difficulty)` — filter by id or difficulty
- `load_verifier(web_app_dir, verify_path)` — dynamic import of verifier module
- `reset_state(server_url)` — POST /api/reset
- `run_task(task, agent_runner, server_url, web_app_dir, task_dir)` — full task lifecycle

## Constants
- `TASK_TIMEOUT = 300` seconds (5 min per task)
- Default `max_steps = 50` (agent steps)
- Default port: 8000 (sequential), 8001+ (parallel)

## Adding a New Web Application

1. Create `{app-name}/` following the environment protocol (see environment-protocol.md)
2. Run with `--web-app {app-name}`:
   ```bash
   python evaluation/run_eval.py --model gpt --web-app my-new-app
   ```
3. The harness auto-discovers tasks from `{app-name}/tasks.json`

## Docker Scaling

```bash
# On env host (EC2)
docker compose up --scale gitlab=20

# From agent machine
python evaluation/run_eval_parallel.py --workers 20 \
    --env-host <ec2-ip> --base-port 8001
```

New environments just need a `Dockerfile` and a service entry in `docker-compose.yml`.
