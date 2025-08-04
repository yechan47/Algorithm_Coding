N = int(input())
ball = input()

blue = ball.count('B')
red = ball.count('R')

first = ball[0]
red_minus = ball.find('B') if first == 'R' else 0
blue_minus = ball.find('R') if first == 'B' else 0
first_result = min(blue - blue_minus, red - red_minus)
last = ball[-1]
red_minus = len(ball) - ball.rfind('B') - 1 if last == 'R' else 0
blue_minus = len(ball) - ball.rfind('R') - 1 if last == 'B' else 0
last_result = min(blue - blue_minus, red - red_minus)

print(min(first_result, last_result))