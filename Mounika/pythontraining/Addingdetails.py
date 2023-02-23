from SchoolProject import *

staff_member_1 = Staff("Teacher", "John", "Smith")
student_1 = StudentDetails("Ramana", "Venkata")
student_2 = StudentDetails("Monika", "Pottumuthu")
student_3 = StudentDetails("Geetha", "Rellala")
student_4 = StudentDetails("Indira", "Vadlamudi")

list_of_student_names = [student_1, student_4, student_3, student_2]

staff_member_1.set_student_association(list_of_student_names)
for each_name in staff_member_1.get_student_names():
    print(each_name.get_student_name())