f = open("uranai2.txt","r",encoding="utf=8")

# print(line1.strip())
# print(line2.strip())
for i in f:
     line = i.strip()
     info = line.split(",")
     print(f"{info[1]}さんの運勢は{info[2]}です")
f.close()