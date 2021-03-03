# 所以等一下吃什么？
——解决在校园的饮食选择困难

## Philosophy
**简单简洁**，仅需考虑自己对这个觅食场所的偏好（意愿点或说权值）

## Requirement
- [rich](https://github.com/willmcgugan/rich)
    - installation guide `pip3 install rich`, [for more information](https://github.com/willmcgugan/rich#installing)

## Usage
1. open terminal, `cd` to desired directory, `git clone https://github.com/madeyexz/pku_idk_eat.git`
2. 对照打开`options.txt`以及`weights.txt`依照自己对食堂的喜爱程度设定权值并保存
3. on terminal, `cd pku_idk_eat` and then `python3 dinner.py`

## 如何让这个东西更nb
- 获取地理位置、获取[餐厅人数数据](https://portal.pku.edu.cn/portal2017/#/pub/canteenH)（需登入）、获取餐厅价格相关数据（可能需要手动获取）并纳入分析考量
- 根据早中晚三餐提供不同的选项
- 写成mobile app

## 有关选项自定义
考虑到有人会把外卖选项加进去，但外卖种类繁复，有需要的人可以自行撰写，步骤如下：
1. 打开`options.txt`并在想要出现的顺序写上想添加的项目 (e.g. `麦当当,肯德基,三只松树`，注意以*半角*逗号区分项目)
2. 打开`weights.txt`并在对应的位置写上权值(e.g. `10,2131,0`)
3. 保存文件，`python3 dinner.py`

---

initiated on 20210110, four days before **高数期末考**