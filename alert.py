# import smtplib
# from email.message import EmailMessage
# def email_alert(subject,body,to):
#     msg=EmailMessage()
#     msg.set_content(body)
#     msg['subject']=subject
#     msg['to']=to
#     user="email.alert.cyberattack@gmail.com"
#     msg['from']=user
#     password="yjcsekbdlgdxwikp"

#     server=smtplib.SMTP("smtp.gmail.com",587)
#     server.starttls
#     server.login(user,password)
#     server.send_message(msg)
#     server.quit()

# if __name__ == '__main__':
#     email_alert("File modification detected!","We have detected some modifications in your files.","priyanshuvarshney1406@gmail.com")

import smtplib
import ssl
from email.message import EmailMessage

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change for Outlook, Yahoo, etc.
SMTP_PORT = 465  # Use 587 for STARTTLS
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "kcesoslmuovbqhbp"  # Use an app password for security
RECIPIENT_EMAIL = "priyanshuvarshney1406@gmail.com"

def send_email_alert(file_name):
    """Send an email alert after detecting ransomware activity"""
    subject = "⚠️ Ransomware Attack Detected!"
    body = f"ALERT: Suspicious ransomware activity detected!\nAffected File: {file_name}\nImmediate action is recommended."

    # Creating Email Message
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    # Sending Email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL_PORT(SMTP_SERVER, SMTP_PORT, context=context) as server:
            
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            server.send_message(msg)
        print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage (Trigger email after ransomware detection)
if __name__ == "__main__":
    detected_file = "encrypted_document.docx"
    send_email_alert(detected_file)

