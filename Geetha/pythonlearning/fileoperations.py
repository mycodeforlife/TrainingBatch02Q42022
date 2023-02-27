import sys

file_name = sys.argv[1]   #input from command line as an argument
output_file_name = sys.argv[2]
fh = open(file_name,"r")
wfh = open(output_file_name,"w")

for each_line in fh:
    # each_line = each_line.rstrip("\n")
    # print(each_line)
    wfh.write(each_line)


fh.close()
wfh.close()

