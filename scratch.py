import pyautogui
import time
import math

def move_mouse_in_circles(x, y, width, height):
    center_x = x + width // 2
    center_y = y + height // 2
    radius = 40  # Initial radius
    angle = 0
    pyautogui.mouseDown(center_x, center_y)

    while radius < max(width, height) // 2:
        x_offset = int(radius * math.cos(angle))
        y_offset = int(radius * math.sin(angle))
        pyautogui.moveTo(center_x + x_offset, center_y + y_offset)
        angle += 0.2
        if angle >= 2 * math.pi:
            #angle = 0
            #radius += 120
            break

    pyautogui.mouseUp()

while True:
    for i in range(8):
        try:
            image_location = pyautogui.locateOnScreen('scratch1.png', confidence=0.6)
            if image_location is not None:
                image_location = pyautogui.center(image_location)
                pyautogui.click(image_location)
                time.sleep(0.2)
                move_mouse_in_circles(144, 288, 378, 322)
            else:
                print("Image 'scratch1.png' not found on the screen.")
        except pyautogui.ImageNotFoundException:
            print("Error: 'scratch1.png' not found.")
        
        time.sleep(0.5)
        
        try:
            image_location3 = pyautogui.locateOnScreen('add_money.png', confidence=0.7)
            if image_location3 is not None:
                # Get the center coordinates of the image
                image_center3 = pyautogui.center(image_location3)

                # Move the mouse to the center of the image and click
                pyautogui.click(image_center3)

                # Pause for a moment to ensure the click is registered
                time.sleep(0.2)
            else:
                print("Image 'add_money.png' not found on the screen.")
        except pyautogui.ImageNotFoundException:
            print("Error: 'add_money.png' not found.")
        
        try:
            image_locationad = pyautogui.locateOnScreen('lock.png', confidence=0.7)
            if image_locationad is not None:
                # Get the center coordinates of the image
                image_centerad = pyautogui.center(image_locationad)

                # Move the mouse to the center of the image and click
                pyautogui.click(image_centerad)

                # Pause for a moment to ensure the click is registered
                time.sleep(0.2)
            else:
                print("Image 'lock.png' not found on the screen.")
        except pyautogui.ImageNotFoundException:
            print("Error: 'lock.png' not found.")

        try:
            image_locationad = pyautogui.locateOnScreen('ads.png', confidence=0.7)
            if image_locationad is not None:
                try:
                    image_locationsk = pyautogui.locateOnScreen('adsk.png', confidence=0.7)
                    image_centerad = pyautogui.center(image_locationsk)
                    pyautogui.click(image_centerad)
                    time.sleep(0.2)
                except pyautogui.ImageNotFoundException:
                    print("Error: 'ads.png' not found.")
            else:
                print("Image 'ads.png' not found on the screen.")
        except pyautogui.ImageNotFoundException:
            print("Error: 'ads.png' not found.")
                    
        time.sleep(1)
    
    #a = input("Type 'e' or 'exit' to quit: ")
    #if a.lower() in ["e", "exit"]:
    #    break