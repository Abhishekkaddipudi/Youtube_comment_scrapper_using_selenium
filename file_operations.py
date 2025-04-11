import json


def count_json_length(data):
    count = 0
    for i in data:
        count += len(i["replies"])
    return len(data) + count


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_to_txt(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(f"Comment: {item.get('comment', '')}\n")
            replies = item.get("replies", [])
            for reply in replies:
                f.write(f"  ↳ Reply: {reply}\n")
            f.write("\n")


def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data


def json_to_text(file_path):
    """
    Reads a JSON file and converts it to a formatted text string.
    Returns the text.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    output = ""

    if isinstance(data, list):
        for idx, item in enumerate(data, start=1):
            output += f"Item {idx}:\n"
            for key, value in item.items():
                output += f"  {key.capitalize()}: {value}\n"
            output += "\n"
    elif isinstance(data, dict):
        for key, value in data.items():
            output += f"{key.capitalize()}: {value}\n"
    else:
        output = str(data)

    return output
