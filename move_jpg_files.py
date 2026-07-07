import os
import shutil

source_folder = r"C:\Users\dell\Desktop\Task3\Source"
destination_folder = r"C:\Users\dell\Desktop\Task3\Destination"

os.makedirs(destination_folder, exist_ok=True)

for file in os.listdir(source_folder):
    if file.endswith(".jpg"):
        shutil.move(
            os.path.join(source_folder, file),
            os.path.join(destination_folder, file)
        )
        print(f"Moved: {file}")

print("All JPG files moved successfully!")