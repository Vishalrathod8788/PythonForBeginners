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
            trasnslation = trasnslation + "_"
        elif element in "Vv":
            trasnslation = trasnslation + "="
        elif element in "Ww":
            trasnslation = trasnslation + "|"
        elif element in "Xx":
            trasnslation = trasnslation + "]"
        elif element in "Yy":
            trasnslation = trasnslation + "["
        elif element in "Zz":
            trasnslation = trasnslation + "*"
        elif element in "1":
            trasnslation = trasnslation + "-"
        elif element in "2":
            trasnslation = trasnslation + "+"
        elif element in "3":
            trasnslation = trasnslation + "."
        elif element in "4":
            trasnslation = trasnslation + "/"
        elif element in "5":
            trasnslation = trasnslation + ">"
        elif element in "6":
            trasnslation = trasnslation + "<"
        elif element in "7":
            trasnslation = trasnslation + ","
        elif element in "8":
            trasnslation = trasnslation + "`"
        elif element in "9":
            trasnslation = trasnslation + "~"
        else:
            trasnslation = trasnslation + element
    return trasnslation

print(created(input("What do you want to cript...")))