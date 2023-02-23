import sys

r_file_name = sys.argv[1]
w_file_name = sys.argv[2]

rfh = open(r_file_name,"r")
wfh = open(w_file_name,"w")

for each_line in rfh:
    #each_line = each_line.rstrip("\n")
    # print(each_line)
    wfh.write(each_line)



rfh.close()
wfh.close()




