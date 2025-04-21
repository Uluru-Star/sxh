class array2:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, key):
        row, col = key
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, key, value):
        row, col = key
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of range")

    def __call__(self, row, col):
        return self.__getitem__((row, col))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# 测试代码
if __name__ == "__main__":
    # 创建一个 3x3 的二维数组
    arr = array2(3, 3)

    # 使用下标运算符设置值
    arr[0, 0] = 1
    arr[1, 1] = 5
    arr[2, 2] = 9

    # 使用下标运算符获取值
    print(f"arr[0, 0] = {arr[0, 0]}")
    print(f"arr[1, 1] = {arr[1, 1]}")
    print(f"arr[2, 2] = {arr[2, 2]}")

    # 使用函数调用运算符
    print(f"arr(0, 0) = {arr(0, 0)}")
    print(f"arr(1, 1) = {arr(1, 1)}")
    print(f"arr(2, 2) = {arr(2, 2)}")

    # 打印整个数组
    print("整个数组:")
    print(arr)

    # 测试越界访问
    try:
        arr[3, 3] = 10
    except IndexError as e:
        print(f"越界访问测试: {e}")