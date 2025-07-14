num = int(input("Enter a Number"))

match num:
    case 10:
        print("Ten")
    case 20:
        print("Twenty")
    case _:
        print("Invalid")