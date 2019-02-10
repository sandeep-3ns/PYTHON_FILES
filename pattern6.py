data1='ABCD'
data2='PQR'
for i in range(4):
    for j in range(4):
        if i>=j:
            print(data1[j],end='')
        else:
            print(data2[j-1],end='')
    print()