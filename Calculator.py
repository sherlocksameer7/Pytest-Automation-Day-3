def add_two_num(a, b):
    return a+b

def sub_two_num(a, b):
    return a-b

def mul_two_num(a, b):
    return a*b

def div_two_num(a, b):
    return a/b

if __name__ == "__main__":


    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))

    Addition = add_two_num(a, b)
    print(Addition)

    Subtraction = sub_two_num(a, b)
    print(Subtraction)

    Multiplication = mul_two_num(a, b)
    print(Multiplication)

    Division = div_two_num(a, b)
    print(Division)


