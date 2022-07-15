def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.")


def ask_questions():
    name = input("name:")
    print(f"It is nice to meet you {name}")

    color = input("Quat is your favorite color?")
    print(f"{color} is a great color!")

    input("Describe yourself")
    print("admirable!")


def goodbye():
    print("Goodbye.)


welcome()
ask_questions()
goodbye()
