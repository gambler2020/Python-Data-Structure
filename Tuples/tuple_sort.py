c={"a":10, "b":1, "c":22}
temp=list()
for k,v in c.items():
    temp.append((v, k))
    temp=sorted(temp, reverse=True)
print(temp)
