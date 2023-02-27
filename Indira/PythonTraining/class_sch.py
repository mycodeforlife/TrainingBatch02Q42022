
class Staff:
    FirstName = ""
    LastName = ""
    ContactDetails = {}
    Staff_ID = ""
    Staff_Type = ""
    student_List = []

    def __init__(self, staff_type, f_name,  l_name):
        self.FirstName = f_name
        self.LastName = l_name
        self.Staff_Type = staff_type

    def set_contact_information(self):
         pass

    def set_additional_staff_details(self):
        pass

    def set_class_room_to_teacher(self):
         if self Staff_Type == "Teacher":
           pass
      else:
          print("class room can't be assigned to non teaching staff")

    def assign_student(self,student_Name_List):
        self.student_list = student_Name_List

    def get_student_names(self):

 class Student:

     name = ""
     student_id = ""
     marks = {}
     Class_Teacher_Name =""


      def __init__(self, first_name, last_name):
       self.name = first_name , last_name
      # self.student_id = roll_no

   #fuction to create and append a student

     def set_student_grades(self, enrolled_subjects,subject_marks):
         self.marks[enrolled_subject] = subject_marks

     def set_student_details(self, name, rollno, marks1, marks2)
          input("enter student name:")




