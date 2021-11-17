# TODO: 用户输入密码
user_password = input("请输入新密码：")

# TODO: 判断密码安全性
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'
PUNCTUATION = '~!@#$%^&*()_+-+:";\'<>,./\\?'

have_upper = False
have_lower = False
have_digit = False
have_punctuation = False

for char in user_password:
    if char in UPPER:
        have_upper = True
    if char in LOWER:
        have_lower = True
    if char in DIGIT:
        have_digit = True
    if char in PUNCTUATION:
        have_punctuation = True

is_secure = (have_upper 
    and have_lower 
    and have_digit 
    and have_punctuation)
# TODO: 输出
print(is_secure)
