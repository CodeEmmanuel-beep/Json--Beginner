import math
import statistics


def analyze(sales, operation, period=None):
    if not sales:
        return "No sale inputed"
    if any(s < 0 for s in sales):
        return "Cannot have a negative sale"
    length = len(sales)
    period = (
        input(
            "Enter 'weeks' for weekly calculations, 'days' for daily calculationd or 'current'  for minute by minute calculation for each day sales: "
        )
        .strip()
        .lower()
    )
    if period == "weeks":
        if length > 4:
            return "cannot Process Greater Than Four, Thank You"
        Duration = "Week" if length == 1 else "Weeks"
        limit_type = "month"
    elif period == "days":
        if length > 7:
            return "cannot Process Greater Than Seven, Thank You"
        Duration = "Day" if length == 1 else "Days"
        limit_type = "week"
    elif period == "current":
        Duration = "Minute"
        limit_type = "Day"
    else:
        return "error invalid input"

    short = {
        "add": "add",
        "avg": "avg",
        "best": "best",
        "worst": "worst",
        "range": "range",
        "freq": "freq",
        "bonus": "bonus",
    }
    result = {
        "add": f"Total for {length} {Duration} ({limit_type}): {sum(sales)}",
        "avg": f"Average for {length} {Duration} ({limit_type}): {sum(sales)/length:.2f}",
        "best": f"Best sale in {length} {Duration}: {max(sales)}",
        "worst": f"Worst sale in {length} {Duration}: {min(sales)}",
        "range": f"Range For {length} {Duration}: {max(sales) - min(sales)}",
        "freq": f"Most Frequent Sale(s) in {length} {Duration}: {statistics.multimode(sales)}",
        "bonus": f"Gain for {length} {Duration} ({limit_type}): {math.sqrt(0.1*sum(sales)):.2f}",
    }

    operation = short.get(operation.strip().lower(), operation.strip().lower())
    return result.get(operation, "Try Again")


def tax(sales, rate, operation):
    if operation == "rate":
        if isinstance(sales, (int, float)):
            return [sales + sales * rate / 100]
        if isinstance(sales, list):
            return [s + s * rate / 100 for s in sales]
