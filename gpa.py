
def grading_by_letter():
    grade_point_average = 0
    letter = user_input_letter_grade()
    number = user_input_number_grade()
    if letter == 'A':
        grade_point_average = 4.0
        print("G.P.A =", grade_point_average, " with a Score of ", number)
    elif letter == 'B':
        grade_point_average = 3.0
        print("G.P.A =", grade_point_average, "with a Score of ", number)
    elif letter == 'C':
        grade_point_average = 2.0
        print("G.P.A =", grade_point_average, "with a Score of ", number)
    elif letter == 'D':
        grade_point_average = 1.0
        print("G.P.A =", grade_point_average, "with a Score of ", number)
    else:
        grade_point_average = 0
        print("G.P.A =", grade_point_average, "with a Score of ", number)


def grading_by_points():
    number = user_input_number_grade()
    if 4.9 >= number <= 4.0:
        print("G.P.A = A")
        exit()
    elif 3.9 > number <= 3.0:
        print("G.P.A = B")
        exit()
    elif 2.9 > number <= 2.0:
        print("G.P.A = C")
        exit()
    elif 1.9 > number <= 1:
        print("G.P.A = D")
        exit()
    elif 0.9 > number <= 0.1:
        print("G.P.A = F with a Score of ", number)
        exit()


def user_input_letter_grade():
    letter = choose()
    print(letter)
    try:
        letter_grade = str(input("Enter the Letter Grade: "))
        if letter_grade == 'A' or letter_grade == 'B' or letter_grade == 'C' or letter_grade == 'D' \
                or letter_grade == 'F':
            return letter_grade
        else:
            print("Invalid Letter Grade Entry")
            user_input_letter_grade()
    except ValueError:
        print("Unacceptable Input")


def user_input_number_grade():
    num = choose()
    if num == 'Number':
        try:
            number_grade = float(input("Enter the Number Grade: "))
            if 5 > number_grade < 0:
                return number_grade
            else:
                print("Invalid Entry Try Again")
                user_input_number_grade()
        except ValueError:
            print("Unacceptable Input")
            user_input_number_grade()
    else:
        user_input_letter_grade()


def choose():
    choice = str(input("Enter Your Choice: 'Letter' or 'Number': "))
    if choice == 'Number':
        return choice
    elif choice == 'Letter':
        return choice
    else:
        print('Invalid Entry: ')
        return


grading_by_points()
grading_by_letter()
