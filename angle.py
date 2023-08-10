import math

# 输入三角形的角度
angle = float(input("请输入三角形的角度（单位：度）："))

# 将角度转换为弧度
angle_rad = math.radians(angle)

# 计算正弦值
sin_value = math.sin(angle_rad)

# 计算余弦值
cos_value = math.cos(angle_rad)

# 计算正切值
tan_value = math.tan(angle_rad)

# 打印结果
print("正弦值为：", sin_value)
print("余弦值为：", cos_value)
print("正切值为：", tan_value)

