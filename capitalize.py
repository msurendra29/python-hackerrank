s = input().strip()
for x in s.split():
    s = s.replace(x,x.capitalize())
print(s)

# my other solution is below
#print(" ".join([i.capitalize() for i in input().strip().split()]))
