import smtplib
#biblioteca para estruturar texto
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = 'email@gmail.com'
toaddr = 'email@gmail.com', 'email@gmail.com'

#instancia do MIMEMultipart
msg = MIMEMultipart()

#email de qm vai enviar
msg['From'] = fromaddr
#para qm
msg['To'] = toaddr
#titulo do email
msg['Subject'] = 'E-mail de teste'
#email (corpo)
body = 'Email enviado do nosso robo.'

msg.attach(MIMEText(body, 'plain'))

#servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)
#seguranca
s.starttls()

#autenticacao
s.login(fromaddr, 'senha')

#converte para string
text = msg.as_string()

#enviar email
s.sendmail(fromaddr, ', '.join(toaddr), msg.as_string())


#fechar o servidor
s.quit()



