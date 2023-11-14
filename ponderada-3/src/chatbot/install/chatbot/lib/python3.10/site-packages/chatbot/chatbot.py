#! /bin/env python3
import re

def go_to(local):
    phrase = "Indo para "
    for loc in local[0]:
        if loc:
            phrase += f"{loc} "
    
    return phrase

intent_dict = {
    r"\b(?:v[aá]i?|dirija(?:-se)?|leve|ir|me)\s?(?:para|pr[ao]|at[ée]|leve|-?me)?\s?(?:a|o|ao|[aà])?\s?(ponto|prateleira|estante|local|peça|secretaria|labs?(?:orat[óo]rio)?|biblioteca)\s?(\d*)": "go_to",
}

action_dict = {
    "go_to": go_to,
}

def main():
    while True:
        command = input("Fala alguma coisa pro robô: ").lower()

        for key, value in intent_dict.items():
            pattern = re.compile(key)
            groups = pattern.findall(command)
            if groups:
                print(action_dict[value](groups))
        print()

if __name__ == "_main_":
    main()