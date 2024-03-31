from taskScheduler import Scheduler, Task
import time

class EmailScheduler:
    """Class responsible for scheduling email sending."""

    def __init__(self, email_sender):
        """
        Initialize EmailScheduler object.

        Args:
            email_sender (EmailSender): Instance of EmailSender for sending emails.
        """
        self.email_sender = email_sender
        self.scheduler = Scheduler()

    def schedule_daily_email(self, receiver_email, subject, body, is_html=False, time='12:09'):
        """
        Schedule sending a daily email.

        Args:
            receiver_email (str): Recipient's email address.
            subject (str): Email subject.
            body (str): Email body.
            is_html (bool, optional): Whether the body is HTML format. Defaults to False.
            time (str, optional): Time of day to send the email in 'HH:MM' format. Defaults to '09:00'.
        """
        def send_email_task():
            """Inner function to send the email."""
            self.email_sender.sendEmail(receiver_email, subject, body, is_html)

        # Create a task to send email
        email_task = Task(func=send_email_task)

        # Add the task to the scheduler
        self.scheduler.add_task(email_task, time)

    def run_scheduler(self):
        """Run the scheduler continuously."""
        self.scheduler.start()
