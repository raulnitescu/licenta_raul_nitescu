from pathlib import Path
from .analyzer import analyze_code

def main():
    base_path = Path(__file__).resolve().parent.parent
    code_file = base_path / "temp_user_code.py"
    cerinta_file = base_path / "cerinta.in"

    result = analyze_code(code_file, cerinta_file)

    print("\n🤖 Rezultatele analizei AI:")
    print(result["feedback"])

if __name__ == "__main__":
    main()
