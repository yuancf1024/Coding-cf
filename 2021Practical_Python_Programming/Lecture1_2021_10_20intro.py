#%%
# _*_ coding: utf-8 _*_

#%% 第一行程序

print("Hello World!")
# %% 测试IPython是否乱码

print("你好！chenfeng.")

# %% 测试linux指令——输出当前工作目录下的内容
# ls

# %% 输出当前工作目录
# pwd

# %% 基本数据类型
# 整数
# int 783 0 -192 0b010 0o642 0xF3
# 整数、0、负数、二进制、八进制、十六进制
print(783, 0, -192, 0b010, 0o642, 0xF3)
# %% 
# 浮点数
# float 9.23 0.0 -1.7e-6
print(9.23, 0.0, -1.7e-6)
# %%
# 布尔型
# bool True False
print(True, False)
# %%
# 字符型
# str "One\nTwo" 'I\'m' 
# """X\tY\tZ
# 1\t2\t3
# """
print("One\nTwo", 'I\'m') # 一个制表符-跳动7格

# 多行字符串
print("""X\tY\tZ
1\t2\t3""")

# 单引号和双引号的区别
print("I'm a teacher") # 方法1
print('I\'m a teacher') # 转义
print("I'm a teacher\nYeah!") # 程序型表达

# 三引号 原封不动保存原字符串的格式

print('Hello' + ' ' + 'World')
# %%
# 字节型
# bytes b"toto\xfe\775"
print(b"toto\xfe\775")


# %% 容器类型——列表

# 顺序序列：快速索引访问，重复值
# list [] [1,5,9] ["x",11,8.9] ["mot"]
# tuple () (1,5,9) 11,"y",7.4 ("mot",)
# str "" b"" bytes 字符串/字节的有序序列
# 元组和字符串是不可变的

# 键值容器：没有优先顺序，快速键值访问，每一个键都是独一无二的
# dictionary {} dict {"key": "value"} dicrt(a=3,b=4,k="v")
# (key/value associations) {1:"one",3:"three",2:"two",3.14:"n"}

# collection set() set {"key1", "key2"} {1,9,3,0}
# keys=hashable values(base types, immutable...)
# frozenset immutable set

# %% 数据四要素

id(345)

a = 345

id(a)

# %%
