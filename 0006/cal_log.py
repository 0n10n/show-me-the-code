import math

def log_f(f, x):
    return math.log(f(x))

# 定义一个函数作为示例
def example_function(x):
    print(f'x: {x}')
    return x**2 + 1

# 计算 log(example_function) 在 x = 2 处的值
result = log_f(example_function, 2)
print(result)
