# Function to read the content of a file and print it
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Contents of {file_name}:")
            print(content)
            print("\n" + "="*40 + "\n")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred while reading {file_name}: {e}")

# File paths
breast_cancer_file = 'breast-cancer.names'
abalone_file = 'abalone.names'

# Read and print the contents of the two files
read_file(breast_cancer_file)
read_file(abalone_file)
