import schedule
import time
import os
from image_capture import capture_images_and_send_to_backend  # Import the function from your image capture script

def job():
    # Call the function to capture images and send them to the backend
    capture_images_and_send_to_backend()

# Schedule the job to run every day at 8 AM
schedule.every().day.at("03:40").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
