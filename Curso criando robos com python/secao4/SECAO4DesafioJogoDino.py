#secao3
#Desafio Jogo do Dinossauro
import pyautogui as bot
import time
from PIL import ImageGrab

def isCollison(data):
    for i in range(720, 775):
        for j in range(290, 330):
            if data[i, j] < 100:
                print('Pulando')
                bot.keyDown('up')
                return
    return


while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    isCollison(data)

    # for i in range(720, 770):
    #     for j in range(290, 330):
    #         data[i, j] = 0
    #
    # image.show()
    # break


# bot.sleep(3)
# print(bot.position())