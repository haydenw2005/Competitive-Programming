import os
import sys

def create_problem(week, problem_name):
    week_dir = f"week{week}"
    problem_dir = f"{week_dir}/{problem_name}"
    test_cases_dir = f"{problem_dir}/test_cases"

    os.makedirs(problem_dir, exist_ok=True)
    os.makedirs(test_cases_dir, exist_ok=True)

    with open(f"{problem_dir}/{problem_name}.py", "w") as f:
        f.write("#Author: Hayden White\n#It is ok to share my code anonymously for educational purposes\n#! /usr/bin/python3\n")

    with open(f"{test_cases_dir}/input1.txt", "w") as f:
        f.write("")

    with open(f"{test_cases_dir}/output1.txt", "w") as f:
        f.write("")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        week = int(sys.argv[1])
        problem_name = sys.argv[2]
        create_problem(week, problem_name)
    else:
        week = input("What week? ")
        problem_name = input("What is the name of the problem? ")
        create_problem(int(week), problem_name)