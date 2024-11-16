def AskNum():
    try:
        int1 = input("Enter an integer 1: ")
        int2 = input("Enter an integer 2: ")

        if not int1.isdigit() or not int2.isdigit():
            raise TypeError("Both inputs must be numerical.")

        print("Success! You entered valid integers.")

    except TypeError as t:
        print(t)

AskNum()
