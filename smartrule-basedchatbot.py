import datetime
import random

# ---------------------------
# CHAT HISTORY
# ---------------------------

def save_history(message):

    with open(
        "chat_history.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(message + "\n")

# ---------------------------
# JOKES
# ---------------------------

jokes = [

    "Why do programmers hate nature? Because it has too many bugs.",

    "Why did Python go to school? To improve its class.",

    "Why do Java developers wear glasses? Because they cannot C#.",

    "Debugging is like being a detective in a crime movie where you are also the criminal."
]

# ---------------------------
# QUOTES
# ---------------------------

quotes = [

    "Success is the sum of small efforts repeated day in and day out.",

    "Believe you can and you're halfway there.",

    "Dream big. Start small. Act now.",

    "Every expert was once a beginner."
]

# ---------------------------
# HELP MENU
# ---------------------------

def show_help():

    print("\nAVAILABLE COMMANDS")
    print("-" * 30)

    print("hello")
    print("time")
    print("date")
    print("calculator")
    print("joke")
    print("quote")
    print("about")
    print("help")
    print("bye")

# ---------------------------
# CALCULATOR
# ---------------------------

def calculator():

    try:

        num1 = float(
            input("Enter First Number: ")
        )

        num2 = float(
            input("Enter Second Number: ")
        )

        op = input(
            "Operation (+,-,*,/): "
        )

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":

            if num2 == 0:
                print("Cannot divide by zero.")
                return

            result = num1 / num2

        else:

            print("Invalid Operation.")
            return

        print("Result =", result)

    except ValueError:

        print("Invalid Input.")

# ---------------------------
# CHATBOT
# ---------------------------

def chatbot():

    print("=" * 50)
    print("SMART CHATBOT")
    print("=" * 50)

    name = input(
        "\nEnter Your Name: "
    )

    print(
        f"\nHello {name}! Type 'help' to see commands."
    )

    while True:

        user = input(
            f"\n{name}: "
        ).lower()

        save_history(
            f"{name}: {user}"
        )

        if user == "hello":

            response = (
                f"Hello {name}! Nice to see you."
            )

        elif user == "time":

            response = (
                datetime.datetime.now()
                .strftime(
                    "Current Time: %I:%M %p"
                )
            )

        elif user == "date":

            response = (
                datetime.datetime.now()
                .strftime(
                    "Today's Date: %d-%m-%Y"
                )
            )

        elif user == "joke":

            response = random.choice(
                jokes
            )

        elif user == "quote":

            response = random.choice(
                quotes
            )

        elif user == "calculator":

            calculator()
            continue

        elif user == "about":

            response = (
                "I am a Python Rule-Based Chatbot."
            )

        elif user == "help":

            show_help()
            continue

        elif user == "bye":

            response = (
                "Goodbye! Have a great day."
            )

            print(
                "\nBot:",
                response
            )

            save_history(
                "Bot: " + response
            )

            break

        else:

            response = (
                "Sorry, I don't understand that command."
            )

        print("\nBot:", response)

        save_history(
            "Bot: " + response
        )

# ---------------------------
# START
# ---------------------------

if __name__ == "__main__":
    chatbot()
