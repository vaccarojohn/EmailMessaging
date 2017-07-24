import smtplib
from email.mime.text import MIMEText

def sendMail(subject, body, fromEmail, toEmail, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = toEmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(fromEmail, password)
    server.sendmail(fromEmail, toEmail, msg.as_string())
    server.close()
