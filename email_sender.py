import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load .env variables locally
load_dotenv()


def send_email(trends, receiver_email):
    sender_email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    message = MIMEMultipart("alternative")
    message["Subject"] = "🌐 Daily Web Development Trends"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Build HTML content with share buttons
    html_trends = ""
    for trend in trends:
        twitter_share = f"https://twitter.com/intent/tweet?url={trend['url']}&text={trend['title']}"
        linkedin_share = f"https://www.linkedin.com/sharing/share-offsite/?url={trend['url']}"
        facebook_share = f"https://www.facebook.com/sharer/sharer.php?u={trend['url']}"

        html_trends += f"""
        <div style="margin-bottom:20px; padding:15px; border:1px solid #ddd; border-radius:8px;">
            <img src="{trend['image']}" alt="Article image" style="max-width:100%; height:auto; border-radius:5px;" />
            <h3><a href="{trend['url']}" target="_blank">{trend['title']}</a></h3>
            <p>{trend['description']}</p>
            <p>
                <a href="{twitter_share}" target="_blank" style="margin-right:10px;">🐦 Share on Twitter</a>
                <a href="{linkedin_share}" target="_blank" style="margin-right:10px;">💼 Share on LinkedIn</a>
                <a href="{facebook_share}" target="_blank">📘 Share on Facebook</a>
            </p>
        </div>
        """

    html = f"""
    <html>
      <body>
        <h2>🚀 Today's Top 3 Web Development Trends</h2>
        {html_trends}
        <p style="font-size:12px; color:gray;">Sent automatically at 7AM GMT</p>
      </body>
    </html>
    """

    message.attach(MIMEText(html, "html"))

    # Send email securely
    try:
        # Use TLS (STARTTLS) instead of SSL
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  # Can be omitted, but safe
            server.starttls(context=ssl.create_default_context())
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("✅ Email sent successfully using TLS")
    except Exception as e:
        print("❌ Error while sending email:", e)
