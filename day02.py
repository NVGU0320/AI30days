def tempC_transform(tempC):
    tempF=tempC*9/5+32
    return tempF

def tempF_transform(tempF):
    tempC=(tempF-32)*5/9
    return tempC

def BMI(weight,height):
    bmi=weight/(height**2)
    bmi=round(bmi,1)
    if bmi<18.5:
        x="pianshou"
    elif bmi<24:
        x="zhengchang"
    elif bmi<28:
        x="chaozhong"
    else:
        x="feipang" 
    return x,bmi


x,bmi=BMI(70,1.75)
print("BMI:",bmi,"Type:",x)

"猜数字：程序随机生成 1–100，最多猜 7 次；每次提示“大了/小了”；输入非数字提示重输；猜中或次数用完结束"

def guess_number():
    import random
    number=random.randint(1,100)
    max=7
    for i in range(max):
        while True:
            guess=input("第%d次，请输入你猜的数字："%(i+1))
            try:
                guess=int(guess)
                break
            except:
                print("请重新输入数字：")
        if guess>number:
            print("大了")
        elif guess<number:
            print("小了")
        else:
            print("猜中了！")
            break
    else:
        print("次数用完，游戏结束。正确答案是：", number)



"九九乘法表：用嵌套 for 打印下三角，格式如 1*2=2，每行结束换行；加练：输入 n，打印 n 行"
def nine_multiplication_table():
    n=input("请输入一个数字：")
    try:
        n=int(n)
    except:
        print("输入错误，请输入一个数字")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("%d*%d=%d"%(j,i,i*j),end="\t")
            if i==j:
                print("\n")



"词频统计：输入一句英文，忽略大小写和 , . ! ?，统计每个单词出现次数，按次数降序输出前 5"

def word_frequency():
    text=input("请输入一句话：")
    for char in [",",".","!","?"]:
        text=text.replace(char," ")
    text=text.lower()
    words=text.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    sorted_word_count=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    for word,count in sorted_word_count[:5]:
        print(f"{word}:{count}")

"成绩统计：给定列表，输出最高分、最低分、平均分（1 位小数）、及格率（≥60）、高于平均分的人数；先用循环手写，再用 max/min/sum 对照"
def score_statistics(scores):
    max=0
    min=1000
    sum=0
    count=0
    num=0
    for score in scores:
        if score>max:
            max=score
        if score<min:
            min=score
        if score>=60:
            count+=1
        sum+=score
        average=sum/len(scores)
    for score in scores:
        if score>average:
            num+=1    
    return max,min,average,count,num     

def score_statistics_builtin(scores):
    count=0
    num=0
    max_score=max(scores)
    min_score=min(scores)
    average=sum(scores)/len(scores)
    for score in scores:
        if score>=60:
            count+=1
        if score>average:
            num+=1
    return max_score,min_score,average,count,num


"字符分类统计：输入任意字符串，统计大写字母、小写字母、数字、空格、其他字符各多少个，用 dict 保存"
def character_classification(s):
    count_dict={"upper":0,"lower":0,"digit":0,"space":0,"other":0}
    for char in s:
        if char.isupper():
            count_dict["upper"]+=1
        elif char.islower():
            count_dict["lower"]+=1
        elif char.isdigit():
            count_dict["digit"]+=1
        elif char.isspace():
            count_dict["space"]+=1
        else:
            count_dict["other"]+=1
    return count_dict

"登录验证（挑战）：预设用户名/密码，最多 3 次；为空提示重输；成功 break；3 次失败锁定"
def login_verification():
    username="admin"
    password="123456"
    max_attempts=3
    for attempt in range(max_attempts):
        input_username=input("请输入用户名：")
        input_password=input("请输入密码：")
        if input_username=="" or input_password=="":
            print("用户名或密码不能为空，请重新输入。")
            continue
        if input_username==username and input_password==password:
            print("登录成功！")
            break
        else:
            print("用户名或密码错误，请重新输入。")
    else:
        print("登录失败，账户已锁定。")


"购物车（挑战）：dict 存商品价格，循环输入商品和数量，q 结束；算总价，满 100 打 9 折，输出明细和实付"

def shopping_cart():
    products = {
        "apple": 5,
        "banana": 2,
        "orange": 3,
        "milk": 10,
        "bread": 8
    }
    cart = {}
    while True:
        item = input("请输入商品名称（或输入 'q' 结束）：")
        if item == 'q':
            break
        if item not in products:
            print("商品不存在，请重新输入。")
            continue
        quantity = input(f"请输入 {item} 的数量：")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("数量必须为正整数，请重新输入。")
                continue
        except ValueError:
            print("数量必须为整数，请重新输入。")
            continue
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

    total_price = sum(products[item] * quantity for item, quantity in cart.items())
    if total_price >= 100:
        total_price *= 0.9

    print("\n购物明细：")
    for item, quantity in cart.items():
        print(f"{item}: {quantity} x {products[item]} = {quantity * products[item]}")
    print(f"总价: {total_price:.2f}")

"简易计算器（挑战）：循环输入两个数和运算符，支持 + - * /；除零和非法运算符要提示；q 退出"
def simple_calculator():
    while True:
        num1 = input("请输入第一个数字（或输入 'q' 退出）：")
        if num1 == 'q':
            break
        num2 = input("请输入第二个数字：")
        operator = input("请输入运算符 (+, -, *, /)：")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("输入的不是有效的数字，请重新输入。")
            continue

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("除数不能为零，请重新输入。")
                continue
            result = num1 / num2
        else:
            print("非法运算符，请重新输入。")
            continue

        print(f"结果: {num1} {operator} {num2} = {result}")
simple_calculator()