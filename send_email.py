import smtplib
import email.message


def sendEmail(nome, mail, servico, numero):
    corpo_email = f"""
    <p>Nome: {nome}</p>
    <p>Email: {mail}</p>
    <p>Serviço: {servico}</p>
    <p>Numero: {numero}</p>
    """
    msg = email.message.Message()
    msg['Subject' ] = "Contato enviado via site KGS Corretora"
    msg['From'] = "kgscorretoradeseguros@gmail.com"
    msg['To'] = "kgscorretoradeseguros@gmail.com"
    password = "ywug dpsv zzxb euok"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
