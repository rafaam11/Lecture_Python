class Student:

    def __init__(self, name, kor, math, eng):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.average = (kor + math + eng) / 3


    def input_student(self):
        name_list.append(self.name)
        kor_list.append(self.kor)
        math_list.append(self.math)
        eng_list.append(self.eng)
        avg_list.append(self.average)

    def delete_student(self,Delete_name):
        if Delete_name in name_list:
            list_index=name_list.index(Delete_name)
            del name_list[list_index]
            del kor_list[list_index]
            del math_list[list_index]
            del eng_list[list_index]
            del avg_list[list_index]


    def print_student(self):
        for count in range(len(name_list)):
            print("{} : {}, {}, {} = {:.4}".format(name_list[count], kor_list[count], math_list[count], eng_list[count], avg_list[count]))


name_list = []
kor_list = []
math_list = []
eng_list = []
avg_list = []


while True:
    Question = input("Menu 1.Input, 2.Delete, 3.Print, 4.Exit ? ")

    if Question == '1' :

        a,b,c,d = input("Student(Name,Kor,Math,Eng) ? ").split(",")
        b = int(b)
        c = int(c)
        d = int(d)
        student = Student(a,b,c,d)
        student.input_student()


    if Question == '2' :
        Delete_name = input("Student(Name) ? ")
        student.delete_student(Delete_name)


    if Question == '3' :
        student.print_student()


    if Question == '4' :
        break




