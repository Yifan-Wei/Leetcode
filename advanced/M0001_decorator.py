from typing import List

# 装饰器
def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

# 语法糖
@debug
def say(something):
    print("hello {}!".format(something))


if __name__ == '__main__':
    say("some test")
