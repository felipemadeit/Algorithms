def gradingStudents(q: int):
    
    final_grades = []
    
    for _ in range(q):
        grade = int(input())
        
        if grade < 38:
            final_grades.append(grade)
        else:
            multiple = 0 
            for i in range(grade, 101):
                if i % 5 == 0:
                    multiple = i
                    break
            if multiple - grade < 3:
                final_grades.append(multiple)
            else:
                final_grades.append(grade)
    
    for i in final_grades:
        print(i)
        
    

gradingStudents(int(input()))