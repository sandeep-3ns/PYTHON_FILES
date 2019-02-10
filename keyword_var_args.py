def student(name,**data):
    print(name)
    for i,j in data.items() : #items() gives key-value pair
        print(i,j)
student('sandeep',age=22,city='knr',mob=12345)
student('vijay',age=37,city='hyd',mob=54321)