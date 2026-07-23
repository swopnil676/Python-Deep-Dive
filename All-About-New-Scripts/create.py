# for i in range(1, 13):
    # with open(f"code{i}.py", "w"):
        # pass

import os

# Replace this with your actual folder path
folder_path = "A:\CODING\ADVANCED PYTHON FOR MASTERY\Python Usable things"

# Optional: This line automatically creates the folder if it doesn't exist yet
os.makedirs(folder_path, exist_ok=True)

for i in range(1, 13):
    # Combines the folder path and the filename
    with open(f"{folder_path}/script{i}.py", "w") as f:
        pass