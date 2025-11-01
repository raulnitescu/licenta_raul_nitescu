import subprocess
from pathlib import Path

def run_code_with_input(code_path: Path, input_path: Path, timeout=2):
    """
    Rulează codul Python (din code_path) cu input din input_path.
    Returnează (stdout, stderr).
    """
    try:
        result = subprocess.run(
            ["python", str(code_path)],
            stdin=open(input_path, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return "", "Timeout (codul a rulat prea mult)"
