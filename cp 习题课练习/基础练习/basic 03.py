# 猜拳游戏
import random
translate = ["石头","剪刀","布"]

teep = input("你出的是石头?剪刀?布:")
diannao = random.randint(0,2)
if translate[diannao]==teep:
    print(translate[diannao],teep)
    print("平局")
if teep == "石头":
    if diannao == 1:
        print("玩家胜")
    elif diannao == 2:
        print("电脑胜")
elif teep == "剪刀":
    if diannao == 0:
        print("玩家胜")
    elif diannao == 2:
        print("电脑胜")
elif teep == "布":
    if diannao == 0:
        print("电脑胜")
    elif diannao == 1:
        print("玩家胜")

print(diannao,teep)

