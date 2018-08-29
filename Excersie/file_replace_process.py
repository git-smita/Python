mountList = open("mount.txt", "r").readlines()
print mountList
newmountList = open("newmount.txt","r").readlines()
outputList = [item for item in mountList if "filer" not in item.lower()]
outputList.extend(newmountList)
f = open("mount.txt","w")
f.write(''.join(outputList))
f.close()
