import ast
from pathlib import Path
from .scorers import *
from .feedback_generator import generate_feedback

def analyze_code(code_path: Path, cerinta_path: Path):
    """
    Analizează codul din code_path în funcție de criteriile educaționale.
    Returnează scorurile și feedbackul bilingv child-friendly.
    """
    code_text = code_path.read_text(encoding="utf-8")
    cerinta_text = cerinta_path.read_text(encoding="utf-8")

    try:
        tree = ast.parse(code_text)
    except:
        tree = ast.parse("")

    scores = {
        "abstractization": score_abstractization(tree),
        "parallelization": score_parallelization(code_text),
        "logic": score_logic(code_text),
        "synchronization": score_synchronization(code_text),
        "flow_control": score_flow_control(code_text),
        "user_interactivity": score_user_interactivity(code_text),
        "data_representation": score_data_representation(code_text),
        "clarity_style": score_clarity_style(code_text),
        "scalability": score_scalability(code_text),
        "efficiency": score_efficiency(code_text),
    }

    total = sum(scores.values())
    feedback = generate_feedback(scores, total)
    return {"scores": scores, "total": total, "feedback": feedback}
