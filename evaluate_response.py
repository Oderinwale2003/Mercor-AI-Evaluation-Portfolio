"""Human-guided rubric scoring for an AI-generated mathematics response.

This tool records evaluator judgments; it does not automatically prove correctness.
Run: python mathematics-evaluation/evaluate_response.py
"""
CRITERIA = {
    "mathematical_correctness": 0.40,
    "reasoning_validity": 0.25,
    "instruction_adherence": 0.15,
    "clarity": 0.10,
    "completeness": 0.10,
}

def weighted_score(scores):
    """Return a score out of 100 from criterion scores on a 1–5 scale."""
    if set(scores) != set(CRITERIA):
        missing = set(CRITERIA) - set(scores)
        extra = set(scores) - set(CRITERIA)
        raise ValueError(f"Criteria mismatch. Missing: {missing}; extra: {extra}")
    for criterion, score in scores.items():
        if not isinstance(score, (int, float)) or not 1 <= score <= 5:
            raise ValueError(f"{criterion} must be a number from 1 to 5.")
    return sum(scores[key] / 5 * weight * 100
               for key, weight in CRITERIA.items())

def main():
    print("AI MATHEMATICS RESPONSE EVALUATOR")
    print("Enter a score from 1 (poor) to 5 (excellent) for each criterion.")
    scores = {}
    for criterion in CRITERIA:
        while True:
            try:
                scores[criterion] = float(input(f"{criterion.replace('_', ' ').title()} (1–5): "))
                if 1 <= scores[criterion] <= 5:
                    break
                print("Please enter a value from 1 to 5.")
            except ValueError:
                print("Please enter a valid number.")
    score = weighted_score(scores)
    print(f"\nWeighted score: {score:.1f}/100")
    print("Evaluator reminder: document the exact mathematical evidence behind each score.")

if __name__ == "__main__":
    main()
