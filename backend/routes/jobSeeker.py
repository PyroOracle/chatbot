from flask import Flask, request, jsonify
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
import os

# Load environment variables (e.g., for email config)
load_dotenv()

app = Flask(__name__)

# Optional: Dummy in-memory "database"
job_seekers = []

# Utility function to validate input
def validate_job_data(data):
    required_fields = ['name', 'email', 'phone', 'linkedin', 'experience', 'department']
    missing = [field for field in required_fields if field not in data or not data[field].strip()]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    
    try:
        validate_email(data['email'])  # check if email is valid
    except EmailNotValidError as e:
        return False, str(e)
    
    return True, "Valid"

# Endpoint to handle job seeker form submission
@app.route("/api/job-seeker", methods=["POST"])
def handle_job_seeker():
    data = request.json
    
    # Validate input
    is_valid, message = validate_job_data(data)
    if not is_valid:
        return jsonify({"status": "error", "message": message}), 400

    # Store in dummy database (you can replace with real DB)
    job_seekers.append(data)

    # Optional: Send confirmation or store to file/email system
    print(f"[INFO] Job application received: {data['name']} - {data['email']}")

    return jsonify({
        "status": "success",
        "message": f"Thank you {data['name']}! Your application has been received."
    })

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
