Student_info = {"R01":"Indira", "R02":"Mounika"}
print(Student_info["R02"])

Student_info["R03"]="Geetha"
Student_info["R04"]="Ramana"


print(Student_info)

list_of_roll_num=Student_info.keys()
for roll_num in list_of_roll_num:
    print(roll_num, Student_info[roll_num])



