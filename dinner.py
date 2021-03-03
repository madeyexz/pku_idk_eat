import random
from rich.text import Text
from rich.console import Console
from rich.table import Table

console = Console()
option = open('options.txt','r+')
options = option.readline().split(',')

try:    
    weight = open('weights.txt','r')
    weights = [int(x) for x in weight.readline().split(',')]
except ValueError: #放置初始数值
    text1 = Text()
    text1.append('请重新设定').append('\'weight.txt\'', style='bold magenta')
    console.print(text1)
except FileNotFoundError:
    text2 = Text()
    text2.append('\'weight.txt\'',style = 'bold magenta').append('缺失，请在本程序目录内自行创建。\
        \n配置格式请参考 https://github.com/madeyexz/pku_idk_eat\n你必须要修改！不然你代替我吃虫子！') 
print('您现在给各恰饭地点的权值为: \n')

table = Table(title = '恰饭地点与所赋权值')
table.add_column('恰饭地点',justify='center',style='cyan',no_wrap=True)
table.add_column('权值',justify='center',style='green')
for i in range(len(options)):
    table.add_row(str(options[i]),str(weights[i]))
console.print(table)


basket = []

for i in range(len(options)):
    basket.extend([options[i]] * weights[i])

option.close()
weight.close()

# print(basket) # used in dev
text3 = Text().append('就决定去吃： ').append(random.choice(basket),style='bold red underline').append(' !!!',style='bold')
console.print(text3)