import random

tools = ["rock", "paper", "scissors"]

while True:
    bot_tool = tools[random.randint(0, 2)]
    player_tool = input("Rock or paper or scissor?: ").lower()
    if player_tool == bot_tool:
        print("Tie!")
    elif player_tool == tools[0]:
        if bot_tool == tools[1]:
            print("You lost!")
        elif bot_tool == tools[2]:
            print("You won!")
    elif player_tool == tools[1]:
        if bot_tool == tools[0]:
            print("You won!")
        elif bot_tool == tools[2]:
            print("You lost!")
    elif player_tool == tools[2]:
        if bot_tool == tools[0]:
            print("You lost!")
        elif bot_tool == tools[1]:
            print("You won!")
    elif player_tool == "help":
        print("""
    You can only choose between :
    'rock' or
    'paper' or
    'scissors' or
    'quit'
    """)
    elif player_tool == "quit":
        break
    elif player_tool != tools[0] and player_tool != tools[1] and player_tool != tools[2]\
            and player_tool != "help" and player_tool != "quit":
        print("""
        ERROR->type 'Help' for the allowed commands.

        """)

