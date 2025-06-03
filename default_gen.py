import os

# ——————————————————————————————————————————————
#Character maps
# ——————————————————————————————————————————————
char_map1 = {
    'a': 'あ', 'e': 'え', 'i': 'い', 'o': 'お', 'u': 'う',
    'A': 'あ', 'E': 'え', 'I': 'い', 'O': 'お', 'U': 'う',
    'n': 'ん', 'N': 'ん'
}
char_map2 = {
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'Ka': 'か', 'Ki': 'き', 'Ku': 'く', 'Ke': 'け', 'Ko': 'こ',
    'KA': 'か', 'KI': 'き', 'KU': 'く', 'KE': 'け', 'KO': 'こ'
}
char_map3 = {
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'Sa': 'さ', 'Shi': 'し', 'Su': 'す', 'Se': 'せ', 'So': 'そ',
    'SA': 'さ', 'SHI': 'し', 'SU': 'す', 'SE': 'せ', 'SO': 'そ'
}
char_map4 = {
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'Ta': 'た', 'Chi': 'ち', 'Tsu': 'つ', 'Te': 'て', 'To': 'と',
    'TA': 'た', 'CHI': 'ち', 'TSU': 'つ', 'TE': 'て', 'TO': 'と'
}
char_map5 = {
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'Na': 'な', 'Ni': 'に', 'Nu': 'ぬ', 'Ne': 'ね', 'No': 'の',
    'NA': 'な', 'NI': 'に', 'NU': 'ぬ', 'NE': 'ね', 'NO': 'の'
}
char_map6 = {
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'Ha': 'は', 'Hi': 'ひ', 'Fu': 'ふ', 'He': 'へ', 'Ho': 'ほ',
    'HA': 'は', 'HI': 'ひ', 'FU': 'ふ', 'HE': 'へ', 'HO': 'ほ'
}
char_map7 = {
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'Ma': 'ま', 'Mi': 'み', 'Mu': 'む', 'Me': 'め', 'Mo': 'も',
    'MA': 'ま', 'MI': 'み', 'MU': 'む', 'ME': 'め', 'MO': 'も'
}
char_map8 = {
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'Ra': 'ら', 'Ri': 'り', 'Ru': 'る', 'Re': 'れ', 'Ro': 'ろ',
    'RA': 'ら', 'RI': 'り', 'RU': 'る', 'RE': 'れ', 'RO': 'ろ'
}
char_map9 = {
    'wa': 'わ', 'wi': 'ゐ', 'we': 'ゑ', 'wo': 'を',
    'Wa': 'わ', 'Wi': 'ゐ', 'We': 'ゑ', 'Wo': 'を',
    'WA': 'わ', 'WI': 'ゐ', 'WE': 'ゑ', 'WO': 'を'
}
char_map10 = {
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'Ya': 'や', 'Yu': 'ゆ', 'Yo': 'よ',
    'YA': 'や', 'YU': 'ゆ', 'YO': 'よ'
}
char_map_11_dakuon = {

    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'Ga': 'が', 'Gi': 'ぎ', 'Gu': 'ぐ', 'Ge': 'げ', 'Go': 'ご',
    'GA': 'が', 'GI': 'ぎ', 'GU': 'ぐ', 'GE': 'げ', 'GO': 'ご',
    'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'Za': 'ざ', 'Ji': 'じ', 'Zu': 'ず', 'Ze': 'ぜ', 'Zo': 'ぞ',
    'ZA': 'ざ', 'JI': 'じ', 'ZU': 'ず', 'ZE': 'ぜ', 'ZO': 'ぞ',
    'da': 'だ', 'du': 'づ', 'de': 'で', 'do': 'ど',
    'Da': 'だ', 'Du': 'づ', 'De': 'で', 'Do': 'ど',
    'DA': 'だ', 'DU': 'づ', 'DE': 'で', 'DO': 'ど',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'Ba': 'ば', 'Bi': 'び', 'Bu': 'ぶ', 'Be': 'べ', 'Bo': 'ぼ',
    'BA': 'ば', 'BI': 'び', 'BU': 'ぶ', 'BE': 'べ', 'BO': 'ぼ',
}
char_map_12_handakuon = {
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'Pa': 'ぱ', 'Pi': 'ぴ', 'Pu': 'ぷ', 'Pe': 'ぺ', 'Po': 'ぽ',
    'PA': 'ぱ', 'PI': 'ぴ', 'PU': 'ぷ', 'PE': 'ぺ', 'PO': 'ぽ',
}

# ——————————————————————————————————————————————
#All maps into one
# ——————————————————————————————————————————————
char_map_all = {}

for cm in (char_map2, char_map3, char_map4, char_map5,
           char_map6, char_map7, char_map8, char_map9, char_map10, char_map_11_dakuon, char_map_12_handakuon):
    char_map_all.update(cm)

# ——————————————————————————————————————————————
#Greedy replacer helper
# ——————————————————————————————————————————————
def replace_text(text: str, mapping: dict) -> str:
    """
    Walk the text and replace any key in 'mapping' with its value,
    matching longest keys first.
    """
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

# ——————————————————————————————————————————————
#Two‐stage generator
# ——————————————————————————————————————————————
vowels = ['a', 'e', 'i', 'o', 'u']
multi_keys = sorted(char_map_all.keys(), key=len, reverse=True)

def convert_default_repetitive(text: str) -> list[str]:
    paragraphs = []

    vowel_map = {}
    for v in vowels:
        vowel_map[v] = char_map1[v]
        vowel_map[v.upper()] = char_map1[v.upper()]
        paragraphs.append(replace_text(text, vowel_map))
    multi_map = {}
    for i in range(0, len(multi_keys), 2):
        added = False
        for k in multi_keys[i:i+2]:
            if k in text:
                multi_map[k] = char_map_all[k]
                added = True
        if not added:
            continue
        paragraphs.append(replace_text(text, multi_map))

    return paragraphs

# ——————————————————————————————————————————————
#Main: read, convert, write
# ——————————————————————————————————————————————
def main():
    input_file = "input.txt"
    output_file = "output_def.txt"

    if not os.path.exists(input_file):
        print(f"[!] Input file '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8-sig") as f:
        source = f.read()

    paras = convert_default_repetitive(source)

    with open(output_file, "w", encoding="utf-8-sig") as f:
        for idx, p in enumerate(paras, 1):
            f.write(f"--- Paragraph {idx} ---\n")
            f.write(p + "\n\n")
    print(f"[✓] Generated {len(paras)} paragraphs → '{output_file}'")
def print_main():
    read_file = "output_def.txt"
    with open(read_file, "r", encoding="utf-8-sig") as f:
        for line in f:
            print(line.strip())
if __name__ == "__main__":
    main()  
    print_main()