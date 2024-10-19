from imports import *

load_dotenv()

def send_email(receiver, report_file):
    """Envia um e-mail com o relatório PDF anexado."""
    sender = os.getenv('Email_Sender')
    password = os.getenv('Email_Password')

    if not sender or not password:
        print("Erro: credenciais de e-mail não encontradas.")
        return

    subject = 'Relatório de Preços das Criptomoedas'
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    with open(report_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(report_file)}')
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha no envio do e-mail para {receiver}: {e}")