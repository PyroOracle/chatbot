# InputBox.py

from typing import Dict


class InputBoxHandler:
    def __init__(self):
        self.state = {}
        self.job_seeker_questions = [
            "What is your full name?",
            "What is your email address?",
            "What is your phone number?",
            "What is your LinkedIn profile URL?",
            "How many years of work experience do you have?",
            "Which department would you like to work in?",
            "Please email your resume to careers@example.com with subject 'Chatbot Application - [Your Name]'"
        ]

        self.client_questions = [
            "What is your company name?",
            "What is your full name (Contact Person)?",
            "What is your email address?",
            "What is your phone number?",
            "What service are you interested in?",
            "Please describe your project or needs in detail."
        ]

    def start_conversation(self, user_type: str):
        self.state['user_type'] = user_type
        self.state['step'] = 0
        self.state['data'] = {}
        return self.get_next_question()

    def get_next_question(self):
        user_type = self.state.get('user_type')
        step = self.state.get('step', 0)

        if user_type == "job":
            if step < len(self.job_seeker_questions):
                return self.job_seeker_questions[step]
            else:
                return "✅ Thank you! Your application has been noted. Would you like to learn about our services or employment requirements?"
        elif user_type == "client":
            if step < len(self.client_questions):
                return self.client_questions[step]
            else:
                return "✅ Thank you! Our sales team will get in touch with you soon. Would you like more details about our services?"
        else:
            return "Are you a job seeker or a client?"

    def process_input(self, user_input: str):
        user_type = self.state.get('user_type')
        step = self.state.get('step', 0)

        if 'data' not in self.state:
            self.state['data'] = {}

        key = f"step_{step}"
        self.state['data'][key] = user_input
        self.state['step'] += 1

        return self.get_next_question()

    def get_collected_data(self) -> Dict:
        return self.state.get('data', {})
