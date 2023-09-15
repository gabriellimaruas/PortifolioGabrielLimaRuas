#Secao 3
#Criando nosso primeiro projeto
import pyautogui as robo

robo.position()
robo.sleep(3)
print(robo.position())

robo.moveTo(x=811, y=1047, duration=2)
robo.rightClick()

robo.sleep(2)
robo.moveTo(x=300, y=390)
robo.dragTo(x=300, y=390, duration=2)

#COPIANDO OS DADOS DA AREA DE TRABALHO PARA A PASTA DOWNLOADS
robo.position()
robo.sleep(4)
print(robo.position())

#posicao para maximizar
robo.moveTo(x=958, y=210, duration=1)
robo.click()

#posicao da pasta de arquivo x=935, y=1057
robo.moveTo(x=935, y=1057, duration=1)
robo.click()

#posicao area de trabalho x=340, y=200
robo.moveTo(x=340, y=200, duration=1)
robo.doubleClick()

#posicao de onde arrastar
robo.moveTo(x=233, y=146, duration=1)

#posicao para onde arrastar x=1884, y=983
robo.dragTo(x=1884, y=983, duration=1)
controlC = robo.hotkey('ctrl', 'c')

#posicao pasta de download
robo.moveTo(x=129, y=287, duration=1)
robo.click()

#colando na pasta de download
robo.hotkey('ctrl', 'v')


