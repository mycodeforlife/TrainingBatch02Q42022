def students_info(details):
        print("student" + " ", details)


students_info("ID")
students_info("Name")
students_info("Class Details")
students_info("Parents Details")
students_info("Address")


def myname(fname, lname):
  print(fname + " " + lname)


myname("Emil" ,"None")


def family_tree(*kids):
  print("My Youngest Child is  " + kids[3] + " and" + kids[4])


family_tree("rani", "swaroopa", "Anil", "Sai","sais")


def life(food):
        for x in food:
                print(x)
 fruits = ["apple","orange","banana"]



life(fruits)