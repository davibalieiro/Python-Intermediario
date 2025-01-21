import pyautogui
from time import sleep

# acha o que tu colocar na foto na tela
# variavel = pyautogui.locateOnScreen('imagem.png')
# pyautogui.click(variavel)  # clica no lugar que tu mandar (no caso na imagem)
# pyautogui.write('mensagem')  # escreve em algum canto
# pyautogui.press('tecla')  # pressiona a tecla


# pip install opencv-python
counter = 1
while counter < 30:
    sleep(1)
    campo_de_msg = pyautogui.locateOnScreen('mensagem.png', confidence=0.8)
    pyautogui.click(campo_de_msg)
    pyautogui.write('@MATHEUS JOSÉÉÉÉ')
    pyautogui.press('Enter')
    counter += 1
