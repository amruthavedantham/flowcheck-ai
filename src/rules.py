def check_duplicates(steps):
    """
    Find duplicate steps
    """
    duplicates = []
    seen = set()

    for step in steps:
        if step.lower() in seen:
            duplicates.append(step)
        else:
            seen.add(step.lower())

    return duplicates


def check_short_steps(steps):
    """
    Find very short or weak steps
    """
    short_steps = []

    for step in steps:
        if len(step.split()) < 3:
            short_steps.append(step)

    return short_steps


def check_unclear_steps(steps):
    """
    Detect vague steps
    """
    unclear_keywords = ["process", "handle", "do", "manage"]

    unclear = []

    for step in steps:
        for word in unclear_keywords:
            if word in step.lower():
                unclear.append(step)
                break

    return unclear


def run_all_checks(steps):
    """
    Run all rule validations
    """

    return {
        "duplicate_steps": check_duplicates(steps),
        "short_steps": check_short_steps(steps),
        "unclear_steps": check_unclear_steps(steps)
    }