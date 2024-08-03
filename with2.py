file1 = "homework.txt"
with open(file1, "r") as f:
    lines = f.readlines()
    for line in lines:
        data = line.strip().split(",")
        change=data[3].replace("$"," ")
        if float(change) > 500 and float(change)<1000:
            print(line)
