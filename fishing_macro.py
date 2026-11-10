import pygetwindow as getwindow
import time
import pyautogui
import keyboard
import threading

# arcane odyssey fishing macro

#f1 to start
#f2 to stop

running = False


def setup_window():
    windows = getwindow.getWindowsWithTitle("Roblox")
    target_win = None
    for win in windows:
        if "RobloxPlayerBeta.exe" in win.title or "Roblox" in win.title:
            target_win = win
            break
    if target_win:
        target_win.activate()
        time.sleep(0.2)

        width, height = target_win.width, target_win.height
        screen_width, screen_height = pyautogui.size()

        if width >= screen_width and height >= screen_height: #check fullscreen
            keyboard.press('F11')
            time.sleep(0.1)

        target_win.resizeTo(800, 599)

## macro functions
def color_close(actual, target, tolerance=40):
    for a, t in zip(actual, target):
        if not (t - tolerance <= a <= t + tolerance):
            return False
    return True

def wait_for_exclamation():
    start_time = time.time()  # timer failsafe
    timeout = 60
    while running:
        if time.time() - start_time > timeout:
            print("exclamation timeout reached, exiting...")
            break
        print("WAITING FOR FISH")
        pixel_1 = pyautogui.pixel(400, 293)
        pixel_2 = pyautogui.pixel(406, 303)
        if color_close(pixel_1, (242, 61, 61)) or color_close(pixel_2, (245,244,244)):
            break
        time.sleep(0.2)


def reel_in():
    start_time = time.time() # timer failsafe
    timeout = 15
    while running:
        if time.time() - start_time > timeout:
            print("reel timeout reached, exiting...")
            break

        print("reel")
        pixel_1 = pyautogui.pixel(714, 473)
        pixel_2 = pyautogui.pixel(714, 474)
        pixel_3 = pyautogui.pixel(697, 473)
        pixel_4 = pyautogui.pixel(703, 473)
        pyautogui.click(572, 334, button='left')
        if color_close(pixel_1, (127, 127, 3)) or color_close(pixel_2, (255, 255, 0)) or color_close(pixel_3, (114, 112, 49)) or color_close(pixel_4, (197, 198, 2)):
            break
        time.sleep(0.05)
    time.sleep(0.5)

def eat():
    pixel = pyautogui.pixel(65, 575)
    if not color_close(pixel, (106, 72, 33), tolerance=20):
        print("EATING")
        time.sleep(0.5)
        keyboard.press_and_release('0')
        time.sleep(0.5)
        for i in range(5):
            pyautogui.click(572, 334, button='left')
            time.sleep(0.3)


def cast():
    print("CASTING")
    keyboard.press_and_release('1')
    keyboard.press_and_release('9')
    time.sleep(0.5)
    pyautogui.click(572, 334, button='left')

def macro_loop():
    pyautogui.click(572, 334, button='left')
    time.sleep(1)

    while running:
        if keyboard.is_pressed('F2'):
            print("macro quit")
            break

        eat()  # check if need to eat

        cast()
        wait_for_exclamation()
        reel_in()

def start_macro():
    global running
    if not running:
        setup_window()
        print("start macro")
        running = True
        threading.Thread(target=macro_loop, daemon=True).start()

def stop_macro():
    global running
    if running:
        print("stop macro")
        running = False

keyboard.add_hotkey('F1', start_macro)
keyboard.add_hotkey('F2', stop_macro)
print("-== FISHING MACRO ==-")
print("================================")
print("Press F1 to start, F2 to stop, ESC to exit.")
print("================================")
print("PUT FISHING ROD in SLOT 9")
print("PUT FOOD IN SLOT 0")
print("================================")
print("setup by shift-lock look straight down \n then zoom all the way out then unshift-lock \n MAKE SURE ON SOLID GROUND \n boats can cause lighting issues")
print("================================")
setup_window()
keyboard.wait('esc')
print("Program exited.")
