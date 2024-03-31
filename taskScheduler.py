import time
import threading

class Task:
    """Represents a task to be scheduled."""

    def __init__(self, func, args=(), kwargs={}):
        """
        Initialize a Task object.

        Args:
            func (callable): The function to be executed.
            args (tuple, optional): The arguments to pass to the function. Defaults to ().
            kwargs (dict, optional): The keyword arguments to pass to the function. Defaults to {}.
        """
        self.func = func
        self.args = args
        self.kwargs = kwargs

class Scheduler:
    """A simple scheduler for running tasks at specific times."""

    def __init__(self):
        """Initialize the Scheduler."""
        self.tasks = []
        self.running = False

    def add_task(self, task, time):
        """
        Add a task to the scheduler.

        Args:
            task (Task): The task to be scheduled.
            time (str): The time at which the task should be executed (in 'HH:MM' format).
        """
        self.tasks.append((task, time))

    def _run_task(self, task):
        """Run a task."""
        task.func(*task.args, **task.kwargs)

    def _check_tasks(self):
        """Check if there are any tasks to run."""
        current_time = time.strftime('%H:%M')

        for task, scheduled_time in self.tasks:
            if current_time == scheduled_time:
                self._run_task(task)

    def start(self):
        """Start the scheduler."""
        self.running = True
        while self.running:
            self._check_tasks()
            time.sleep(60)  # Check every minute

    def stop(self):
        """Stop the scheduler."""
        self.running = False
