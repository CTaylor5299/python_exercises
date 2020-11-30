maths = int(input('Enter score: '))
chemistry = int(input('Enter score: '))
physics = int(input('Enter score: '))


total = (maths + chemistry + physics)

def calc_average(total):
    return total / 3

def determine_score(grade):
    if 70 <= grade <= 100:
        return 'A'
    elif 60 <= grade <= 69:
        return 'B'
    elif 50 <= grade <= 59:
        return 'C'
    elif 40 <= grade <= 49:
        return 'D'
    else:
        return 'F'


grade = total
avg = calc_average(total)
abc_grade = determine_score(grade)

print("That's a(n): " + str(abc_grade))
print('Average grade is: ' + str(avg))