class Building:
    def __init__(self, building_id, floors, total_area):
        self.building_id = building_id  # 建筑物编号
        self.floors = floors           # 层数
        self.total_area = total_area   # 总面积

    def display_info(self):
        """显示建筑物基本信息"""
        return f"建筑编号: {self.building_id}\n层数: {self.floors}\n总面积: {self.total_area}平方米"

class TeachBuilding(Building):
    def __init__(self, building_id, floors, total_area, classroom_count):
        super().__init__(building_id, floors, total_area)
        self.classroom_count = classroom_count  # 教室数

    def display_info(self):
        """显示教学楼信息"""
        basic_info = super().display_info()
        return f"教学楼信息：\n{basic_info}\n教室数: {self.classroom_count}"

    def get_avg_classroom_per_floor(self):
        """计算每层平均教室数"""
        return self.classroom_count / self.floors

class DormBuilding(Building):
    def __init__(self, building_id, floors, total_area, dorm_count, student_capacity):
        super().__init__(building_id, floors, total_area)
        self.dorm_count = dorm_count          # 宿舍数
        self.student_capacity = student_capacity  # 容纳学生总人数

    def display_info(self):
        """显示宿舍楼信息"""
        basic_info = super().display_info()
        return f"宿舍楼信息：\n{basic_info}\n宿舍数: {self.dorm_count}\n可容纳学生数: {self.student_capacity}"

    def get_avg_students_per_dorm(self):
        """计算每个宿舍平均容纳学生数"""
        return self.student_capacity / self.dorm_count

# 测试代码
if __name__ == "__main__":
    # 创建一个教学楼实例
    teach_building = TeachBuilding(
        building_id="T101",
        floors=5,
        total_area=3000,
        classroom_count=30
    )

    # 创建一个宿舍楼实例
    dorm_building = DormBuilding(
        building_id="D201",
        floors=6,
        total_area=4000,
        dorm_count=120,
        student_capacity=480
    )

    # 显示教学楼信息
    print(teach_building.display_info())
    print(f"每层平均教室数: {teach_building.get_avg_classroom_per_floor():.1f}")
    
    print("\n" + "="*50 + "\n")  # 分隔线
    
    # 显示宿舍楼信息
    print(dorm_building.display_info())
    print(f"每个宿舍平均人数: {dorm_building.get_avg_students_per_dorm():.1f}")