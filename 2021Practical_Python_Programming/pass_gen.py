import string

while 1:
    # TODO: 用户输入密码
    user_password = input("请输入新密码：")

    # TODO: 判断密码安全性
 
    password_state = 0b00000

    for char in user_password: # 下面的条件属于多选一，具有排他性
        if char in string.ascii_uppercase:
            password_state |= 0b10000
        elif char in string.ascii_lowercase:
            password_state |= 0b01000
        elif char in string.digits:
            password_state |= 0b00100
        else:
            password_state |= 0b00010

    if len(user_password) >= 8:
        password_state |= 0b00001

    # TODO: 输出结果

    if password_state == 0b11111:
        print('密码符合要求！')
        break
    else:
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