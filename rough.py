manfest=[('ram',65),('syamn',90),('hari',87),('usual',78)]
for name,weight in manfest:
    if weight>70:
        print(name)

    ##
cargo=[('ram',67),('ali',98),('usual',78),('jeevan',32)]
weight=0
item=[]
for operation in cargo:
    if weight>90:
        break
    else:
        item.append(operation[0])
        weight += operation[1]
print(item)