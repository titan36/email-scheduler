from emailSender import EmailSender
from emailScheduler import EmailScheduler

# Create an instance of EmailSender with your email credentials
sender_email = "info@gmail.com"
password = "yourpassword"
email_sender = EmailSender(sender_email, password)

# Read the content of the HTML file
with open('htmlfile.html', 'r') as file:
    html_body = file.read()

# Create an instance of EmailScheduler using the EmailSender instance
email_scheduler = EmailScheduler(email_sender)

# Schedule sending a daily email
receiver_email = "titushailu125@gmail.com"
subject = "Daily Report"
#html_body = "<html><body><h1>This is a HTML email</h1><p>This is a paragraph</p></body></html>"
email_scheduler.schedule_daily_email(receiver_email, subject, html_body, is_html=True, time='01:00')

#body = "Put your daily report content here."
#email_scheduler.schedule_daily_email(receiver_email, subject, body, time='00:22')

# Run the scheduler
email_scheduler.run_scheduler()
