import re

def go_to(local):
    phrase_conclusion = "Indo para "
    for loc in local[0]:
        if loc:
            phrase_conclusion += f"{loc} "
    
    return phrase_conclusion

dict_intent = {
    r"\b(?:v[aá]i?|dirija(?:-se)?|leve|ir|me)\s?(?:para|pr[ao]|at[ée]|leve|-?me)?\s?(?:a|o|ao|[aà])?\s?(ponto|prateleira|estante|local|peça|secretaria|labs?(?:orat[óo]rio)?|biblioteca)\s?(\d*)": "go_to",
}

dict_action = {
    "go_to": go_to,
}

def main():
    while True:
        send_command = input("Fala alguma coisa pro robô: ").lower()

        for key, value in dict_intent.items():
            pattern = re.compile(key)
            groups = pattern.findall(send_command)
            if groups:
                print(dict_action[value](groups))
        print()

if __name__ == "_main_":
    main()