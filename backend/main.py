from flask import Flask, request, jsonify
from flask import Flask, render_template
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)

CORS(app)

# In-memory database (you can replace this with real DB or file storage)
job_seekers = []
clients = []

# Routes
@app.route('/')
def home():
    return jsonify('chatbot.html')

@app.route('/api/job-seeker/submit', methods=['POST'])
def submit_job_seeker():
    data = request.json

    required_fields = ['name', 'email', 'phone', 'linkedin', 'experience', 'department']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    data['timestamp'] = datetime.now().isoformat()
    job_seekers.append(data)

    return jsonify({"message": "Job seeker information received!", "data": data}), 200

@app.route('/api/client/submit', methods=['POST'])
def submit_client():
    data = request.json

    required_fields = ['company', 'contact_name', 'email', 'phone', 'service', 'description']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    data['timestamp'] = datetime.now().isoformat()
    clients.append(data)

    return jsonify({"message": "Client information received!", "data": data}), 200

@app.route('/api/services', methods=['GET'])
def get_services():
    services = [
        "Cloud Migration", "FinOps", "Generative AI Solutions", "Managed Cloud Services", 
        "Microsoft Workloads", "DevOps On The Cloud", "Artificial Intelligence", 
        "Robotic Process Automation", "Chatbot Development", "Digital Agriculture", 
        "Internet Of Things (IoT/Locate 365)", "Virtual Reality", "Public Financial Management", 
        "Digital Identity Management", "Tax & Customs", "e-Government Solutions", 
        "IT Training", "Business Process Outsourcing (BPO)", "Software Engineering", 
        "Systems Integration and Turnkey Solutions"
    ]
    return jsonify({"services": services})

@app.route('/api/employment', methods=['GET'])
def get_employment_requirements():
    requirements = {
        "general": [
            "Bachelor's/Master’s degree in Computer Science, ICT, Engineering, or related fields",
            "Relevant professional certifications",
            "Experience (varies by role)",
            "Strong interpersonal and communication skills",
            "Team collaboration",
            "Proficiency in Microsoft Office & technical tools"
        ],
        "skills": [
            "C#, .NET, ASP.NET, VB.NET, React, Angular, SQL, NoSQL",
            "Test planning, automation, bug tracking, QA fundamentals",
            "Agile (Jira, Azure DevOps), Git, CI/CD",
            "Project management, finance, and sales skills",
            "Computer architecture knowledge"
        ],
        "departments": [
            "Software Engineering", "Cloud Services", "BPO", "Solutions", "Sales & Marketing",
            "QA & Testing", "HR", "Finance", "IT Training", "Project Management"
        ]
    }
    return jsonify(requirements)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
