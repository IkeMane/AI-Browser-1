from Browsing import analyze_content, click_element, visit_url
from pynput import keyboard

def on_activate():
    try:
        print("Activated!\n")  # Debug print to confirm activation
        result = analyze_content("Answer the following question")
        print(f"AI response: {result}\n")  
        click_result = click_element(result)  #Assuming analyze_content expects a question and screenshot
        print(f"Click result: {click_result}\n")  # Debug print to confirm completion
        # You could replace this with any action based on the result
        print("Done!\n\n")  # Debug print to confirm completion
    except Exception as e:
        print(f"Error: {e}")

def for_canonical(f):
    return lambda k: f(keyboard.Key.from_canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<cmd>+<shift>+f'), on_activate)

def on_press(key):
    try:
        hotkey.press(key)
    except AttributeError:
        pass  # Handle the exception if the key event doesn't have a char attribute

def on_release(key):
    try:
        hotkey.release(key)
    except AttributeError:
        pass  # Handle the exception if the key event doesn't have a char attribute

# Set up the listener
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# Visit Google as the initial URL
visit_url("https://www.google.com")

# Keep the program running
listener.join()
