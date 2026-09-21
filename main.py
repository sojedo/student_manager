students = [ 
        {
    "name": "sam",
    "scores":{ 
    "math": 56,
    "science": 65,
    "english": 87,
    "religion": 45
    },
    "attendance":{
    "monday": "absent",
    "tuesday": "present",
    "wednesday": "absent",
    "thursday": "present",
    "friday": "absent"
    }
}
]
students.append( {"name": "maria", "scores": { "math": 34, "science": 76, "english": 85,"religion": 54}, "attendance": {"monday": "absent", "tuesday": "present", "wednesday": "present", "thursday": "present", "friday": "absent"}}
)
for student in students:
    average = sum(student["scores"].values()) / len(student["scores"].values())    
    if average >= 45:
        print(student["name"], average, "pass")
    else:
        print(student["name"], average, "fail")

highest_student = students[0]

for student in students:
    student_average = sum(student["scores"].values()) / len(student["scores"].values())
    highest_average = sum(highest_student["scores"].values()) / len(highest_student["scores"].values())
    if student_average > highest_average:
        highest_student = student
        print(highest_student["name"])

lowest_student = students[0]

for student in students:
    student_average = sum(student["scores"].values()) / len(student["scores"].values())
    lowest_average = sum(lowest_student["scores"].values()) / len(lowest_student["scores"].values())
    if student_average < lowest_average:
        lowest_student = student
        print(lowest_student["name"])

for pass_number in range(len(students)-1):
    for i in range(len(students)-1):
        first_average = sum(students[i]["scores"].values()) / len(students[i]["scores"].values())
        second_average = sum(students[i + 1]["scores"].values()) / len(students[i + 1]["scores"].values())

    if first_average > second_average:
            temp = students[i]
            students[i] = students[1+i]
            students[1+i] = temp
print(students[0])
print(students[1])

found = False

for student in students:
    if student["name"] == "maria":
        print(student["name"])
        found = True
    if found == False:
        print("not found")

passing_student = []

for student in students:
    average = sum(student["scores"].values()) / len(student["scores"].values())
    if average >= 45:
        passing_student.append(student)
        print(passing_student)

import json
students_json = json.dumps(students)
file = open("students.json", "w")
file.write(students_json)
file.close()

file = open("students.json", "r")
loaded_students = json.load(file)
file.close()
print(loaded_students)
print(type(loaded_students))

valid = False
while valid == False:
    try:
        score = input("Enter your score:")
        score = int(score)
        print("converted successfully")
        valid = True
    except:
        print("wrong input")

file = open("api_key.txt", "r")
api_key = file.read()
file.close()
print(api_key)
        

import anthropic
client = anthropic.Anthropic(api_key=api_key)
student_text = json.dumps(students[0])

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Write a short performance summary for this student: " + student_text}
    ]
)
print(response.content[0].text)