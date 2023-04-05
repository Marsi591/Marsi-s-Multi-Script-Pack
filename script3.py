import tkinter as tk
import subprocess

def change_hwid():
    new_hwid = hwid_entry.get()
    subprocess.call(['wmic', 'bios', 'serialnumber', f'{new_hwid}'])

root = tk.Tk()
root.geometry("400x150")
root.title("Hardware ID Changer")

hwid_label = tk.Label(root, text="Enter new hardware ID:")
hwid_label.pack()

hwid_entry = tk.Entry(root)
hwid_entry.pack()

change_button = tk.Button(root, text="Change Hardware ID", command=change_hwid)
change_button.pack()

root.mainloop()
