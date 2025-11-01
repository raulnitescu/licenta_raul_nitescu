from pathlib import Path
from code_runner import run_code_with_input
from grader import grade_tests
from file_manager import load_code, cleanup_temp

def main():
    # Calea către folderul părinte (D:\RaulWork\licenta)
    base_path = Path(__file__).resolve().parent.parent

    code_file = load_code(base_path)
    total_tests = 3
    results = []

    for i in range(1, total_tests + 1):
        input_file = base_path / f"input{i}.in"
        output_file = base_path / f"output{i}.in"

        if not input_file.exists() or not output_file.exists():
            print(f"⚠️ Test {i}: fișiere lipsă (input/output).")
            results.append({"test": i, "result": 0, "error": "missing files"})
            continue

        expected_output = output_file.read_text(encoding="utf-8").strip()
        actual_output, errors = run_code_with_input(code_file, input_file)

        if errors:
            print(f"❌ Test {i}: Eroare la rulare — {errors}")
            results.append({"test": i, "result": 0, "error": errors})
        elif actual_output == expected_output:
            print(f"✅ Test {i}: PASS")
            results.append({"test": i, "result": 1})
        else:
            print(f"❌ Test {i}: FAIL")
            results.append({
                "test": i,
                "result": 0,
                "expected": expected_output,
                "got": actual_output
            })

    grade_tests(results, total_tests)
    cleanup_temp(code_file)

if __name__ == "__main__":
    main()

