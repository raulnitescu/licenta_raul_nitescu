import ast

def score_abstractization(tree):
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    return min(len(funcs) * 2 + 4, 10)

def score_parallelization(code_text):
    return 10 if "thread" in code_text or "async" in code_text else 7

def score_logic(code_text):
    count_if = code_text.count("if")
    return 10 if count_if > 0 else 6

def score_synchronization(code_text):
    if "await" in code_text or "join" in code_text:
        return 9
    return 7

def score_flow_control(code_text):
    loops = code_text.count("for") + code_text.count("while")
    return max(10 - loops // 3, 6)

def score_user_interactivity(code_text):
    return 10 if "input(" in code_text or "print(" in code_text else 5

def score_data_representation(code_text):
    if any(x in code_text for x in ["list", "dict", "set", "tuple"]):
        return 10
    return 6

def score_clarity_style(code_text):
    return 10 if "#" in code_text or " " in code_text else 7

def score_scalability(code_text):
    if "for" in code_text and "range" in code_text:
        return 8
    return 9

def score_efficiency(code_text):
    lines = len(code_text.splitlines())
    return 10 if lines < 40 else 7
