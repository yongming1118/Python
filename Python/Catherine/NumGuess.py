import random

print("我是一个机器人，我有一个秘密数字，来猜一猜吧！")

min=int(input("你想猜最小数是多少："))
max=int(input("你想猜最大数是多少："))
while max < min:
    print("你输入的数据有误。")
    min=int(input("你想猜最小数是多少："))
    max=int(input("你想猜最大数是多少："))

maxTries =int(input("你能在几次前猜中："))
secret=random.randint( min,max)
guess=0
tries=0

print("这个数字在"+str(min)+","+str(max)+"之间，我会给1你"+str(maxTries)+"次猜的机会。")
while guess != secret and tries < maxTries:
    tries = tries + 1
    tip = "请做出你的第" + str(tries) + "尝试："
    guess =int(input(tip))
     
    if guess < secret:
        print(")这个数太小了。")
    elif guess > secret:
        print("这个数太大了。")
if guess == secret:
    
    print("恭喜你，猜对了。你真棒！")
else:
    print("机会已经用完了，不能再猜了。")
    print("那个秘密数字是", secret)



