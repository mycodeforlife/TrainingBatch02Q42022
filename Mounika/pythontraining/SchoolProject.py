class Staff:

    FirstName = ""
    LastName = ""
    ContactDetails = {}
    Staff_ID = ""
    Staff_Type = ""
    Student_List = []

    def __init__(self, staff_type, f_name, l_name):
        self.FirstName = f_name
        self.LastName = l_name
        self.Staff_Type = staff_type

    def set_contact_information(self):
        pass

    def set_additional_staff_details(self):
        pass

    def set_class_room_to_teacher(self):
        if self.Staff_Type == "Teacher":
            pass
        else:
            print("Sorry,Cant assign classroom to Non staff members")

    def set_student_association(self, student_name_list):
        self.Student_List = student_name_list

    def get_student_names(self):
        return self.Student_List


class StudentDetails:

    name = ""
    student_id = ""
    marks = {}
    Class_Teacher_Name = ""

    def __init__(self, first_name, last_name):
        self.name = first_name+" "+last_name
        # self.student_id = roll_num

    # Function to create and append a student
    def set_student_grades(self, enrolled_subject, subject_marks):
        self.marks[enrolled_subject] = subject_marks

    def get_student_id(self):
        return self.student_id

    def get_student_name(self):
        return self.name

    def set_class_teacher(self, teacher_name):
        self.Class_Teacher_Name = teacher_name

    def get_class_teacher_name(self):
        return self.Class_Teacher_Name
