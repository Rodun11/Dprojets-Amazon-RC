import smtplib
from email.message import EmailMessage

def alert_system(product, link, price, message1="", message2=""):
    email_address = 'nouvelletteadresse@hotmail.com'
    email_password = 'Esdtre1412%'

    msg = EmailMessage()
    msg['Subject'] = 'Alerte de baisse de prix'
    msg['From'] = email_address
    msg['To'] = 'rboadrian@icloud.com'
    msg.set_content(f"Bonjour, le prix de {product} a baissé, il est de {price} euros!\nLien : {link}\n{message1}, {message2}")
    #Paramètres serveur SMTP Outlook
    smtp_server = 'smtp.office365.com'
    smtp_port = 587

    try:
        #Connexion au serveur SMTP d'Outlook
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(email_address, email_password)

        # Envoi d'e-mail
        server.send_message(msg)

        print('E-mail envoyé avec succès')

    except Exception as e:
        print(f'Erreur lors de l\'envoi de l\'e-mail : {e}')

    finally:
        server.quit()
