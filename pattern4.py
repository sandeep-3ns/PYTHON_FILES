# for i in range(5):
#     for j in range(i+1):
#         print("#",end='')
#     print()

for i in range(5):
    for j in range(0,5-i): #for j in range(5-i) also works
        print("@",end='')
    print()