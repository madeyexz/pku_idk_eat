import random
import datetime


# return date and time
def collect_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
def collect_population():
    



def collect_weight() #收集权值
    weight = [int(x) for x in input('输入对以下xxx的偏好，格式如1 3 4 1')]
    wls = []
    jy = 50 # 家园的权值
    return wls

def option_generator(time,population,weightlist)
    dinner_option = ["学一","学五","最美时光","农园","艺园"]
    dinner_option.extend("家园" for _ in range(jy))
    option = random.choice(dinner_option)
    return option
    
def option_flr()
        flr = random.randint(2,4)
        print('去家园%d楼吧' % flr)

def main():
    option = option_generator()
    print("等一下去吃%s！" % option)

    if option == '家园':
        home_flr()

if __name__ == '__main__':
    main()