import json
from pathlib import Path

def grade_tests(results, total_tests, results_file="results.json"):
    """Calculează scorul total și salvează fișierul JSON."""
    passed_tests = sum(r.get("result", 0) for r in results)
    score_percentage = round((passed_tests / total_tests) * 100, 2)

    summary = {
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "score_percentage": score_percentage,
        "results": results
    }

    Path(results_file).write_text(json.dumps(summary, indent=4), encoding="utf-8")

    print("\n📊 Rezumat final:")
    print(f"   Teste trecute: {passed_tests}/{total_tests}")
    print(f"   Scor total: {score_percentage}%")
    print(f"📄 Rezultatele detaliate au fost salvate în '{results_file}'")

    return summary
