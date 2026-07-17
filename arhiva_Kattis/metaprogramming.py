translations = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    words = list(line.split())
    if words[0] == "define":
        translations[words[2]] = int(words[1])
    else:
        if words[1] not in translations or words[3] not in translations:
            print("undefined")
        else:
            a=translations[words[1]]
            comp = words[2]
            b=translations[words[3]]

            if comp == "=" and a == b:
                print("true")
            elif comp == "<" and a < b:
                print("true")
            elif comp == ">" and a > b:
                print("true")
            else:
                print("false")




