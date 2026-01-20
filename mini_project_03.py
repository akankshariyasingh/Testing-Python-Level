'''
mini_project_03 - Student Performance and validation system
1. Extract students name 
2. convert marks string - list of integers
3. calculate average marks
4. decide grade
5. check if email is valid 
6. store final result in dictionary
7. store failed students seperately
8. store invalid emials seprately

'''
def student_performance_system(students):

    results = []
    failed_students = []
    invalid_emails = []

    for record in students:
        name, marks_str, email = record.split(",") #for multiple arguments

        marks_list = marks_str.split() #split marks and store in another variable
        marks = []

        for m in marks_list:
            marks.append(int(m)) 

        total = 0
        for m in marks:
            total += m  #adding each marks and calculate total for finding the average

        average = total / len(marks)

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

        student_data = { 
            "name": name,
            "marks": marks,
            "average": average,
            "grade": grade,
            "email": email
        } #for storing the record or result in the form of string

        results.append(student_data)

    return results, failed_students, invalid_emails #for returning all the parameters 

    

students=[ "Akanksha,78 85 90,akanksha@gmail.com",
    "Ravi,45 60 55,ravigmail.com",
    "Neha,30 35 40,neha@gmail.com"]
print(student_performance_system(students))




