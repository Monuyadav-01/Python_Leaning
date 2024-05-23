x = int(input("Enter number : "))
match x:
    case 0:
        print("output is 0")
    case 2:
        print("output is 2")
    case _:
        print("Output is", x)
