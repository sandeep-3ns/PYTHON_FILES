
"""i = 1
while i<=5:
    j=1
    while j<=5:
        print("#", end="")
        j=j+1
    i=i+1
    print()
"""

#alternate_method and better approach. using * operator
i = 1
while i<=5:
        print(5*"#")
        i=i+1