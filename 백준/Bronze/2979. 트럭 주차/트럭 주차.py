if __name__ == "__main__":
    one_fee, two_fee, three_fee = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(3)]
    maxtime = max(table[0][1], table[1][1], table[2][1])
    parking = [0] * (maxtime - 1)

    for car in table:
        for i in range(car[0] - 1, car[1] - 1):
            parking[i] += 1

    fee = 0
    for i in parking:
        if i == 1:
            fee += one_fee
        elif i == 2:
            fee += 2 * two_fee
        elif i == 3:
            fee += 3 * three_fee
    print(fee)