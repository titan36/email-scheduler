import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    """Class for sending emails"""

    def __init__(self, senderEmail, password, smtpServer='smtp.gmail.com', smtpPort=587):
        """
        Initialize EmailSender object.

        Args:
            sender_email (str): This is the sender's email address.
            password (str): This is the sender's email password.
            smtp_server (str, optional if gmail used): SMTP server address. Defaults to 'smtp.gmail.com'.
            smtp_port (int, optional): SMTP server port. Defaults to 587.
        """
        self.senderEmail = senderEmail
        self.password = password
        self.smtpServer = smtpServer
        self.smtpPort = smtpPort

    def sendEmail(self, receiverEmail, subject, body, is_html=False):
        """
        This method will send the email.

        Args:
            receiverEmail (str): This is the recipient's email address.
            subject (str): This is the email subject.
            body (str): This is the email body.
            is_html (bool, optional): Whether the body is HTML format. Defaults to False.
        """

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = self.senderEmail
        msg['To'] = receiverEmail
        msg['Subject'] = subject

        # Email content
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(self.smtpServer, self.smtpPort) as smtp:
            smtp.starttls()
            smtp.login(self.senderEmail, self.password)
            smtp.send_message(msg)
