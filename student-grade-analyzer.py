def student_grade(*marks,n):
    total_marks=sum(marks)
    avg_marks=round(total_marks/n,2)
    highest_marks=max(marks)
    lowest_marks=min(marks)
    print('Average marks:',avg_marks)
    print('Highest marks:',highest_marks)
    print('Lowest marks:',lowest_marks)
def assign_grade(*marks):
    for i in marks:
        if i>=90:
            print('Grade A')
        elif 75 <=i<= 89:
            print('Grade B')
        elif 60<=i<=74:
            print('Grade C')
        elif 50<=i<=59:
            print('Grade D')
        else:
            print('Fail')
num=int(input('enter number of students:'))
marks=[]
for i in range(num):
    marks.append(int(input('Enter marks:')))
student_grade(n=num,*marks)
assign_grade(*marks)