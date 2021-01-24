# 所以等一下吃什么？
解决在北大的饮食选择困难

## Philosophy
构想这个程序的时候是想说**越简单越好**，不需要考虑任何因素，把选项手动输进去然后直接输出一个选项就好了。

但后来想了想决定增加一个模式，把“餐厅人数”、“时间”等参数也考虑进去，最后输出一个依靠分析结果、随机性不那么强的选项。

## 使用说明
1. 打开命令行，输入`python3` 然后把文件拖进去（当然直接用编译器跑也不是不行）

（到时候我可能会考虑把它变成一个`alias`这样以后就可以直接在terminal里面决定了😂）

## 特色
- 目前选项极少
- 家园的权值极大
  - 会帮你决定去家园的几楼

## TODO
1. 从校网爬取餐厅信息（人数、名称）
2. 增加“外卖”选项到餐厅list
3. 增加“时间获取”模块（no input; output: now)
4. 编写餐厅人数分析模块（input: time; output: occupied percentage）
4. 编写“选择生成”模块 (input: occpied percentage, )
5. 加入“模式选择”模块（PURE RANDOM, TIME-BASED-RMD,
6. 修改外观 (via *[rich](https://github.com/willmcgugan/rich)*)


---

initiated on 20210110, four days before **高数期末考**