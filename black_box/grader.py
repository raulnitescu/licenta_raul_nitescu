import json
from pathlib import Path

def grade_tests(results, total_tests):
    """
    Calculează scorul total și salvează rezultatele în results.json.
    Returnează scorul procentual (float).
    """
    passed = sum(1 for r in results if r["result"] == 1)
    score = (passed / total_tests) * 100.0

    print("\n📊 Rezumat final:")
    print(f"   Teste trecute: {passed}/{total_tests}")
    print(f"   Scor total: {score}%")

    results_file = Path(__file__).resolve().parent.parent / "results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print("📄 Rezultatele detaliate au fost salvate în 'results.json'")

    return score
