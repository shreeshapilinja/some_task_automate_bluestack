import pyautogui
import time

while True:
    for i in range(8):
        try:
            image_location = pyautogui.locateOnScreen('spin.png', confidence=0.7)
            if image_location is not None:
                image_location = pyautogui.center(image_location)
                pyautogui.click(image_location)
                time.sleep(0.2)
            else:
                print("Image 'spin.png' not found on the screen.")
        except pyautogui.ImageNotFoundException:
            print("Error: 'spin.png' not found.")
        
        time.sleep(5.2)
        
        try:
            image_location2 = pyautogui.locateOnScreen('add_money.png', confidence=0.7)
            if image_location2 is not None:
                # Get the center coordinates of the image
                image_center2 = pyautogui.center(image_location2)

                # Move the mouse to the center of the image and click
                pyautogui.click(image_center2)

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
        time.sleep(0.2)
    
    #a = input("Type 'e' or 'exit' to quit: ")
    #if a.lower() in ["e", "exit"]:
    #    break