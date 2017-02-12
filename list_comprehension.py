l = []
x = int(input())
y = int(input())
z = int(input())
n = int(input())

for i1 in range(0,x+1):
    for i2 in range(0,y+1):
        for i3 in range(0,z+1):
            sum = i1 + i2 + i3
            if(sum != n):
                temp_list = [i1,i2,i3]
                l.append(temp_list)
print(l)
                
