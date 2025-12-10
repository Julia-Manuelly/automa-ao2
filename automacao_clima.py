import pyautogui
import time

pyautogui.FAILSAFE = True

time.sleep(3)

pyautogui.click(200, 200)

pyautogui.hotkey("ctrl", "l")
time.sleep(0.5)
pyautogui.write("https://www.google.com")
pyautogui.press("enter")

time.sleep(3)

pyautogui.write("Clima hoje na minha cidade")
pyautogui.press("enter")

time.sleep(4)

screenshot = pyautogui.screenshot()
screenshot.save("previsao.png")

print("Automação finalizada! Arquivo salvo como previsao.png")