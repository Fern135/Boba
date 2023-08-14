
from django.core.mail import get_connection, EmailMessage, EmailMultiAlternatives
from django.core.mail import  send_mail
from configs.config import Config ####### i don't know why this is giving so many errors
from lib.util.util import valEmail, error


# conn = mail.get_connection() # !<====> DO NOT DELETE. may not use. not sure yet

class SendEmail:

    def __init__(self, subject) -> None:
        self.subject    = subject  # needed and used
        self.from_email = None
        self.to_email   = None
        self.connection = get_connection(
            backend     = 'django.core.mail.backends.smtp.EmailBackend',
            use_tls     = True, 
            host        = Config.MAIL_SERVER,
            port        = Config.MAIL_PORT, 
            username    = Config.MAIL_USERNAME, 
            password    = Config.MAIL_PASSWORD
        )
        self.filled_in  = self.subject is not None and self.from_email is not None and self.to_email is not None


    def __del__(self) -> None:
        if self.filled_in:
            self.subject    = None
            self.from_email = None
            self.to_email   = None
            self.connection.close()


    def setFromEmail(self, from_email):
        self.from_email = from_email

    def setToEmail(self, to_email):
        self.to_email = to_email

    def attatch_html(self, html):
        self.html = html

    
    def Send(self):
        try:
            #  {'context': 'values'}
            # plain_message   = strip_tags(html_message)
            # self.con.open()
            from_email = 'webdesignbusiness11@gmail.com'
            to_email   = 'webdesignbusiness11@gmail.com'

            # TODO: If send_mail does not work. use this
            # msg = EmailMessage(
            #     self.subject,
            #     self.html,
            #     from_email,
            #     [to_email],
            #     [self.html],
            #     # connection = self.connection
            # )

            send_mail(
                subject = self.subject,
                message = self.html,
                from_email     = from_email,
                recipient_list = [to_email],
                fail_silently  = True,
                html_message   = self.html,
                connection     = self.connection
            )

        except Exception as e:
            print(f"{error} * error is in the sending of the Send_Email_v2\n error: {str(e)}")
