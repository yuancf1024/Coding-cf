import string
import random

# TODO: 用户输入密码
# TODO: 判断密码安全性


def evaluate_password(password, show_info=True):
    result = False
    password_state = 0b00000

    for char in password: # 下面的条件属于多选一，具有排他性
        if char.isupper():
            password_state |= 0b10000
        elif char.islower():
            password_state |= 0b01000
        elif char.isdigit():
            password_state |= 0b00100
        else:
            password_state |= 0b00010

    if len(password) >= 8:
        password_state |= 0b00001
    
    # TODO: 输出结果
    if password_state == 0b11111:
        if show_info:
            print('密码符合要求！')
        result = True
    else:
        if show_info:
            prompt = '密码不符合要求，' # 下面的条件属于并行判断
            if password_state & 0b00001 == 0: # 长度不足8时，按位与为0
                prompt += '长度不足8，'
            if password_state & 0b10000 == 0:
                prompt += '没有包含大写符号，'
            if password_state & 0b01000 == 0:
                prompt += '没有包含小写符号，'
            if password_state & 0b00100 == 0:
                prompt += '没包含数字，'
            if password_state & 0b00010 == 0:
                prompt += '没包含标点，'
            prompt = prompt[:-1]
            print(prompt)
    return result


def generate_password():
    all_char_set = string.printable
    # print(all_char_set)
    all_char_set *=  9
    # print(all_char_set)
    result = ''.join(random.sample(all_char_set, k=9))
    return result

def create_password(pass_length, confuse=False):
    result = ''
    # TODO: 生成指定长度包含四类字符的密码前四位
    result += random.choice(string.ascii_uppercase)
    result += random.choice(string.ascii_lowercase)
    result += random.choice(string.digits)
    result += random.choice(string.punctuation)
    # print(result)
    if confuse:
        result += 'Il'
        result += ''.join(random.sample(string.printable[:-6]*pass_length, pass_length-6))
    else:
        result += ''.join(random.sample(string.printable[:-6]*pass_length, pass_length-4))
    # TODO：对生成密码进行随机打乱
    # random.shuffle(result)
    # print(result)
    result = ''.join(random.sample(result, len(result)))
    return result

def main_userinput():
    while 1:
        user_password = input("请输入新密码：")
        if evaluate_password(user_password):
            break

def main_genpassword():
    while 1:
        user_password = generate_password()
        if evaluate_password(user_password, show_info=False):
            print(f"新生成密码为：{user_password}")
            break

def main():
    for i in range(1):
        print(f"新生成密码为：{create_password(12, True)}")

main()