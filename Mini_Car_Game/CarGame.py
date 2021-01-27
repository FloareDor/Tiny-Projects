command = ""
    started = False
    stopped = False
    while True:
        command = input("command:").lower()
        if command == "start":
            if not started:
                started = True
                print("Car has now been started")
            elif started:
                print("The Car has already been started :)")

        elif command == "stop":
            if stopped:
                print("The car is already at rest :)")
            elif not stopped:
                stopped = True
                print("The car is now stopped")
        elif command == "quit":
            break
        elif command == "help":
            print("""
           start -> to start the car
           stop -> to stop the car
           quit -> to exit
           """)
