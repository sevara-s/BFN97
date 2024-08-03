file1="homework.txt"
with open(file1,"r") as f:
    lines=f.readlines()
    for line in lines:
        data=line.split(",")
        if data[4].strip()=="true":
            print(line)