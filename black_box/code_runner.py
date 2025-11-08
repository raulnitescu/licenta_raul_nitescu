import subprocess
from pathlib import Path

def run_code_with_input(code_path: Path, input_path: Path, timeout=2):
    """
    Rulează codul Python într-un container Docker izolat.
    Returnează (stdout, stderr).
    """
    try:
        # --- Rulează codul în Docker ---
        result = subprocess.run(
            [
                "docker", "run", "--rm", "--net=none",
                "--memory=128m", "--cpus=0.5",
                "-v", f"{code_path.parent}:/app",
                "-w", "/app",
                "python:3.10-slim",
                "bash", "-c",
                f"python {code_path.name} < {input_path.name}"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip(), result.stderr.strip()

    except FileNotFoundError:
        # Docker nu e disponibil → fallback local (mai puțin sigur)
        try:
            with open(input_path, "r") as f:
                result = subprocess.run(
                    ["python", str(code_path)],
                    stdin=f,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=timeout
                )
            return result.stdout.strip(), result.stderr.strip()
        except subprocess.TimeoutExpired:
            return "", "Timeout (codul a rulat prea mult)"

    except subprocess.TimeoutExpired:
        return "", "Timeout (codul a rulat prea mult)"
