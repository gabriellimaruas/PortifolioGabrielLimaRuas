#Secao 3
#localizando imagens
import pyautogui as bot
# -------------------------------------------------------
bot.locateOnScreen("imgsecao4\\button5.png")
print(bot.locateCenterOnScreen("imgsecao4\\button5.png"))

bot.moveTo(1528, 738, duration=2)
bot.click(bot.locateCenterOnScreen("imgsecao4\\button5.png"))

# ------------------------------------------------------
# usando o confidence
print(bot.locateCenterOnScreen("imgsecao4\\button5.png", confidence=0.2))
# usando o grayscale
print(bot.locateCenterOnScreen("imgsecao4\\button5.png", grayscale=True))

# ------------------------------------------------------
# Controlando o teclado

bot.position(x=1286, y=340)
bot.click(x=1286, y=340, duration=1)

bot.typewrite('Hello World')

bot.press('enter')

bot.write('Hello World')

# Funcao de teclado
bot.keyDown('alt')
bot.keyDown('tab')
bot.keyUp('alt')
bot.keyUp('tab')
bot.press('enter')

# eu prefiro usar
bot.hotkey('alt', 'tab')
bot.press('enter')
