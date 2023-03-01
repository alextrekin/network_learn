# from email.mime.text import MIMEText
# import smtplib
# msg = MIMEText("Hello there")
# msg['Teмa'] = "А Test Message"
# msg['Oт'] = 'John Mueller <trekin.alexey@gmail.com>'
# msg['Koмy'] = 'John Mueller <lexa199378@gmail.com>'
# s = smtplib.SMTP('173.194.222.138')
# print(s)
# s.sendmail('173.194.222.138', ['127.0.0.1'], msg.as_string())
import socket

print(socket.gethostbyaddr("smtp.yandex.com"))
print(socket.gethostbyaddr("gmail.com"))
