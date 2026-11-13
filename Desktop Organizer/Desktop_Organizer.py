import shutil
import tkinter as tk
from pathlib import Path

# File extensions and their destination folders.
FILE_TYPES = {
    ".exe": "Programs",
    ".docx": "Documents",
    ".jpg": "Images",
    ".mp3": "Music",
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".zip": "Archives",
    ".xlsx": "Excel Files",
    ".pptx": "PowerPoint Files",
    ".mp4": "Videos",
    ".png": "PNG Images",
    ".gif": "GIF Images",
    ".bmp": "BMP Images",
    ".avi": "AVI Videos",
    ".wmv": "WMV Videos",
    ".mov": "MOV Videos",
    ".flv": "FLV Videos",
    ".psd": "Photoshop Files",
    ".html": "HTML Files",
    ".css": "CSS Files",
}

desktop_path = Path.home() / "Desktop"
moved_files = {}
created_folders = set()

root = tk.Tk()
root.title("Desktop Organizer")

label = tk.Label(root, text="Ready to organize your desktop.")
label.pack(padx=20, pady=10)


def organize():
    if not desktop_path.is_dir():
        label.config(text=f"Desktop folder not found: {desktop_path}")
        return

    organize_button.config(state=tk.DISABLED)
    moved_count = 0
    skipped_count = 0

    for source in list(desktop_path.iterdir()):
        if not source.is_file():
            continue

        folder_name = FILE_TYPES.get(source.suffix.lower())
        if not folder_name:
            continue

        destination_folder = desktop_path / folder_name
        destination = destination_folder / source.name

        if destination.exists():
            skipped_count += 1
            continue

        if not destination_folder.exists():
            destination_folder.mkdir()
            created_folders.add(destination_folder)

        try:
            shutil.move(str(source), str(destination))
        except OSError:
            skipped_count += 1
            continue

        moved_files[destination] = source
        moved_count += 1
        label.config(text=f"Moving {source.name} to {folder_name}")
        root.update_idletasks()

    undo_button.config(state=tk.NORMAL if moved_files else tk.DISABLED)
    organize_button.config(state=tk.NORMAL)
    label.config(
        text=f"Organization complete: {moved_count} moved, {skipped_count} skipped."
    )


def undo():
    restored_count = 0
    skipped_count = 0

    for destination, original in list(moved_files.items()):
        if not destination.exists():
            moved_files.pop(destination)
            skipped_count += 1
            continue

        if original.exists():
            skipped_count += 1
            continue

        try:
            shutil.move(str(destination), str(original))
        except OSError:
            skipped_count += 1
            continue

        moved_files.pop(destination)
        restored_count += 1

    for folder in list(created_folders):
        try:
            folder.rmdir()
            created_folders.remove(folder)
        except OSError:
            pass

    undo_button.config(state=tk.NORMAL if moved_files else tk.DISABLED)
    label.config(
        text=f"Undo complete: {restored_count} restored, {skipped_count} skipped."
    )


organize_button = tk.Button(root, text="Organize", command=organize)
organize_button.pack(pady=5)

undo_button = tk.Button(root, text="Undo", command=undo, state=tk.DISABLED)
undo_button.pack(pady=(0, 10))

root.mainloop()
