"""
list = [1, 2, 2, 1, 1]
flag = True
start = 0
end = len(list)
while start < end:
    if list[start] != list[end - 1]:
        flag = False
        break
    start = start + 1
    end = end - 1
print(flag)

"""
# problem no.3
studentGrades = ['A', 'B', 'C', 'A', 'B', 'A', 'A']
count = 0
for i in range(len(studentGrades)):
    if studentGrades[i] == 'A':
        count = count + 1
print(count)
print(len(studentGrades))
