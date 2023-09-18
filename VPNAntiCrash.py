import pyautogui
import math
import time
import keyboard

pyautogui.PAUSE = 0.03
CIRCLE_RADIUS = 200

circle_points = []


def calculate_circle_points():
    screen_width, screen_height = pyautogui.size()  # Get screen dimensions
    screen_width //= 2
    screen_height //= 2

    for angle in range(0, 360, 5):
        radian = math.radians(angle)
        x = screen_width + int(CIRCLE_RADIUS * math.cos(radian))
        y = screen_height + int(CIRCLE_RADIUS * math.sin(radian))
        circle_points.append((x, y))

    return circle_points


# Function to check if the "Space" or "Esc" key is pressed
def check_keys():
    return


while True:  # Infinite loop
    circle_points = calculate_circle_points()

    for point in circle_points:
        pyautogui.moveTo(point)

        # Check if the "Space" or "Esc" key is pressed
        if keyboard.is_pressed("esc"):
            exit()

    # Wait for a few seconds before repeating the movement
    time.sleep(5)
