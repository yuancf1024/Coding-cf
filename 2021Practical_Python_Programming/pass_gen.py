while 1:
    # TODO: 用户输入密码
    user_password = input("请输入新密码：")

    # TODO: 判断密码安全性
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    DIGIT = '0123456789'
    # PUNCTUATION = '~!@#$%^&*()_+-+:";\'<>,./\\?'

    have_upper = False
    have_lower = False
    have_digit = False
    have_punctuation = False

    for char in user_password: # 下面的条件属于多选一，具有排他性
        if char in UPPER:
            have_upper = True
        elif char in LOWER:
            have_lower = True
        elif char in DIGIT:
            have_digit = True
        # if char in PUNCTUATION:
        else:
            have_punctuation = True
    have_enough_char = len(user_password) >= 8

    is_secure = (have_enough_char
        and have_upper 
        and have_lower 
        and have_digit 
        and have_punctuation)
    # TODO: 输出
    # print(is_secure)

    if is_secure:
        print('密码符合要求！')
        break
    else:
        prompt = '密码不符合要求，' # 下面的条件属于并行判断
        if not have_enough_char:
            prompt += '长度不足8，'
        if not have_upper:
            prompt += '没有包含大写符号，'
        if not have_lower:
            prompt += '没有包含小写符号，'
        if not have_digit:
            prompt += '没包含数字，'
        if not have_punctuation:
            prompt += '没包含标点，'
        prompt = prompt[:-1]
        print(prompt)

