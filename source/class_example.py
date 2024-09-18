class Student:

    def __init__(self, name, kor, math, eng):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

    def get_sum(self):
        return self.kor + self.math + self.eng

    def get_average(self):
        return self.get_sum() / 3

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, \
                                   self.get_sum(), \
                                   self.get_average())


student_a = Student("KJM", 95, 100, 95)
student_b = Student("KNK", 90, 90, 100)

print(student_a.to_string())
print("{}, {} {} {}".format(student_b.name,student_b.kor, student_b.math, student_b.eng))