# Create a test case generator for the worst-case scenario
def generate_worst_case_test_file(filename):
    max_test_cases = 100
    max_price = 1_000_000  # in cents
    max_people = 100
    max_contribution = 1_000_000  # maximum contribution a person can make
    min_contribution = 1  # minimum contribution a person can make

    with open(filename, "w") as file:
        # Write the number of test cases
        file.write(f"{max_test_cases}\n")
        
        for _ in range(max_test_cases):
            # Generate worst case with max price and max number of people
            file.write(f"{max_price} {max_people}\n")
            
            # Generate contributions: alternate between the minimum and maximum contribution
            contributions = [min_contribution if i % 2 == 0 else max_contribution for i in range(max_people)]
            
            # Write contributions to file
            file.write(" ".join(map(str, contributions)) + "\n")

# Call the function to create the worst-case test file
generate_worst_case_test_file("worst_case_test.txt")
