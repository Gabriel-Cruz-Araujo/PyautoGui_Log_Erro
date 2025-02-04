import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

email = os.getenv('EMAIL')
senha_email = os.getenv('SENHA_EMAIL')

def enviar_email(log_path):
    destinatario = 'gabrielindolfinho14@gmail.com'
    assunto = 'Erros encontrados no log'
    corpo_email = 'Segue em anexo os erros encontrados no log'

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remetente = email
    senha = senha_email

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo_email, 'plain'))

    if os.path.exists(log_path):
        with open(log_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log_path)}')
        msg.attach(part)
    else:
        print(f'Erro ao anexar arquivo {log_path}')

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        print('Email enviado com sucesso')
    except Exception as e:
        print(f'Erro ao enviar email: {e}')
    finally:
        server.quit()
