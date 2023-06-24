# -----------------------------------------------------------------------------
#
# Trivial example of using exception in Python3
#
# -----------------------------------------------------------------------------

# Exception handling using 'with' statement
try:
    with open('file.txt', 'r') as f:
        content = f.read()
        # Perform some operations with the file content
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")
