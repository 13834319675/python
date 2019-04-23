# 猜拳游戏
import random
translate = ["石头","剪刀","布"]
diannaosun = 0
wanjiasun = 0
n = 0
pingjusun = 0

print("游戏开始!")
print("输入!继续!")
print("输入2退出!")
inp = input("请输入你的选择!:")
if inp == "1":
    wanjia = int(input("请输入要玩的回合数:"))
    while wanjia>0:
        teep = input("你出的是(石头?剪刀?布):")
        if teep in translate:
            teep = teep.strip()
            diannao = random.randint(0,2)
            if translate[diannao]==teep:
                print(translate[diannao],teep)
                pingjusun = pingjusun+1
                print("平局")
            if teep == "石头":
                if diannao == 1:
                    print("玩家胜")
                    wanjiasun = wanjiasun+1
                elif diannao == 2:
                    print("电脑胜")
                    diannaosun = diannaosun+1
            elif teep == "剪刀":
                if diannao == 0:
                    print("玩家胜")
                    wanjiasun = wanjiasun + 1
                elif diannao == 2:
                    print("电脑胜")
                    diannaosun = diannaosun + 1
            elif teep == "布":
                if diannao == 0:
                    print("电脑胜")
                    diannaosun = diannaosun + 1
                elif diannao == 1:
                    print("玩家胜")
                    wanjiasun = wanjiasun + 1
            wanjia = wanjia-1
            n = n+1
        else:
            print("请安规定输入!")
    print("结果!")
    print("进行了{0}回合,玩家赢了{1}回合,电脑赢了{2}回合,平局{3}回合".format(n,wanjiasun,diannaosun,pingjusun))
    if wanjiasun>diannaosun:
        print("你好厉害!赢了电脑!")
    elif wanjiasun == diannaosun:
        print("平湖哎!要不要在在试试!")
        teep = input("你出的是(石头?剪刀?布):")
    else:
        print("笨蛋!居然输了")
elif inp == "2":
    print("退出")
    exit()
print("游戏结束")

