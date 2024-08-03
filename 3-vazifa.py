#Ne'matullayeva Sevara 3-vazifa
file=open("homework.txt","r", encoding="utf-8")
information=[]
lines=file.readlines()
for line in lines:
    info=line.strip().split(",")
    change=info[3].replace("$","")
    info1={
        "num":info[0],
        "code":info[1],
        "product":info[2],
        "price":float(change),
        "availability":info[4]
    }
    information.append(info1)

filtered=list(filter(lambda info: info["availability"] == "false" and info["price"]<1000,information ))
filtered.sort(key=lambda info:info["price"],reverse=False)
for info1 in filtered:
    print(f"{info1["num"]},{info1["code"]},{info1["product"]},{info1["price"]},{info1["availability"]}\n")
file.close()