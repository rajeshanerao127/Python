marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

ascending = dict(sorted(marks.items(), key=lambda item: item[1]))
descending = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order:", ascending)
print("Descending Order:", descending)