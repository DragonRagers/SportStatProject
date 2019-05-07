import os

out = open("data/data.csv","w")

fileNames = []
for fileName in os.listdir("data"):
    fileNames.append(fileName)

for name in fileNames:
    f = open("data/" + name)
    for line in f:
         out.write(line)
    print("Added", name)
    f.close()
out.close()
