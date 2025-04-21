import numpy as np

# 给定的列表
list1 = [5, 6, 3, 12, 41, 25, 33, 51, 16]
list2 = [5, 6, 8, 10, 15, 3, 25, 29, 66]

# 生成3x3矩阵A和B
A = np.array(list1).reshape(3, 3)
B = np.array(list2).reshape(3, 3)

# 输出矩阵A和B
print("矩阵A:")
print(A)
print("\n矩阵B:")
print(B)

# 求A的转置并输出
A_transpose = np.transpose(A)
print("\n矩阵A的转置:")
print(A_transpose)

# 求A的逆并输出
A_inv = np.linalg.inv(A)
print("\n矩阵A的逆:")
print(A_inv)

# 求矩阵A的行列式并输出
A_det = np.linalg.det(A)
print("\n矩阵A的行列式:")
print(A_det)

# 求矩阵A和B的乘积并输出
A_times_B = np.dot(A, B)
print("\n矩阵A和B的乘积:")
print(A_times_B)