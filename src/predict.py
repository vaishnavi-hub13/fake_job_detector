from src.modules.pattern_analyzer import check_pattern
from src.modules.trust_score import calculate_score

def predict_job(text):
    pattern_score = check_pattern(text)
    score = calculate_score(pattern_score)
    return {"trust_score": score}
