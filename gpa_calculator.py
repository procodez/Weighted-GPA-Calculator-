print("For classes put grade")
print("Type r for regular, h for honors, a for AP or dual-credit")
grades = []
def gpacreator(coursegrade, courseweight):
    if coursegrade >= 97:
        gpa = 4
    if 92 >= coursegrade >= 90:
        gpa = 3.7
    if 89 >= coursegrade >= 87:
        gpa = 3.3
    if 86 >= coursegrade >= 83:
        gpa = 3
    if 82 >= coursegrade >= 80:
        gpa = 2.7
    if 79 >= coursegrade >= 77:
        gpa = 2.3
    if 76 >= coursegrade >= 73:
        gpa = 2
    if 72 >= coursegrade >= 70:
        gpa = 1.7
    if 69 >= coursegrade >= 67:
        gpa = 1.3
    if 66 >= coursegrade >= 65:
        gpa = 1
    if coursegrade < 65:
        gpa = 0
    if courseweight == "h":
        gpa = gpa + 0.5
    if courseweight == "a":
        gpa = gpa + 1
    grades.append(gpa)
    print(str(gpa) + " GPA")

first = float(input("1st Class: "))
firstw = input("Type of course (r, h, or a): ")
gpacreator(first, firstw)
second = float(input("2nd Class: "))
secondw = input("Type of course (r, h, or a): ")
gpacreator(second, secondw)
third = float(input("3rd Class: "))
thirdw = input("Type of course (r, h, or a): ")
gpacreator(third, thirdw)
fourth = float(input("4th Class: "))
fourthw = input("Type of course (r, h, or a): ")
gpacreator(fourth, fourthw)
fifth = float(input("5th Class: "))
fifthw = input("Type of course (r, h, or a): ")
gpacreator(fifth, fifthw)
sixth = float(input("6th Class: "))
sixthw = input("Type of course (r, h, or a): ")
gpacreator(sixth, sixthw)
seventh = float(input("7th Class: "))
seventhw = input("Type of course (r, h, or a): ")
gpacreator(seventh, seventhw)
eighth = float(input("8th Class: "))
eighthw = input("Type of course (r, h, or a): ")
gpacreator(eighth, eighthw)
print("Your cumulative weighted GPA is " + str(sum(grades)/8))
