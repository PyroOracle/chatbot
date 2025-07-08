from flask import Flask, request, jsonify
from datetime import datetime
import smtplib
import os

app = Flask(__name__)

# In-memory storage for demo (can replace with database)
job_seekers = []
clients = []

@app.route('/')
def home():
    return "🤖 TechnoBot Backend is Running."

# ----------------------
# JOB SEEKER SUBMISSION
# ----------------------
@app.route('/submit-jobseeker', methods=['POST'])
def submit_jobseeker():
    data = request.json

    required_fields = ['name', 'email', 'phone', 'linkedin', 'experience', 'department']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    job_seekers.append({
        'timestamp': datetime.now().isoformat(),
        **data
    })

    # Optionally: Send email or save to file/db
    print(f"[JobSeeker] Data Received: {data['name']}")

    return jsonify({'message': 'Job seeker info received successfully!'}), 200

# -------------------
# CLIENT SUBMISSION
# -------------------
@app.route('/submit-client', methods=['POST'])
def submit_client():
    data = request.json

    required_fields = ['company', 'contact_name', 'email', 'phone', 'service', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    clients.append({
        'timestamp': datetime.now().isoformat(),
        **data
    })

    # Optionally: Send email or store
    print(f"[Client] Project Request from {data['company']}")

    return jsonify({'message': 'Client info received successfully!'}), 200

# --------------------------
# ADMIN ENDPOINT (Optional)
# --------------------------
@app.route('/admin/jobseekers', methods=['GET'])
def list_job_seekers():
    return jsonify(job_seekers)

@app.route('/admin/clients', methods=['GET'])
def list_clients():
    return jsonify(clients)

# -------------------------
# RUN THE FLASK SERVER
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
