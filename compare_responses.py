"""Compare two AI responses using evaluator-provided scores.

Scores must be entered on a 1–5 scale. This is a decision-support demonstration,
not an automatic mathematical fact-checker.
"""
WEIGHTS = {
    "correctness": 0.40,
    "reasoning": 0.25,
    "instruction_adherence": 0.15,
    "clarity": 0.10,
    "completeness": 0.10,
}

def total(scores):
    if set(scores) != set(WEIGHTS):
        raise ValueError("Provide a score for every criterion.")
    if any(not 1 <= value <= 5 for value in scores.values()):
        raise ValueError("All scores must be between 1 and 5.")
    return sum(scores[k] / 5 * w * 100 for k, w in WEIGHTS.items())

def main():
    print("Compare two candidate responses (scores are human judgments).")
    results = {}
    for response in ("A", "B"):
        print(f"\nResponse {response}")
        scores = {}
        for criterion in WEIGHTS:
            while True:
                try:
                    value = float(input(f"  {criterion.replace('_', ' ').title()} (1–5): "))
                    if 1 <= value <= 5:
                        scores[criterion] = value
                        break
                    print("  Enter a score from 1 to 5.")
                except ValueError:
                    print("  Enter a valid number.")
        results[response] = total(scores)
    print(f"\nResponse A: {results['A']:.1f}/100")
    print(f"Response B: {results['B']:.1f}/100")
    if results["A"] == results["B"]:
        print("Result: Tie. Use written evidence and task-specific priorities to decide.")
    else:
        print(f"Higher rubric score: Response {max(results, key=results.get)}")
    print("Always record a short evidence-based rationale; a higher score is not proof by itself.")

if __name__ == "__main__":
    main()
