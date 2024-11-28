import pyautogui
import cv2
import numpy as np



import cv2
import numpy as np
import pyautogui
import time

# Step 1: Define output file settings
output_file = "screen_recording.avi"  # Name of the output file
fps = 20.0  # Frames per second
screen_size = pyautogui.size()  # Get screen resolution

# Step 2: Define video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec for AVI files
out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

print("Recording will start in 3 seconds...")
time.sleep(3)  # Delay to prepare for recording

try:
    print("Recording started. Press 'Ctrl+C' to stop.")
    while True:
        # Step 3: Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Step 4: Convert screenshot to a format compatible with OpenCV
        frame = np.array(screenshot)  # Convert to numpy array
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color format

        # Step 5: Write frame to video file
        out.write(frame)
except KeyboardInterrupt:
    print("Recording stopped.")

# Step 6: Release resources
out.release()
cv2.destroyAllWindows()
