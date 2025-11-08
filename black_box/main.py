from pathlib import Path
from code_runner import run_code_with_input
from grader import grade_tests
from file_manager import load_code, cleanup_temp

def main():
    base_path = Path(__file__).resolve().parent.parent

    code_file = load_code(base_path)
    total_tests = 3
    results = []

    for i in range(1, total_tests + 1):
        input_file = base_path / "sandbox" / "inputs" / f"input{i}.in"
        output_file = base_path / "sandbox" / "outputs" / f"output{i}.in"

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

    # Calculează scorul general
    score_percentage = grade_tests(results, total_tests)

    # Analiza AI dacă toate testele au trecut
    if score_percentage == 100.0:
        print("\n🎯 Toate testele au fost trecute! Se lansează analiza AI...\n")

        from code_analysis.analyzer import analyze_code

        cerinta_path = base_path / "cerinta.in"
        temp_code_path = base_path / "sandbox" / "temp" / "temp_user_code.py"

        # scriem codul temporar pentru analiză
        temp_code_path.write_text(code_file.read_text(encoding="utf-8"), encoding="utf-8")

        ai_result = analyze_code(temp_code_path, cerinta_path)
        print(ai_result["feedback"])
    else:
        print("\n⚠️ Codul nu a trecut toate testele — analiza AI nu se va face.")

    cleanup_temp(code_file)

if __name__ == "__main__":
    main()
