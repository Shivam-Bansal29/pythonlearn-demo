# program to dmeo match case
x=int(input("Enter day of week "))

match x:
    case 1:
        print("Day is Sunday ")
    case 2:
        print("Day is Monday ")
    case 3:
        print("Day is Tuesday ")
    case 4:
        print("Day is Wednesday ")
    case 5:
        print("Day is Thursday ")
    case 6:
        print("Day is Friday ")
    case 7:
        print("Day is Saturday ")
    case _:
        print("invalid day ")
