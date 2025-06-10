import os
def load_chosen_map(filepath="chosen_map.txt") -> dict:

    chosen_map = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    chosen_map[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"[!] '{filepath}' not found.")
    return chosen_map


def replace_text(text: str, mapping: dict) -> str:
    result = []
    i = 0
    keys = sorted(mapping.keys(), key=len, reverse=True)
    while i < len(text):
        for k in keys:
            if text.startswith(k, i):
                result.append(mapping[k])
                i += len(k)
                break
        else:
            result.append(text[i])
            i += 1
    return ''.join(result)


def convert_from_chosen_map(text: str, chosen_map: dict) -> list[str]:

    paragraphs = []
    cumulative = {}
    keys = sorted(chosen_map.keys(), key=len, reverse=True)

    for i in range(0, len(keys), 2):
        added = False

        # Try to add key i
        k1 = keys[i]
        if k1 in text:
            cumulative[k1] = chosen_map[k1]
            added = True

        # Try to add key i+1
        if i + 1 < len(keys):
            k2 = keys[i + 1]
            if k2 in text:
                cumulative[k2] = chosen_map[k2]
                added = True

        if added:
            converted = replace_text(text, cumulative)
            paragraphs.append(converted)

    return paragraphs


def main_chosen(text, chosen_map={}):
    input_file = "input.txt"
    chosen_map = "chosen_map.txt"
    output_file = "output_chosen.txt"
    if not os.path.exists(input_file):
        print(f"[!] Input file '{input_file}' not found.")
        return


    paragraphs = convert_from_chosen_map(text, chosen_map)

    with open(output_file, "w", encoding="utf-8-sig") as f:
        for i, p in enumerate(paragraphs, 1):
            f.write(f"--- Paragraph {i} ---\n{p}\n\n")

    print(f"[✓] {len(paragraphs)} paragraphs written to '{output_file}'.")
def print_chosen():
    read_file = "output_chosen.txt"
    with open(read_file, "r", encoding="utf-8-sig") as f:
        for line in f:
            print(line.strip())


if __name__ == "__main__":
    main_chosen()
    print_chosen()