from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Allow access from frontend

# Optional: For email notifications (requires configuration)
# import smtplib
# from email.mime.text import MIMEText

# Route for client submissions
@app.route('/api/client/submit', methods=['POST'])
def submit_client_info():
    try:
        data = request.get_json()

        required_fields = ['company_name', 'contact_name', 'email', 'phone', 'service', 'project_description']

        # Validate required fields
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"{field} is required."}), 400

        # Basic email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            return jsonify({"error": "Invalid email address."}), 400

        # Log or save the data (for now, we just print it)
        print("📩 New Client Inquiry:")
        print(f"Company: {data['company_name']}")
        print(f"Contact Name: {data['contact_name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Service Needed: {data['service']}")
        print(f"Project Description: {data['project_description']}")

        # Optional: Send an email notification (configure SMTP)
        # send_notification_email(data)

        return jsonify({"message": "Client data received successfully!"}), 200

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": "An error occurred while processing the request."}), 500


# Optional: Email sending function
# def send_notification_email(data):
#     smtp_server = "smtp.gmail.com"
#     port = 587
#     sender_email = "yourcompany@example.com"
#     password = "your_password"

#     subject = "New Client Inquiry - TechnoBot"
#     body = f"""
#     Company: {data['company_name']}
#     Contact Name: {data['contact_name']}
#     Email: {data['email']}
#     Phone: {data['phone']}
#     Service Needed: {data['service']}
#     Description: {data['project_description']}
#     """

#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = "client.inquiries@technobrain.com"

#     server = smtplib.SMTP(smtp_server, port)
#     server.starttls()
#     server.login(sender_email, password)
#     server.sendmail(sender_email, msg['To'], msg.as_string())
#     server.quit()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
