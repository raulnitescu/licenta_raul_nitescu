import subprocess
from pathlib import Path

def run_code_with_input(code_path: Path, input_path: Path, timeout=2):
    """
    Rulează codul Python într-un container Docker extrem de izolat (sandbox).
    Returnează (stdout, stderr).
    """
    try:
        # Folosim .resolve() pentru a ne asigura că Docker primește
        # întotdeauna căi absolute, indiferent de unde e rulat scriptul.
        code_dir_abs = code_path.parent.resolve()
        input_dir_abs = input_path.parent.resolve()

        # Lista cu argumentele comenzii Docker
        docker_command = [
            "docker", "run", "--rm",

            # --- Izolare Rețea și Resurse ---
            "--net=none",            # Fără acces la rețea
            "--memory=128m",         # Maxim 128MB RAM
            "--cpus=0.5",            # Maxim jumătate de nucleu CPU
            "--pids-limit=20",       # Protecție anti-fork bomb (max 20 procese)

            # --- Întărirea Securității (Hardening) ---
            "--read-only",           # Sistemul de fișiere al containerului e read-only
            "--cap-drop=ALL",        # Renunță la toate "capabilities" Linux
            "--user", "1000:1000",   # Rulează ca utilizator neprivilegiat (non-root)

            # --- Volume (montate read-only) ---
            "-v", f"{code_dir_abs}:/app/temp:ro",
            "-v", f"{input_dir_abs}:/app/inputs:ro",

            # --- Workaround pentru --read-only ---
            # Python-ul ar putea avea nevoie să scrie fișiere .pyc sau temp
            # Creăm un mic sistem de fișiere temporar (în RAM) pentru /tmp
            "--tmpfs", "/tmp:size=4m,nodev,nosuid,noexec",

            # --- Comanda de executat ---
            "-w", "/app/temp",       # Working directory
            "python:3.10-slim",      # Imaginea Docker
            "bash", "-c",
            # Comanda propriu-zisă care rulează codul cu inputul
            f"python {code_path.name} < /app/inputs/{input_path.name}"
        ]

        result = subprocess.run(
            docker_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip(), result.stderr.strip()

    except FileNotFoundError:
        # Această excepție este ridicată dacă "docker" nu e în PATH.
        # **NU rulăm local.** Returnăm o eroare de sistem.
        return "", "Eroare Sistem: Comanda 'docker' nu a fost găsită."

    except subprocess.TimeoutExpired:
        # Timeout-ul a fost atins
        return "", "Timeout (codul a rulat prea mult)"

    except Exception as e:
        # Prindem orice altă eroare neașteptată
        # (ex. Docker daemon oprit, eroare de permisiuni la volume)
        return "", f"Eroare necunoscută la rularea Docker: {str(e)}"
