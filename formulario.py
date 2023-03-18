import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_address = 'correo_del_remitente@gmail.com'
password = 'contraseña_del_remitente'

to_address = 'jonaferreyra111@gmail.com'
subject = 'Consulta desde el sitio web'

nombre = 'Juan Perez'
email = 'juan.perez@gmail.com'
telefono = '555-1234'
mensaje = 'Quería hacer una consulta sobre sus productos.'

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

body = f"""
Nombre: {nombre}
Correo electrónico: {email}
Teléfono: {telefono}

Mensaje:
{mensaje}
"""

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_address, password)
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()

print('El correo ha sido enviado correctamente.')
