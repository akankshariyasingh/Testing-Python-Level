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
    result={}
    topper=""
    higest_avg=0
    failed_student=[]
    invalid_emails=[]
    for records in students:
        name,marks_str,emails=records.split(",") #we can handle multiple arguments inside the def function.
 
        name=0
        marks_str=0
        emails=0
        marks_str=marks_str.split()

        marks=[]
        for m in marks_str:
            marks.append(int(m))
            average=sum(marks)/len(marks)
            if average>=85:
                grade="A"
            elif average>=60:
                grade="B"
            elif average>=40:
                grade="C"
            elif average<40:
                grade="Fail"
    failed_student.append(m)

print(data_analyzer(["Akanksha,78 85 90,akanksha@gmail.com","Ravi,45,60,55,ravi@gmail.com","Neha,90 95 92,nehagmail.com"]))
        
        


   
    
