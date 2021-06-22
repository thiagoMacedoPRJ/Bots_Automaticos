import pyautogui
import time


p = pyautogui.position () # Obter a posição XY do mouse.


print(p)

'''

    pyautogui.click(100, 200) # Clicar Em Uma Parte Expecifica na Tela
    time.sleep(2)
    pyautogui.click(154, 486)
    time.sleep(1)
    pyautogui.write('TESTE!', intervalo = 0,25)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.doubleClick ()
    time.sleep(1)
    pyautogui.keyDown('a') # Pressione a tecla Shift e mantenha-a pressionada. 
    time.sleep(7)
    pyautogui.keyUp('a') # Solte a tecla Shift.
    time.sleep(3)
    pyautogui.hotkey ('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(155, 186)
    time.sleep(1)
    pyautogui.hotkey ('ctrl', 'v')


'''
