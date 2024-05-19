# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2002472
#Student ID: w2002472
#Date: 16/04/2023

# THIS PROGRAM HAS THE PARTS 4

def get_student_id():
    while True:
        student_id = input('Enter Student ID: ').strip().lower()
        if not (student_id.startswith('w') and len(student_id) == 8 and student_id[1:].isnumeric()):
            print('Invalid Student ID')
        else:
            return student_id


def get_credits(txt):
    while True:
        credits_input = input(f"Please enter the {txt} credits: ").strip()
        try:
            credits = int(credits_input)
            if credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Credits out of range")
            else:
                return credits
        except ValueError:
            print("Integer required")


def calculate_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits
    if pass_credits == 120:
        outcome = "Progress"
        details = f"Progress - {pass_credits}, {defer_credits}, {fail_credits}"
    elif pass_credits == 100:
        outcome = "Progress (module trailer)"
        details = f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}"
    elif pass_credits + defer_credits >= fail_credits:
        outcome = "Module retriever"
        details = f"Module retriever - {pass_credits}, {defer_credits}, {fail_credits}"
    else:
        outcome = "Exclude"
        details = f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}"
    return outcome, details


def print_outcomes(outcomes_dict):
    for student_id, details in outcomes_dict.items():
        print(f"{student_id}: {details}")


def main():
    outcomes_dict = {}
    while True:
        student_id = get_student_id()
        pass_credits = get_credits("pass")
        defer_credits = get_credits("defer")
        fail_credits = get_credits("fail")

        # Check that the total credits add up to 120
        if pass_credits + defer_credits + fail_credits != 120:
            print("Total credits incorrect")
            continue

        # Calculate the student outcome based on credit scores
        outcome, details = calculate_outcome(pass_credits, defer_credits, fail_credits)

        # Add the student outcome to the dictionary
        outcomes_dict[student_id] = details

        print(outcome)

        # Ask the user if they want to enter another set of data or quit and view results
        while True:
            yq = input("Would you like to enter another set of data? (y/q)").strip().lower()
            if yq == 'q':
                print('Part 4:')
                print_outcomes(outcomes_dict)
                return
            elif yq == 'y':
                break
            else:
                print('Invalid Input')

if __name__ == "__main__":
    main()