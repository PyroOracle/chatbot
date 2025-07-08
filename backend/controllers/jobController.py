from flask import request, jsonify
import re

# Simulate a database (can be replaced with real DB)
job_seekers = []

# Simple email validation function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Job Seeker Handler Function
def submit_job_seeker():
    data = request.get_json()

    required_fields = [
        "name", "email", "phone", "linkedin",
        "experience", "department"
    ]

    # Check for missing fields
    missing = [field for field in required_fields if field not in data or not data[field]]
    if missing:
        return jsonify({
            "status": "error",
            "message": f"Missing required fields: {', '.join(missing)}"
        }), 400

    # Validate email
    if not is_valid_email(data["email"]):
        return jsonify({"status": "error", "message": "Invalid email address"}), 400

    # Save to list (or database)
    job_seekers.append(data)

    # Simulate sending email or storing into DB
    print("Job seeker submitted:", data)

    return jsonify({
        "status": "success",
        "message": f"Thank you {data['name']}! Your information has been received. Please send your CV to careers@technobrain.com"
    }), 200
