def can_you_add_this(num1, num2):

    return num1 + num2

if __name__ == "__main__":

    for _ in range(int(input())):

        num1, num2 = map(int, input().split())

        

        print(can_you_add_this(num1, num2))