# Write data to a file
with open("example.txt", "w") as file:
    file.write("This is some sample text written to the file.")
print("Data written to the file.")


# Append content to a file
with open("example.txt", "a") as file:
    file.write("\nThis is additional text appended to the file.")
print("Content appended to the file.")


# Copy contents from one file to another
with open("example.txt", "r") as source_file:
    with open("copy_example.txt", "w") as destination_file:
        for line in source_file:
            destination_file.write(line)
print("Contents copied to another file.")


# Read contents of the file using readline() method
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")  # Prints each line without adding extra newlines
        line = file.readline()
