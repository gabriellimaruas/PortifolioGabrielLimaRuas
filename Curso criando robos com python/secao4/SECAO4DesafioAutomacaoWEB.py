#secao3
#Desafio Automação WEB
import pyautogui as bot
import time

bot.PAUSE = 0.2
bot.FAILSAFE = True

bot.hotkey('win', 'r')
bot.typewrite('https://www.gabrielcasemiro.com.br/atividade_pyautogui \n')

time.sleep(2)

with open('membros.csv') as f:
    next(f)

    for line in f:
        line=line.strip()
        line=line.split(';')
        print('Dados: ', line)

        name=line[0]
        sex=line[1]
        email=line[2]
        phone=line[3]

        bot.click(bot.locateCenterOnScreen('imgsecao4\\nomeFuncionario.png', confidence=0.8), duration=0.2)
        bot.typewrite(name, interval=0.1)
        bot.click(bot.locateCenterOnScreen('imgsecao4\\emailFuncionario.png', confidence=0.8), duration=0.2)
        bot.typewrite(email, interval=0.1)
        bot.click(bot.locateCenterOnScreen('imgsecao4\\phoneFuncionario.png', confidence=0.8), duration=0.2)
        bot.typewrite(phone, interval=0.1)
        bot.click(bot.locateCenterOnScreen('imgsecao4\\sexoFuncionario.png', confidence=0.8), duration=0.2)
        if sex == 'Masculino':
            bot.click(bot.locateCenterOnScreen('imgsecao4\\masculino.png', confidence=0.8), duration=0.2)
        else:
            bot.click(bot.locateCenterOnScreen('imgsecao4\\feminino.png', confidence=0.8), duration=0.2)

        bot.screenshot(f'cadastro_{name}.png')
        bot.click(bot.locateCenterOnScreen('imgsecao4\\cadastrar.png', confidence=0.8), duration=0.2)

        time.sleep(3)
bot.alert(text='Programa finalizado com sucesso!', title='Aviso do sistema', button='OK')


