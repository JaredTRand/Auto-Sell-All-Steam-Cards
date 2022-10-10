import pyautogui
from time import sleep

img1 = r"C:\Users\jared\OneDrive\Desktop\Code Dumb\steamsellcards\carddrops.png"
img2 = r"C:\Users\jared\OneDrive\Desktop\Code Dumb\steamsellcards\profilename.png"
img3 = r"C:\Users\jared\OneDrive\Desktop\Code Dumb\steamsellcards\viewmyprofile.png"
img4 = r"C:\Users\jared\OneDrive\Desktop\Code Dumb\steamsellcards\level.png"
img5 = r"C:\Users\jared\OneDrive\Desktop\Code Dumb\steamsellcards\sellonmarket.png"
img6 = r"C:\Users\jared\OneDrive\Desktop\Code Dumb\steamsellcards\createlistings.png"

def get_pos_of(img):
    isOnScreen = None
    i = 0
    
    while isOnScreen == None:
        isOnScreen = pyautogui.locateOnScreen(img, grayscale=True, confidence=.75)
        i += 1
        if i > 1:
            print("Can't find selection.")
        if i > 10:
            print("Couldn't find selection. \nStopping...")
            quit()
        sleep(.5)

    [LocX, LocY, _, _] = pyautogui.locateOnScreen(img, grayscale=True, confidence=.75)
    return(LocX, LocY)

def click(buttonClick):
    pyautogui.mouseDown(button=buttonClick)
    pyautogui.mouseUp(button=buttonClick)
    sleep(1.5)

def get_to_cards():
    curPos = get_pos_of(img2)
    pyautogui.moveTo(curPos[0]+50, curPos[1]+20)
    click('left')

    curPos = get_pos_of(img3)
    pyautogui.moveTo(curPos[0]+20, curPos[1]+10)
    click('left')

    curPos = get_pos_of(img4)
    pyautogui.moveTo(curPos[0]+50, curPos[1]+20)
    click('left')

def sell_pack():
    curPos = get_pos_of(img1)
    pyautogui.moveTo(curPos[0]-300, curPos[1])
    click('left')

    curPos = get_pos_of(img5)
    pyautogui.moveTo(curPos[0]+50, curPos[1]+20)
    click('left')

    sleep(3)
    pyautogui.scroll(-5000)

    curPos = get_pos_of(img6)
    pyautogui.moveTo(curPos[0]+50, curPos[1]+20)
    click('left')

if __name__ == "__main__":
    while True:
        get_to_cards()
        sell_pack()
