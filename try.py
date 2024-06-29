import simpleaudio as sa

def play_error_sound():
    # Load a sound file
    wave_obj = sa.WaveObject.from_wave_file("error.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

try:
    # Example of code that might raise an error
    print("Trying to execute code...")
    1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print("An error occurred:", e)
    play_error_sound()

# This code will continue to execute after the exception handling
print("Continuing execution...")
# More code here
