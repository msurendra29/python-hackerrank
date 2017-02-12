n = int(input())
data = {}
for _ in range(n):
    marks = {}
    student_data = []
    student_data = input().strip().split(' ')
    name = student_data.pop(0)
    marks["maths"] = float(student_data.pop(0))
    marks["physics"] = float(student_data.pop(0))
    marks["chemistry"] = float(student_data.pop(0))
    data["{}".format(name)] = marks
get_marks_of_student = input().strip()
avg = float((data["{}".format(get_marks_of_student)]["maths"] + data["{}".format(get_marks_of_student)]["physics"] + data["{}".format(get_marks_of_student)]["chemistry"])/3)
print("{0:.2f}".format(avg))
print("length = ",len(data))


    
    
