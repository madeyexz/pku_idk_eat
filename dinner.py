import random

jy = 50 # 家园的权值

dinner_choice = ["学一","学五","最美时光","农园","艺园"]
dinner_choice.extend("家园" for _ in range(jy))
# to_run_or_not_to_run = ["YES","NO"] #决定要不要去跑步
choice = random.choice(dinner_choice)
print("等一下去吃%s！" % choice)
# print("To run or not to run: ", random.choice(to_run_or_not_to_run))

if choice == '家园':
    flr = random.randint(2,4)
    print('去家园%d楼吧！' % flr)