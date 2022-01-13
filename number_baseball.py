from random import randint
from os import system

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        rand_num = randint(0, 9)
        if rand_num not in numbers:
            numbers.append(rand_num)

    return numbers

def take_guess():
    new_guess = []
    count = 0
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    while count < 3:
        temp = int(input('{}번째 숫자를 입력하세요: '.format(count+1)))
        if temp > 9 or temp < 0:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        elif temp in new_guess:
            print('중복되는 숫자압니다. 다시 입력하세요.')
        else:
            new_guess.append(temp)
            count += 1
    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for num_count in range(len(guess)):
        if guess[num_count] == solution[num_count]:
            strike_count += 1
        elif guess[num_count] in solution:
            ball_count += 1

    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0
strike = 0
print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
while strike != 3:
    GUESS = take_guess()
    strike, ball  = get_score(GUESS, ANSWER)
    print('{}S {}B\n'.format(strike, ball))
    tries += 1
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
print('답은' , str(ANSWER[0])+str(ANSWER[1])+str(ANSWER[2]), '이었습니다!')
system('pause')
