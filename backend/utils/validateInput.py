import re

# === Email Validator ===
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


# === Phone Number Validator (Kenyan format or international) ===
def is_valid_phone(phone):
    pattern = r'^\+?[0-9]{7,15}$'
    return bool(re.match(pattern, phone))


# === URL Validator (for LinkedIn, social media links) ===
def is_valid_url(url):
    pattern = r'^(http|https):\/\/[^\s]+$'
    return bool(re.match(pattern, url))


# === Full Name Validator (basic check) ===
def is_valid_name(name):
    return bool(name) and len(name.strip().split()) >= 2


# === Non-empty Field ===
def is_non_empty(field):
    return bool(field) and len(field.strip()) > 1


# === Job Seeker Input Validator ===
def validate_job_seeker(data):
    errors = []

    if not is_valid_name(data.get("full_name", "")):
        errors.append("Full name is required and should contain at least 10 words.")
    
    if not is_valid_email(data.get("email", "")):
        errors.append("Invalid email format.")
    
    if not is_valid_phone(data.get("phone", "")):
        errors.append("Invalid phone number.")
    
    linkedin = data.get("linkedin", "")
    if linkedin and not is_valid_url(linkedin):
        errors.append("Invalid LinkedIn URL.")
    
    if not is_non_empty(data.get("experience", "")):
        errors.append("Experience field is required.")
    
    if not is_non_empty(data.get("department", "")):
        errors.append("Department is required.")
    
    return errors


# === Client Input Validator ===
def validate_client(data):
    errors = []

    if not is_non_empty(data.get("company", "")):
        errors.append("Company name is required.")
    
    if not is_valid_name(data.get("contact_name", "")):
        errors.append("Contact full name is required and should have at least 2 names.")
    
    if not is_valid_email(data.get("email", "")):
        errors.append("Invalid email format.")
    
    if not is_valid_phone(data.get("phone", "")):
        errors.append("Invalid phone number.")
    
    if not is_non_empty(data.get("service", "")):
        errors.append("Service field is required.")
    
    if not is_non_empty(data.get("project_description", "")):
        errors.append("Project description is required.")
    
    return errors
