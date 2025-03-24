import random

count = 0       # 현재 입력된 횟수
chance = 10     # 총 입력 기회

number = random.randint(1, 100)

print("1부터 100까지의 숫자를 {}번 안에 맞춰보세요.".format(chance))

while count < chance:
    count += 1
    user_input = int(input("몇 일까요?> "))

    if user_input == number:
        break
    elif user_input < number:
        print("{} 보다 큰 숫자 입니다.".format(user_input))
    elif user_input > number:
        print("{} 보다 낮은 숫자 입니다.".format(user_input))

    print("기회가{} 번 남았습니다.".format(chance-count))

if user_input == number:
    print("성공!! {} 이 맞습니다.".format(number))
elif count == 10:
    print("실패하셨습니다.")
else
    print("실패, 정답은 {} 입니다.".format(number))
