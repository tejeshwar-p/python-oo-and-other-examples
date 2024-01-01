marks = [12, 23, 34, 45, 56, 67, 78, 89, 99, 1, 2, 3, 4, 9, 6, 0]
print(sum(marks))
print(max(marks))
print(len(marks))
marks.append(101)
print(marks)
marks.insert(2, 60)
print(marks)
marks.remove(60)
print(marks)
print(55 in marks)
print(67 in marks)
print(marks.index(99))
# Below line will throw error because 7 is not in the list - ValueError: 7 is not in list
# print(marks.index(7))
for mark in marks:
    print(mark)

