import pyautogui
import time

def get_region():
    print("Move your mouse to the top-left corner of the region and press Enter...")
    input()
    x1, y1 = pyautogui.position()

    print("Move your mouse to the bottom-right corner of the region and press Enter...")
    input()
    x2, y2 = pyautogui.position()

    # Calculate width and height
    width = x2 - x1
    height = y2 - y1

    return x1, y1, width, height

def main():
    print("You have 5 seconds to move your mouse to the desired screen before the selection starts...")
    time.sleep(5)  # Gives you time to move the mouse to the desired screen
    region = get_region()
    print(f"Selected region coordinates: (x, y, width, height = {region[0]}, {region[1]}, {region[2]}, {region[3]})")

if __name__ == "__main__":
    main()
