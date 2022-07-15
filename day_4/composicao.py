names = ["Bruno", "Joao", "Bernardo", "Barbara", "Brian"]


def start_with_b(name):
    return name[0].lower() == "b"


names_with_b = list(filter(start_with_b, names))
