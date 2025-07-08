from api import fetch_latest_result

def get_prediction():
    result = fetch_latest_result()
    number = result['number']

    # LCG (a=2, c=9, m=10)
    next_lcg = (2 * number + 9) % 10

    # Rick rules
    mapping = {
        1: "Small Green", 3: "Small Green",
        2: "Small Red", 4: "Small Red",
        7: "Big Green", 9: "Big Green",
        6: "Big Red", 8: "Big Red",
        0: "Red + Violet",
        5: "Green + Violet"
    }

    size_color = mapping.get(next_lcg, "Unknown")
    return f"🔮 Predicted Next: {next_lcg} – {size_color}"