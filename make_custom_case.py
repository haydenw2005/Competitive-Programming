def generate_worst_case_test_file(filename):
    n = 400000  # Maximum number of topics (4 * 10^5)
    
    with open(filename, "w") as file:
        # First line: number of topics
        file.write(f"{n}\n")
        
        # First topic has no dependencies
        file.write(f"1000000 0\n")  # Maximum time (10^6)
        
        # Each subsequent topic depends on the previous one
        for i in range(2, n + 1):
            # Maximum time (10^6) and one dependency (the previous topic)
            file.write(f"1000000 1 {i-1}\n")

# Create the worst case test file
generate_worst_case_test_file("worst_case_test.txt")