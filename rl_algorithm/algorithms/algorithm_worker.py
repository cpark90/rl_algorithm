from celery import Celery
import time

# Create a Celery instance
app = Celery('tasks', broker='redis://localhost:6379/0')

# Define the task
@app.task
def print_message(message, delay):
    time.sleep(delay)
    print(message)