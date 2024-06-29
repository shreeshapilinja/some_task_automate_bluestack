import pyautogui
import easyocr
import cv2
import time
import numpy as np
import re
from playsound import playsound

def play_error_sound():
    try:
        print("*********** Error sound played successfully.  ***************")
        playsound('error.wav')
    except Exception as e:
        print(f"Error playing sound: {e}")

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])
count = 0
while True:
    for i in range(6):
        x, y, width, height = 188, 405, 320, 155

        # Define the region coordinates (x, y, width, height)
        region = (x, y, width, height)

        # Capture the screen region
        screenshot = pyautogui.screenshot(region=region)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # Use EasyOCR to extract text
        result = reader.readtext(screenshot)

        # Extract the text from the result
        extracted_text = ' '.join([item[1] for item in result])
        print("Extracted Text:", extracted_text)

        # Replace misdetected '4' with '+'
        cleaned_text = re.sub(r'\b4\b', '+', extracted_text)
        print("Cleaned Text:", cleaned_text)

        # Clean the extracted text and extract numbers
        try:
            # Split text by either '+' or spaces
            parts = re.split(r'\+|\s+', cleaned_text)
            numbers = [int(part.strip()) for part in parts if part.strip().isdigit()]
            
            if len(numbers) == 2:
                num1, num2 = numbers
                calculated_result = num1 + num2
                print("Calculated Result:", calculated_result)
                count = 0
                try:
                    image_location = pyautogui.locateOnScreen('enter_ans.png', confidence=0.8)
                    if image_location is not None:
                        # Get the center coordinates of the image
                        image_center = pyautogui.center(image_location)

                        # Move the mouse to the center of the image and click
                        pyautogui.click(image_center)

                        # Pause for a moment to ensure the click is registered
                        time.sleep(0.2)

                        pyautogui.click(image_center)

                        # Pause for a moment to ensure the click is registered
                        time.sleep(0.1)

                        # Type the text at the current cursor position
                        pyautogui.write(str(calculated_result))
                    else:
                        print("Image 'enter_ans.png' not found on the screen.")
                except pyautogui.ImageNotFoundException:
                    print("Error: 'enter_ans.png' not found.")

                try:
                    image_location2 = pyautogui.locateOnScreen('submit.png', confidence=0.8)
                    if image_location2 is not None:
                        # Get the center coordinates of the image
                        image_center2 = pyautogui.center(image_location2)

                        # Move the mouse to the center of the image and click
                        pyautogui.click(image_center2)

                        # Pause for a moment to ensure the click is registered
                        time.sleep(0.2)
                    else:
                        print("Image 'submit.png' not found on the screen.")
                except pyautogui.ImageNotFoundException:
                    print("Error: 'submit.png' not found.")

                time.sleep(0.9)

                try:
                    image_location3 = pyautogui.locateOnScreen('add_money.png', confidence=0.6)
                    if image_location3 is not None:
                        # Get the center coordinates of the image
                        image_center3 = pyautogui.center(image_location3)
                        
                        # Move the mouse to the center of the image and click
                        pyautogui.click(image_center3)
                        
                        # Pause for a moment to ensure the click is registered
                        time.sleep(0.2)
                        
                        # Move the mouse to the center of the image and click
                        pyautogui.click(image_center3)

                        # Pause for a moment to ensure the click is registered
                        time.sleep(0.1)
                    else:
                        print("Image 'add_money.png' not found on the screen.")
                except pyautogui.ImageNotFoundException:
                    print("Error: 'add_money.png' not found.")
                
                time.sleep(0.4)
                
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
                print(count)    
            else:
                print("Extracted text does not contain two valid numbers.")
                count += 1
                if count in [6, 8, 10, 12, 14, 16, 18] or count > 19:
                    try:
                        play_error_sound()
                    except:
                        print("error in song")
        except ValueError as e:
            print("Error processing extracted text:", e)
        time.sleep(1)

    try:
        image_locationback = pyautogui.locateOnScreen('back.png', confidence=0.7)
        if image_locationback is not None:
            # Get the center coordinates of the image
            image_centerback = pyautogui.center(image_locationback)

            # Move the mouse to the center of the image and click
            pyautogui.click(image_centerback)

            # Pause for a moment to ensure the click is registered
            time.sleep(0.2)
    except pyautogui.ImageNotFoundException:
        print("Error: 'back.png' not found.")

    try:
        image_locationlock = pyautogui.locateOnScreen('lock.png', confidence=0.8)
        if image_locationlock is not None:
            # Get the center coordinates of the image
            image_centerlock = pyautogui.center(image_locationlock)

            # Move the mouse to the center of the image and click
            pyautogui.click(image_centerlock)

            # Pause for a moment to ensure the click is registered
            time.sleep(0.2)
    except pyautogui.ImageNotFoundException:
        print("Error: 'lock.png' not found.")

    try:
        image_location3 = pyautogui.locateOnScreen('add_money.png', confidence=0.6)
        if image_location3 is not None:
            image_center3 = pyautogui.center(image_location3)
            pyautogui.click(image_center3)
            time.sleep(0.2)

        else:
            print("Image 'add_money.png' not found on the screen.")
    except pyautogui.ImageNotFoundException:
        print("Error: 'add_money.png' not found.")

    #a = input("Type 'e' or 'exit' to quit: ")
    #if a.lower() in ["e", "exit"]:
    #    break
