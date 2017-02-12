def second_min(t):
    temp_list = []
    for i in t:
        if ((i in set(t)) and (i not in temp_list)):
            temp_list.append(i)

    temp_list.sort()
    return temp_list[1]
# ========================================================

students = []
temp = []
n = int(input())
for i in range(0,n):
    name = input().strip()
    grade = float(input())
    temp.append(name)
    temp.append(grade)
    students.append(temp)
    temp = []
#print(students)
y = 0
score_list = []
for i in students:
    score_list.append(students[y][1])
    y = y+1
second_min_score = second_min(score_list)
#print(second_min_score)
names = []
for i in students:
    if(second_min_score == i[1]):
        names.append(i[0])
names.sort()
for i in names:
    print(i)

        
    
    

