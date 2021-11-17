import random
import time

def chou_1(u_list):
    selected_user_info = random.choice(u_list).split('\t')
    print(f"恭喜中奖用户：{selected_user_info[0]} {selected_user_info[1]}")
    return selected_user_info[0]

def chou_2(u_list):
    while 1:
        try:
            idx = int(time.time()*1000) % len(u_list)
            print(f"\r{u_list[idx]}   ", end='')
            time.sleep(0.001)
        except KeyboardInterrupt:
            break
    # print(idx)
    selected_user_info = u_list[idx].split('\t')
    print(f"\r恭喜中奖用户：{selected_user_info[0]} {selected_user_info[1]}         ")
    return selected_user_info[0]

def chou_3(u_list):
    while 1:
        rand_x = random.randint(0,10000) / 10
        rand_y = random.randint(0,10000) / 10
        try:
            print(f"\r{rand_x}, {rand_y}", end='')
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        
    user_distance_list = []
    for user_info in u_list:
        uid, uname, ux, uy = user_info.split('\t')
        distance = int((int(ux) - rand_x) ** 2 + (int(uy) - rand_y) ** 2)
        user_distance_list.append((uid, uname, distance))

    user_distance_list.sort(key=lambda x:x[2])
    print(f"\r恭喜中奖用户：{user_distance_list[0][0]} {user_distance_list[0][1]} ")

def main():
    with open('users.txt') as f:
        content = f.read()

    user_list = content.split("\n")
    # print(user_list)
    
    chou_1(user_list)
    chou_2(user_list)
    chou_3(user_list)

main()