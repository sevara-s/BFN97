file="homework.txt"
with open(file,"r") as f:
    lines=f.readlines()
    for line in lines:
        info=line.split(",")
        change=info[3].replace("$","")
        if float(change)<1000 and info[4]=="false":
            print(line)