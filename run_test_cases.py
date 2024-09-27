import os
import sys
import subprocess

import os
import sys
import subprocess
import time

# My custom test suite!

def run_test_cases(problem_week, problem_name):
    test_cases_dir = f"week{problem_week}/{problem_name}/test_cases"
    solution_file = f"week{problem_week}/{problem_name}/{problem_name}.py"
    total_failed = 0

    # Run test cases with input/output files
    for input_file in os.listdir(test_cases_dir):
        if input_file.startswith("input"):
            output_file = input_file.replace("input", "output")
            with open(f"{test_cases_dir}/{input_file}", "r") as f:
                input_data = f.read()

            with open(f"{test_cases_dir}/{output_file}", "r") as f:
                expected_output = f.read()

            start_time = time.time()
            process = subprocess.Popen(["python3", solution_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            output, _ = process.communicate(input_data.encode())
            end_time = time.time()
            execution_time = end_time - start_time

            print(f"Test case {input_file} execution time: {execution_time:.4f} seconds ⏰")

            if output.decode().strip() != expected_output.strip():
                print(f" Test case {input_file} failed :( \n")
                print(f"Expected output: \n{expected_output}\n")
                print(f"Actual output: \n{output.decode()}")
                total_failed += 1
                

    # Run test case with sample.in/sample.out files
    sample_input_file = f"{test_cases_dir}/sample.in"
    sample_output_file = f"{test_cases_dir}/sample.ans"

    if os.path.exists(sample_input_file) and os.path.exists(sample_output_file):
        with open(sample_input_file, "r") as f:
            input_data = f.read()

        with open(sample_output_file, "r") as f:
            expected_output = f.read()

        start_time = time.time()
        process = subprocess.Popen(["python3", solution_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, _ = process.communicate(input_data.encode())
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Test case sample.in execution time: {execution_time:.4f} seconds")

        if output.decode().strip() != expected_output.strip():
            print(f"Test case sample.in failed :( \n")
            print(f"Expected output: \n{expected_output}\n")
            print(f"Actual output: \n{output.decode()}")
            # return False
   
    
    if not total_failed:
        print("All test cases passed! ✅")
    else:
        print(f"{total_failed} test cases failed ❌")
    return True

if __name__ == "__main__":
    print()
    if len(sys.argv) != 3:
        print("Usage: python run_test_cases.py <problem_week> <problem_name>")
        sys.exit(1)

    problem_week = sys.argv[1]
    problem_name = sys.argv[2]

    run_test_cases(problem_week, problem_name)
    print()