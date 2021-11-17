import random
import os
import time

def main():
    ALL_DIGITS = '01234567890'
    MAX_TRY = 6
    NUM_DIGITS = 3

    os.system('cls') # 执行命令行的命令
    print(f'我想好了一个{NUM_DIGITS}位不重复的数字，你来猜猜看？')

    target = ''.join(random.sample(ALL_DIGITS, k=NUM_DIGITS))
    # print(target)

    round = 1
    start_time = int(time.time())
    while True:
        while True:
            guess = input('> ')
            if len(guess) == NUM_DIGITS \
                and len(guess) == len(set(guess)) \
                and guess.isdigit():
                break
            else:
                print(f'请输入{NUM_DIGITS}位不重复的数字')

        if guess == target:
            print('猜对了！你真棒！')
            end_time = int(time.time())
            print(f'总共猜了{round}次，用时{end_time-start_time}秒')
            break
        else:
            print(get_glue(target, guess))
        if round > MAX_TRY:
            print(f'您已经猜了{round}个数字，挑战失败！')
            break
        round += 1

def get_glue(target, guess):
    glue = ''
    for index in range(len(guess)):
        if guess[index] == target[index]:
            glue += '✅'
        elif guess[index] in target:
            glue += '⭕'
        else:
            glue += '❌'
        glue = ''.join(sorted(list(glue)))
    return glue

main()