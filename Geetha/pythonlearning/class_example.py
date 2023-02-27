class Student:
    marks = []
    def getData(self, rn, name, m1, m2, m3):
        Student.rn = rn
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)

    def displayData(self):
        print("Roll Number is: ", Student.rn)
        print("Name is:", Student.name)
        print("Marks in subject 1:", Student.marks[0])
        print("Marks in subject 2:", Student.marks[1])
        print("Marks in subject 3:", Student.marks[2])
        print("Marks are:", Student.marks)
        print("total marks are:", self.total())

    def total(self):
        return(Student.marks[0] + Student.marks[1] + Student.marks[2])


r = int(input("enter the roll number: "))
name = input("enter the name: ")
m1 = int(input("enter the marks 1st subject: "))
m2 = int(input("enter the marks of 2nd subject: "))
m3 = int(input("enter the marks of 3rd subject: "))

s1 =  Student()
s1.getData(r, name, m1, m2, m3)
s1.displayData()





