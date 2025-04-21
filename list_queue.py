class List_Queue:
    def __init__(self, initial_list=[]):
        self.list = initial_list

    def add(self, item):
        """在队列最后位置添加一个元素"""
        self.list.append(item)

    def delete(self):
        """删除队列第一个元素，若队列为空则抛出异常"""
        if not self.list:
            raise Exception("队列为空，队列删除出现错误")
        return self.list.pop(0)

    def length(self):
        """返回队列长度"""
        return len(self.list)

try:
    # 创建一个List_Queue对象，初始列表参数自定义
    queue = List_Queue([1, 2, 3])

    # 测试add方法
    queue.add(4)
    print("添加元素后队列：", queue.list)

    # 测试length方法
    print("队列长度：", queue.length())

    # 测试delete方法
    print("删除元素：", queue.delete())
    print("删除元素后队列：", queue.list)

    # 再次测试delete方法，此时队列为空，应抛出异常
    queue.delete()
except Exception as e:
    # 捕获并打印异常信息
    print("出现异常：", e)