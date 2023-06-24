# -----------------------------------------------------------------------------
#
# Trivial example for 'with' keyword in Python3
#
# -----------------------------------------------------------------------------

# Reading a file using 'with' statement
with open('file.txt', 'r') as f:
    contents = f.read()
    print(contents)

# The file will be automatically closed after the 'with' block
