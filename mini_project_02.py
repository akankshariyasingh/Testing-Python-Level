'''
mini_project_02 - STUDENT DATA ANALYZER AND VALIDATOR
1. extract student name
2. convert marks into a list of integers
3. calculate avg marks
4. assign grade
5. validate email
6. store all data in a dictionary
7. find: topper, failed stu, invalid emails

'''
               
def data_analyzer(students):
    result = []
    failed_students = []
    invalid_emails = []

    for record in students:
        name, marks_str, email = record.split(",")

        marks_list = marks_str.split()   # split by space
        marks = []

        for m in marks_list:
            marks.append(int(m))         # convert to int safely

        average = sum(marks) / len(marks)

        if average >= 85:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"
            failed_students.append(name)

        if "@" not in email:
            invalid_emails.append(email)

        result.append({"name": name, "average": average,"grade": grade})
        
           

    return result, failed_students, invalid_emails


students = [
    "Akanksha,78 85 90,akanksha@gmail.com",
    "Ravi,45 60 55,ravigmail.com",
    "Neha,30 35 40,neha@gmail.com"
]

print(data_analyzer(students))