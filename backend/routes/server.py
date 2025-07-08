from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Allow requests from the front-end

# ----------------------
# Sample In-Memory Stores
# ----------------------
job_seekers = []
clients = []

# ----------------------
# Routes
# ----------------------

@app.route("/")
def home():
    return jsonify({"message": "TechnoBot API is running."})


# 1. JOB SEEKER SUBMISSION
@app.route("/api/job-seeker/submit", methods=["POST"])
def submit_job_seeker():
    data = request.json

    required_fields = [
        "name", "email", "phone", "linkedin",
        "experience", "department"
    ]

    # Check required fields
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    data["timestamp"] = datetime.datetime.utcnow().isoformat()
    job_seekers.append(data)  # In real usage, store in DB
    print(f"[JOB SEEKER] {data['name']} submitted an application.")

    return jsonify({"message": "Application submitted successfully!"})


# 2. CLIENT SERVICE REQUEST
@app.route("/api/client/submit", methods=["POST"])
def submit_client():
    data = request.json

    required_fields = [
        "company", "contact_name", "email",
        "phone", "service", "description"
    ]

    # Check required fields
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    data["timestamp"] = datetime.datetime.utcnow().isoformat()
    clients.append(data)  # In real usage, store in DB
    print(f"[CLIENT] {data['company']} requested service: {data['service']}")

    return jsonify({"message": "Service request submitted successfully!"})


# ----------------------
# Run Server
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
