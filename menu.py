import functions

def menu():
    grades = []

    while True:
        print("\n----- MENU -----")
        print("1. Check pass/fail status")
        print("2. Enter list of grades")
        print("3. Calculate average")
        print("4. Count grades above a specific value")
        print("5. Verify and count a specific grade")
        print("6. Exit")

        option = input("Choose an option (1-6): ")

        if option == "1":
            functions.enter_grades()
        elif option == "2":
            grades = functions.check_pass_status()
        elif option == "3":
            functions.calculate_average(grades)
        elif option == "4":
            functions.count_above(grades)
        elif option == "5":
            functions.verify_and_count_specific(grades)
        elif option == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()