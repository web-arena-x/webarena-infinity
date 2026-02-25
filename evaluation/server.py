"""Server lifecycle management: start, wait, stop."""

import os
import signal
import subprocess
import sys
import time

import requests


def kill_port(port: int):
    """Kill any process listening on the given port (handles zombie servers)."""
    try:
        result = subprocess.run(
            ["lsof", "-ti", f":{port}"],
            capture_output=True, text=True, timeout=5,
        )
        pids = result.stdout.strip().split()
        for pid in pids:
            if pid:
                try:
                    os_pid = int(pid)
                    os.kill(os_pid, signal.SIGTERM)
                except (ValueError, ProcessLookupError, PermissionError):
                    pass
        if pids:
            time.sleep(0.5)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass


def start_server(web_app_dir: str, port: int) -> subprocess.Popen:
    kill_port(port)
    return subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=web_app_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def wait_for_server(port: int, host: str = "localhost", timeout: int = 10) -> bool:
    url = f"http://{host}:{port}/"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.5)
    return False


def stop_server(proc: subprocess.Popen):
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
