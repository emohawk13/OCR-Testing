import pyautogui
import numpy as np

def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    return screenshot