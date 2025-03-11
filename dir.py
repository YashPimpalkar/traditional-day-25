import os

# Get the current working directory
current_dir = os.getcwd()

# Output file name
output_file = "file_list.txt"

try:
    # Get only files (excluding directories)
    files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]

    # Save to a text file
    with open(output_file, "w") as f:
        for file in files:
            f.write(file + "\n")

    print(f"File list saved to {output_file}")
except Exception as e:
    print(f"Error: {e}")
