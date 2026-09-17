print("Questão 3: Turno de Estudo \n")

turno = input("M = Matutino\nV = Vespertino\nN = Noturno\nEm qual turno voce estuda:  ")

match turno:
    case "M" | "m":
        print("Bom dia!")
    case "V" | "v":
        print("Bom Tarde!")
    case "N" | "n":
        print("Bom Noite!")
    case _:
        print("Turno inválido!")