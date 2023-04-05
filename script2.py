import pyautogui
imagenumber = 1

while imagenumber <= 1:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'screenshot{imagenumber}.png')
    imagenumber += 1

print("Done!")
""
