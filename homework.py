
def power(x,y):
    if y==1:
        return x
    elif y==0:
        return 1
    else:
        return x*power(x, y-1)

print(power(3,0))
print(power(3,1))      
print(power(3,2))

