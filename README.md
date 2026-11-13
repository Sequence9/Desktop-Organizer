# Desktop Organizer

A small Tkinter utility that groups files on your desktop into folders based on
their extensions.

## How it works

Run the application and click **Organize** to begin. Recognized files are moved
into category folders such as Documents, Images, Music, Videos, and Archives.
Files with unknown extensions are left untouched.

The operation is now opt-in: simply launching the app does not move anything.
The **Undo** button restores files moved during the current session and removes
category folders created by the app when they are empty.

For safety, a file is skipped when a destination file with the same name already
exists. If an original path becomes occupied before an undo, that file is also
skipped instead of being overwritten.

## Run

Python 3 includes Tkinter on most Windows installations:

```powershell
python "Desktop Organizer/Desktop_Organizer.py"
```

The utility expects the desktop at `Desktop` inside the current user's home
folder.
