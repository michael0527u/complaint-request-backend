import os
import aiosmtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

async def send_email(to_email: str, subject: str, content: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_USERNAME
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(content)

    try:
        await aiosmtplib.send(
            msg,
            hostname=SMTP_SERVER,
            port=SMTP_PORT,
            start_tls=True,
            username=EMAIL_USERNAME,
            password=EMAIL_PASSWORD,
        )
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
