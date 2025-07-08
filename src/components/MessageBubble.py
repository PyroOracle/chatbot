# MessageBubble.py

from datetime import datetime

class MessageBubble:
    def __init__(self, sender, message):
        """
        sender: str - 'bot' or 'user'
        message: str - the content of the message
        """
        self.sender = sender
        self.message = message
        self.timestamp = datetime.now()

    def render_template(self):
        """
        Returns the HTML string for rendering the message bubble.
        """
        bubble_class = "bot-message" if self.sender == "bot" else "user-message"
        align_style = "text-align:left;" if self.sender == "bot" else "text-align:right;"
        bg_color = "#e3f2fd" if self.sender == "bot" else "#dcedc8"

        return f"""
        <div class="{bubble_class}" style="{align_style}; background-color: {bg_color}; 
            margin: 10px 0; padding: 10px; border-radius: 8px; max-width: 90%;">
            <small><i>{self.timestamp.strftime('%H:%M')}</i></small><br/>
            {self.message}
        </div>
        """

    def render_json(self):
        """
        Returns a dictionary for use in APIs or front-end rendering.
        """
        return {
            "sender": self.sender,
            "message": self.message,
            "timestamp": self.timestamp.isoformat()
        }

# Example usage:
if __name__ == "__main__":
    bot_reply = MessageBubble("bot", "Hello! I'm TechnoBot. Are you a Job Seeker or a Client?")
    user_reply = MessageBubble("user", "I am a client.")

    print(bot_reply.render_template())
    print(user_reply.render_template())

    print(bot_reply.render_json())
    print(user_reply.render_json())
