# 9번째 문제

# 모듈을 통해 설계하여라 클래스와 생성자를 필수적으로 설계하여라

class Student:

    def __init__(self, name, year, major, gpa, prof):
        self.name = name
        self.year = year
        self.major = major
        self.gpa = gpa
        self.prof = prof

    def print_student(self):
        print("학생")
        for i in range(len(name_list)):
            print("이름: {}  학년: {}  전공: {}  직전학기평균: {}  지도교수: {}".format(name_list[i],year_list[i],major_list[i],gpa_list[i],prof_list[i]))

class Professor(Student):

    def __init__(self, prof_name, lab, student_num):
        self.prof_name = prof_name
        self.lab = lab
        self.student_num = student_num


    def print_professor(self):
        print("교수")
        for i in range(len(prof_name_list)):
            print("이름: {}  연구실: {}  지도학생수: {}".format(prof_name_list[i],lab_list[i],student_num[i]))


name_list = ["김철수","이영희","박보람","박찬이","오하영","조인수","최강","무명"]
year_list = ["3","2","1","4","2","3","1","-1"]
major_list = ["컴소공","기계시스템","경영학","신소재","물리","전자","컴공","전공없음"]
gpa_list = ["4","3.5","4.5","3.5","4","2.5","0","-1"]
prof_list = ["나교수","공석","김박사","이영재","공석","김박사","공석","공석"]
prof_name_list = ["나교수","이영재","김박사","무명"]
lab_list = ["D443","G128","T335","N/A"]
student_num = ["4","2","-1","-1"]


for i in range(len(name_list)):
    student = Student(name_list[i],year_list[i],major_list[i],gpa_list[i],prof_list[i])
for i in range(len(prof_name_list)):
    professor = Professor(prof_name_list[i],lab_list[i],student_num[i])

student.print_student()
professor.print_professor()




