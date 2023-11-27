def created(sentence):
    trasnslation = ""
    for element in sentence:
        if element in "Aa":
            trasnslation = trasnslation + "1"
        elif element in "Bb":
            trasnslation = trasnslation + "2"
        elif element in "Cc":
            trasnslation = trasnslation + "3"
        elif element in "Dd":
            trasnslation = trasnslation + "4"
        elif element in "Ee":
            trasnslation = trasnslation + "5"
        elif element in "Ff":
            trasnslation = trasnslation + "6"
        elif element in "Gg":
            trasnslation = trasnslation + "7"
        elif element in "Hh":
            trasnslation = trasnslation + "8"
        elif element in "Ii":
            trasnslation = trasnslation + "9"
        elif element in "Jj":
            trasnslation = trasnslation + "!"
        elif element in "Kk":
            trasnslation = trasnslation + "@"
        elif element in "Ll":
            trasnslation = trasnslation + "#"
        elif element in "Mm":
            trasnslation = trasnslation + "$"
        elif element in "Nn":
            trasnslation = trasnslation + "%"
        elif element in "Oo":
            trasnslation = trasnslation + "^"
        elif element in "Pp":
            trasnslation = trasnslation + "&"
        elif element in "Qq":
            trasnslation = trasnslation + "*"
        elif element in "Rr":
            trasnslation = trasnslation + "("
        elif element in "Ss":
            trasnslation = trasnslation + ")"
        elif element in "Tt":
            trasnslation = trasnslation + "-"
        elif element in "Vv":
            trasnslation = trasnslation + "+"
        elif element in "Ww":
            trasnslation = trasnslation + "|"
        elif element in "Xx":
            trasnslation = trasnslation + "]"
        elif element in "Yy":
            trasnslation = trasnslation + "["
        elif element in "Zz":
            trasnslation = trasnslation + "{"
        else:
            trasnslation = trasnslation + element
    return trasnslation

print(created("vishalrathod8788"))