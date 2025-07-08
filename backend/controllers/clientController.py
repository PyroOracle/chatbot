from flask import Blueprint, request, jsonify
import re

client_bp = Blueprint('client', __name__)

# Simulated storage for demo (replace with DB or email logic)
submitted_clients = []

# Validation helper function
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.match(r"^\+?[0-9\s\-]{7,15}$", phone)

# POST /api/client/submit
@client_bp.route('/submit', methods=['POST'])
def submit_client():
    data = request.json
    required_fields = [
        "company_name", "contact_name", "email", "phone",
        "service", "description"
    ]

    # Check required fields
    missing = [field for field in required_fields if field not in data or not data[field].strip()]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validate email and phone
    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email address."}), 400
    if not is_valid_phone(data["phone"]):
        return jsonify({"error": "Invalid phone number."}), 400

    # Simulate storing client info
    submitted_clients.append(data)

    # TODO: Send to email / database / CRM
    return jsonify({
        "message": "Client information received successfully.",
        "data": data
    }), 200
