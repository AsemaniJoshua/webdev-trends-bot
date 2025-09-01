from trends_fetcher import get_trends
from email_sender import send_email
import os

if __name__ == "__main__":
    trends = get_trends()
    receiver_email = os.getenv("RECEIVER")
    send_email(trends, receiver_email)
