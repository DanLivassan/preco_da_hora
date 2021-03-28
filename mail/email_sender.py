from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, PackageLoader, select_autoescape
import os
import mail.creds as creds


class EmailSender:

    @staticmethod
    def send_mail(bodyContent, to_email, subject):
        to_email = to_email
        from_email = creds.USER
        subject = subject
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = from_email
        message['To'] = to_email
        message.attach(MIMEText(bodyContent, "html"))
        msgBody = message.as_string()
        server = SMTP(creds.HOST, creds.PORT)
        server.starttls()
        server.login(from_email, creds.PASSWORD)
        server.sendmail(from_email, to_email, msgBody)
        server.quit()

    @staticmethod
    def send_products(products):
        env = Environment(
            loader=PackageLoader('templates', ''),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('child.html')
        output = template.render(data=products)
        EmailSender.send_mail(output, "daniloxc@msn.com", "Produtos")
