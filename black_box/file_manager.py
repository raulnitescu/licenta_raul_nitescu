from pathlib import Path

def load_code(base_path: Path):
    """Citește codul din code.in și îl scrie în sandbox/temp/temp_user_code.py"""
    code_file_path = base_path / "code.in"
    if not code_file_path.exists():
        raise FileNotFoundError(f"Nu s-a găsit {code_file_path}")

    code_text = code_file_path.read_text(encoding="utf-8")
    temp_file = base_path / "sandbox" / "temp" / "temp_user_code.py"
    temp_file.write_text(code_text, encoding="utf-8")
    return temp_file

def cleanup_temp(code_file: Path):
    """Șterge fișierul temporar creat pentru rulare."""
    if code_file.exists():
        code_file.unlink()
