# 6. Program to create grade calculator in Python
def grade_calculator(marks):
    if marks >= 91:
        return 'Disctintion'
    elif marks >= 81:
        return 'First Class'
    elif marks >= 75:
        return 'Second Class'
    elif marks >= 50:
        return 'Third Class'
    elif marks >=35:
        return 'Pass Class'
    else:
        return 'Fail'

print('Secured Grade :- ', grade_calculator(int(input('Enter percentage secured : '))))

#Enter Marks secured : 89
# Secured Grade :-  First Class