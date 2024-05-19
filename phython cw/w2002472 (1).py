# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2002472
#Student ID: w2002472
#Date: 15/04/2023

# THIS PROGRAM HAS THE PARTS 1 , 2 , 3

def get_version():
    while True:
        version = input('Enter Version (student/staff): ').lower()
        if version in ['student', 'staff']:
            return version
        else:
            print('Invalid Input\n')

def get_input(txt): #for input and Validate Marks
    while True:
        try:
            x = int(input(f"Please enter your credits at {txt}: ").strip())
            if x not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range\n")
            else:
                return x
        except ValueError:
            print("Integer required\n")

def outcomes(pass_credits, defer_credits, fail_credits):
    if pass_credits == 120:
        return 'Progress', f'Progress - {pass_credits}, {defer_credits}, {fail_credits}'
    elif pass_credits == 100:
        return 'Progress (module trailer)', f'Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}'
    elif pass_credits + defer_credits >= fail_credits:
        return 'Module retriever', f'Module retriever - {pass_credits}, {defer_credits}, {fail_credits}'
    else:
        return 'Exclude', f'Exclude - {pass_credits}, {defer_credits}, {fail_credits}'

def generate_report(version):
    outcome_list = []
    progress, trailer, retriever, exclude = 0, 0, 0, 0

    while True:
        pass_credits = get_input('pass')
        defer_credits = get_input('defer')
        fail_credits = get_input('fail')

        if pass_credits + defer_credits + fail_credits != 120: #Validation
            print("Total incorrect.\n")
            continue

        outcome, outcome_str = outcomes(pass_credits, defer_credits, fail_credits)
        outcome_list.append(outcome_str)

        if outcome == 'Progress':
            progress += 1
        elif outcome == 'Progress (module trailer)':
            trailer += 1
        elif outcome == 'Module retriever':
            retriever += 1
        else:
            exclude += 1

        print(outcome, '\n')

        if version == 'staff':
            while True:
                yq = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").strip().lower()

                if yq == 'q':
                    print('-' * 50)
                    print(f"Progress {progress}\t: {'*' * progress}")
                    print(f"Trailer {trailer}\t: {'*' * trailer}")
                    print(f"Retriever {retriever}\t: {'*' * retriever}")
                    print(f"Exclude {exclude}\t: {'*' * exclude}")
                    print(f"{progress+trailer+retriever+exclude} outcomes in total.")
                    print('-' * 50)

                    out = '\n'.join(outcome_list)
                    print('Part 2:')
                    print(out)

                    with open("output.txt", "w") as f:
                        f.write(out)
                    print('\nPart 3:')
                    with open("output.txt", "r") as f:
                        print(f.read())

                    return
                elif yq == 'y':
                    break
                else:
                    print('Invalid Input\n')
        else:
            return

version = get_version()
generate_report(version)