import os
import shutil

# Define the directory to organize
source_dir = "C:/Users/YourUsername/Downloads"  # Replace with your directory
organized_dir = "C:/Users/YourUsername/Organized"  # Directory to move organized files

# File type categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

# Function to organize files
def organize_files(source, target):
    if not os.path.exists(target):
        os.makedirs(target)

    # Create folders for categories if they don't exist
    for category in file_categories:
        folder_path = os.path.join(target, category)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through files in the source directory
    for item in os.listdir(source):
        item_path = os.path.join(source, item)

        if os.path.isfile(item_path):
            # Determine file category
            file_ext = os.path.splitext(item)[1].lower()
            moved = False

            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    shutil.move(item_path, os.path.join(target, category, item))
                    moved = True
                    break

            # If the file doesn't match any category, move it to 'Others'
            if not moved:
                shutil.move(item_path, os.path.join(target, "Others", item))

# Run the script
organize_files(source_dir, organized_dir)
print(f"Files from {source_dir} have been organized into {organized_dir}.")