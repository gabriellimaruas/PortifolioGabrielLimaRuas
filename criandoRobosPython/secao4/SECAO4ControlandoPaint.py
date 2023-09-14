#Secao 3
#Controlando o paint
import pyautogui as bot

# bot.position()
# bot.sleep(4)
# print(bot.position())

#posicao para pesquisar no windows
bot.press('win')
bot.moveTo(x=854, y=344, duration=1)
bot.click()
bot.write('Paint')
bot.press('enter')

#posicao para maximizar o paint x=1555, y=113
bot.sleep(1)
bot.moveTo(x=1555, y=113)
bot.sleep(1)
bot.click()

bot.moveTo(x=925, y=554)

distance = 200
while distance > 0:
    bot.dragRel(distance, 0, duration=0.5)   # move right
    distance -= 25
    bot.dragRel(0, distance, duration=0.5)   # move down
    bot.dragRel(-distance, 0, duration=0.5)  # move left
    distance -= 25
    bot.dragRel(0, -distance, duration=0.5)  # move up

