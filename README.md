# HTML Email Scheduler

The HTML Email Scheduler is a Python library I have been using for my projects to automate email send and it allows me to schedule and send plain and styled HTML emails automatically. With this library, you can easily create and schedule emails with customized HTML content for various purposes such as newsletters, reports, announcements, etc.

## Features

- Schedule sending of emails at specific times.
- Include styled HTML content in the emails.
- Easy-to-use interface with customizable options.

## Installation

To install the HTML Email Scheduler library, you can use pip:

```
pip install html-email-scheduler
```

## Usage

```python
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
```

Replace `"info@gmail.com"` and `"yourpassword"` with your actual email address and password. Similarly, replace `"titushailu125@gmail.com"` with the recipient's email address.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
Fell free to do what ever you want.
---
