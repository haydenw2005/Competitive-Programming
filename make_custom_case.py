import random

def generate_custom_test_file(filename):
    with open(filename, "w") as file:
        # First line: Always 100
        file.write("100\n")
        
        # Second line: 100 values, 1 <= k <= 1000
        second_line = [str(random.randint(1, 1000)) for _ in range(100)]
        file.write(" ".join(second_line) + "\n")
        
        # Third line: 1 <= m <= 1000
        m = random.randint(1, 1000)
        file.write(f"{m}\n")
        
        # Fourth line: m values, 1 <= l <= 30,000
        fourth_line = [str(random.randint(1, 30000)) for _ in range(m)]
        file.write(" ".join(fourth_line) + "\n")

# Call the function to create the custom test file
generate_custom_test_file("custom_test.txt")