import smtplib
from email.message import EmailMessage

# ========== Configuration ==========
SMTP_SERVER = 'smtp.gmail.com'        # Use your email provider's SMTP server
SMTP_PORT = 587                       # Port for TLS
EMAIL_ADDRESS = 'yourcompanyemail@gmail.com'     # Replace with your email
EMAIL_PASSWORD = 'your_app_password'             # Use an App Password or environment variable
RECEIVER_EMAIL = 'careers@example.com'       # Where to send the emails (HR/Client desk)
# ===================================

def send_email(subject, body, reply_to=None):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECEIVER_EMAIL
        if reply_to:
            msg['Reply-To'] = reply_to
        msg.set_content(body)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        
        print("✅ Email sent successfully.")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False


# ========== Sample Usage ==========
if __name__ == "__main__":
    subject = "New Job Application via TechnoBot"
    body = """
    New job seeker information received from TechnoBot chatbot:

    Full Name: Jane Doe
    Email: janedoe@example.com
    Phone: +254700123456
    LinkedIn: https://linkedin.com/in/janedoe
    Years of Experience: 3
    Department: Engineering

    Please follow up or check resume as requested.
    """
    send_email(subject, body, reply_to="janedoe@example.com")
