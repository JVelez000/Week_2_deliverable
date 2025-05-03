# calculate_average
# total += grade
# Adds each grade to the total sum to later compute the average

# count_above_value
# count += 1
# Increments count when a grade is greater than the given value

# count_above_value
# i += 1
# Moves to the next grade in the list to continue comparison

# verify_and_count_specific
# count += 1
# Increments count each time the target grade is found in the list

def check_pass_status():
    while True:
        try:
            grade = float(input("Enter a grade (0&100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("The grade must be a number between 0 & 100.")
        except ValueError:
            print("Please enter a valid number.")

    if grade >= 60:
        print("Passed")
    else:
        print("Failed")

def enter_grades():
    while True:
        entry = input("Enter a list of grades separated by commas: ")
        try:
            grades = [float(x.strip()) for x in entry.split(',')]
            return grades
        except ValueError:
            print("Make sure to enter only numbers separated by commas.")

def calculate_average(grades):
    if not grades:
        print("No grades available to calculate the average.")
        return
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print(f"Average: {average:.2f}")

def count_above(grades):
    if not grades:
        print("No grades available to evaluate.")
        return
    while True:
        try:
            value = float(input("Enter a value to compare: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    count = 0
    i = 0
    while i < len(grades):
        if grades[i] > value:
            count += 1
        i += 1
    print(f"Number of grades above {value}: {count}")

def verify_and_count_specific(grades):
    if not grades:
        print("No grades available to evaluate.")
        return
    while True:
        try:
            target = float(input("Enter a specific grade to search for: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    count = 0
    for grade in grades:
        if grade != target:
            continue
        count += 1

    if count > 0:
        print(f"The grade {target} appears {count} time(s).")
    else:
        print(f"The grade {target} is not found in the list.")
