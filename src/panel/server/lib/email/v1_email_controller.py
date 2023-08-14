# import smtplib
import smtplib
import ssl
from configs.config import *
from email.message import EmailMessage
import json

class Email:
    def __init__(self):
        self.message = EmailMessage()


    def setSender(self, sender:str) -> None:  # set where the email is being sent from
        self.sender = sender


    def setReceiver(self, recipient:str) -> None:  # set who's receiving
        self.recipient = recipient


    def setSubject(self, subject:str) -> None:  # set the subject of said email
        self.subject = subject


    def setMessage(self, message:str) -> None:    # set message to send
        self.message = message


    def setCsrfToken(self, token:str) -> None:  # security
        self.token = token


    # sending html document with data
    def attachHtmlDocument(self, documentName, subType=None) -> None:
        try:
            if subType is None:
                subType = "html"

            self.message.add_alternative(documentName, subtype=subType)
        except Exception as e:
            print(f"error from the email sending class {str(e)}")


    def setUSR(self, USR:str) -> None:  # setting the username for the email
        self.USR = USR


    def setPSW(self, PSW:str) -> None:  # setting the password for the email
        self.PSW = PSW


    def send(self) -> bool:  # * sending the message.
        try:
            context = ssl.create_default_context()  # security

            # setting message to be sent
            self.message['From']    = self.sender
            self.message['To']      = self.recipient
            self.message['Subject'] = self.subject

            # connecting to the smtp email sending server
            with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT, context=context) as server:
                server.login(
                    self.USR,
                    self.PSW
                )

                sent = server.sendmail(
                    self.sender,
                    self.recipient,
                    self.message.as_string()
                )

                if sent:
                    return True

                else:
                    return False

        except Exception as e:
            return json.dumps(
                {
                    "error": "error"
                }
            )