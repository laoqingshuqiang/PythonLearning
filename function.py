# 导入模块
import random
import math

# 变量定义（基本数据类型）
name = "小明"  # 字符串
age = 20       # 整数
height = 1.75  # 浮点数
is_student = True  # 布尔值
hobbies = ["读书", "运动", "编程"]  # 列表
scores = {"数学": 95, "语文": 88}  # 字典

# 函数定义
def greet(person_name):
    return f"你好，{person_name}！"

# 条件语句
def check_age(age):
    if age >= 18:
        print("你已成年！")
    elif age > 0:
        print("你还未成年。")
    else:
        print("年龄输入有误！")

# 循环语句
def print_hobbies(hobby_list):
    print("你的爱好有：")
    for hobby in hobby_list:  # for 循环遍历列表
        print(f"- {hobby}")
    # while 循环示例
    count = 0
    while count < 3:
        print(f"第 {count+1} 次循环")
        count += 1

# 面向对象编程 - 定义一个类
class Student:
    # 构造函数
    def __init__(self, name, age):
        self.name = name  # 实例变量
        self.age = age
        self.grades = []  # 空列表，用于存储成绩

    # 实例方法
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"已添加成绩：{grade}")
        else:
            raise ValueError("成绩必须在 0-100 之间！")

    # 计算平均分
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# 异常处理
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} 除以 {b} = {result}")
    except ZeroDivisionError:
        print("错误：除数不能为 0！")
    except TypeError:
        print("错误：输入类型无效！")
    finally:
        print("计算结束。")

# 主程序
if __name__ == "__main__":
    # 基本输出
    print(greet(name))
    check_age(age)

    # 列表操作
    print_hobbies(hobbies)
    hobbies.append("音乐")  # 添加元素
    print(f"更新后的爱好：{hobbies}")

    # 字典操作
    print("成绩单：")
    for subject, score in scores.items():  # 遍历字典
        print(f"{subject}: {score}")

    # 面向对象示例
    student = Student("小红", 19)
    student.add_grade(85)
    student.add_grade(92)
    print(f"{student.name} 的平均分：{student.get_average()}")

    # 异常处理示例
    divide_numbers(10, 2)
    divide_numbers(10, 0)  # 触发除零错误

    # 使用导入的模块
    random_num = random.randint(1, 10)  # 随机数
    print(f"随机数：{random_num}")
    print(f"π 的值：{math.pi}")  # 使用 math 模块
    print(f"2 的平方根：{math.sqrt(2)}")

    # 列表推导式（简洁语法）
    squares = [x**2 for x in range(5)]
    print(f"0-4 的平方：{squares}")