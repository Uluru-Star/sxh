from datetime import datetime

class Person:
    def __init__(self, name, gender, id_number, birth_date):
        self.name = name            # 姓名
        self.gender = gender        # 性别
        self.id_number = id_number  # 身份证号
        self.birth_date = birth_date  # 出生年月

    def get_age(self):
        """计算年龄"""
        birth_year = int(self.birth_date.split('-')[0])
        current_year = datetime.now().year
        return current_year - birth_year

    def display_info(self):
        """显示人员基本信息"""
        return f"""个人基本信息：
姓名: {self.name}
性别: {self.gender}
身份证号: {self.id_number}
出生年月: {self.birth_date}
年龄: {self.get_age()}岁"""

class Student(Person):
    def __init__(self, name, gender, id_number, birth_date, student_id, scores=None):
        super().__init__(name, gender, id_number, birth_date)
        self.student_id = student_id    # 学号
        self.scores = scores or {}      # 成绩字典

    def add_score(self, subject, score):
        """添加或更新某门课程成绩"""
        self.scores[subject] = score

    def get_average_score(self):
        """计算平均成绩"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def display_info(self):
        """显示学生信息"""
        basic_info = super().display_info()
        scores_info = "\n".join([f"{subject}: {score}" for subject, score in self.scores.items()])
        return f"""{basic_info}
学号: {self.student_id}
课程成绩：
{scores_info}
平均成绩: {self.get_average_score():.1f}"""

class Teacher(Person):
    def __init__(self, name, gender, id_number, birth_date, title, department):
        super().__init__(name, gender, id_number, birth_date)
        self.title = title          # 职称
        self.department = department # 所属部门

    def display_info(self):
        """显示教师信息"""
        basic_info = super().display_info()
        return f"""{basic_info}
职称: {self.title}
所属部门: {self.department}"""

class Stu_teach(Student, Teacher):
    def __init__(self, name, gender, id_number, birth_date, 
                 student_id, title, department, research_topic):
        Person.__init__(self, name, gender, id_number, birth_date)
        self.student_id = student_id    # 学号
        self.title = title             # 职称
        self.department = department    # 所属部门
        self.research_topic = research_topic  # 研究课题
        self.scores = {}               # 成绩字典

    def display_info(self):
        """显示在职教师学生信息"""
        return f"""在职教师学生信息：
姓名: {self.name}
性别: {self.gender}
身份证号: {self.id_number}
出生年月: {self.birth_date}
年龄: {self.get_age()}岁
学号: {self.student_id}
职称: {self.title}
所属部门: {self.department}
研究课题: {self.research_topic}
平均成绩: {self.get_average_score():.1f}"""

# 测试代码
if __name__ == "__main__":
    # 创建一个普通学生实例
    student = Student(
        name="张三",
        gender="男",
        id_number="110101200001015432",
        birth_date="2000-01-01",
        student_id="2023001"
    )
    student.add_score("数学", 90)
    student.add_score("英语", 85)
    student.add_score("计算机", 95)

    # 创建一个教师实例
    teacher = Teacher(
        name="李四",
        gender="女",
        id_number="110101198001015432",
        birth_date="1980-01-01",
        title="副教授",
        department="计算机科学系"
    )

    # 创建一个在职教师学生实例
    stu_teach = Stu_teach(
        name="王五",
        gender="男",
        id_number="110101199001015432",
        birth_date="1990-01-01",
        student_id="2023002",
        title="讲师",
        department="数学系",
        research_topic="人工智能在教育中的应用"
    )
    stu_teach.add_score("高等数学", 88)
    stu_teach.add_score("教育学", 92)

    # 显示所有信息
    print("1. 学生信息：")
    print(student.display_info())
    print("\n" + "="*50 + "\n")

    print("2. 教师信息：")
    print(teacher.display_info())
    print("\n" + "="*50 + "\n")

    print("3. 在职教师学生信息：")
    print(stu_teach.display_info())