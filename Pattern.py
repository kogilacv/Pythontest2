#print pattern
print("the pattern required is  as follows")
for r in range(0,10):
    a=0
for column in range(0,r+1):
    print(a,end="")
    a=a+1
    #ending line
    print('\r')
# to get the control to the next line once the loop is over