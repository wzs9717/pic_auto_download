with open('list.jason',"r") as f:
    a=f.read()
with open('list_all.jason',"r") as f:
    c=f.read()

bb=a.split('\n')
cc=c.split('\n')

for i in bb:
    if i in cc:
        cc.remove(i)

for i in cc:
    with open('list_re.jason',"a") as f:
        f.write(i)
        f.write("\n")
# print(cc)
