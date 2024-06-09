from tkinter import *
from tkinter import ttk
class ChatbotWindow:
    def __init__(self,root):
        self.root=root
        self.root.geometry ("700x615")
        self.root.title("Mood_Detector")

         # GUI Styling
        self.BG_GRAY = "#6a7d95"  # Soft blue-gray background
        self.BG_COLOR = "#1F2557"  # Light blue background
        self.TEXT_COLOR = "white"  # Dark text color
        self.FONT = "Helvetica 14"
        self.FONT_BOLD = "Helvetica 13 bold"

        # Emotion detection (for demonstration purposes)
        # Add more empathetic responses for other user inputs here
        self.emotional_responses = {
            "i feel happy": "I'm glad to hear that you're feeling happy! 😊",
            "i feel sad": "I'm sorry to hear that you're feeling sad. How can I help you?",
            "i feel angry": "It's okay to feel angry sometimes. Let's talk about it.",
            "i feel lonely": "I'm here for you. You're not alone. What's going on?",
            "i feel stressed": "I understand that life can be stressful. Take a deep breath. What's bothering you?",
            "i feel excited": "That's fantastic! What's making you feel so excited?",
            "i feel calm": "It sounds like you're feeling calm. Is there anything specific on your mind?",
            "i feel confused": "It's okay to feel confused. Let's work together to clear things up.",
            "i feel loved": "Feeling loved is wonderful! Who or what is bringing joy to your life?",
            "i feel motivated": "Great to hear you're feeling motivated! What inspired you?",
            "i feel fearful": "I hear you're feeling fearful. It's okay; we can talk through your fears together.",
            "i feel grateful": "Expressing gratitude is a beautiful thing! What are you thankful for today?",
            "i feel hopeful": "Maintaining hope is important. What are you hopeful for in the near future?",
            "i feel proud": "Feeling proud is an accomplishment! What have you achieved that makes you proud?",
            "i feel curious": "Curiosity is a wonderful trait! What are you curious about right now?",
            "i feel relieved": "I'm glad to hear you're feeling relieved. What brought you a sense of relief?",
            "i feel inspired": "Inspiration is a powerful force! What or who inspired you recently?",
            "i feel hopeless": "Feeling hopeless is tough. Let's explore together and find a way to bring hope back.",
            "i feel overwhelmed": "Being overwhelmed is a common feeling. What's overwhelming you right now?",
            "i feel isolated": "Feeling isolated can be challenging. I'm here to provide support. What's going on?",
            "i feel numb": "If you're feeling numb, it's okay. Let's work together to understand and address these emotions.",
            "i feel empty": "Feeling empty is difficult. Can you share more about what might be contributing to this feeling?",
            "i feel worthless": "You are not worthless. Your feelings are valid, and I'm here to listen and support you.",
            "i feel fatigue": "Fatigue can impact both the body and mind. What's been draining your energy?",
            "i feel disconnected": "Feeling disconnected is tough. Let's talk about what might be causing this disconnect.",
            "i feel unmotivated": "Lack of motivation is a common struggle. What's been making it hard to find motivation?",
            "i feel despair": "If you're feeling despair, I'm here to provide support. You don't have to face it alone.",
            "i feel guilt": "Guilt can weigh heavily on the mind. Let's explore these feelings and find ways to cope.",
            "i feel depressed": "Feeling depressed is tough. What positive changes can we make, even small ones, to improve your mood?",
            "i feel suicidal": "I'm really sorry to hear that you're feeling this way, but I can't provide the help that you need. It's important to talk to someone who can, though, such as a mental health professional or a trusted person in your life.",
            "what about you?": "me? im just a bot, got no  emotions :')",
            "what about you??": "me? im just a bot, got no  emotions :')",
            "what about you???": "me? im just a bot, got no  emotions :')",
            "happy": "I'm glad to hear that you're feeling happy! 😊",
            "sad": "I'm sorry to hear that you're feeling sad. How can I help you?",
            "angry": "It's okay to feel angry sometimes. Let's talk about it.",
            "lonely": "I'm here for you. You're not alone. What's going on?",
            "stressed": "I understand that life can be stressful. Take a deep breath. What's bothering you?",
            "excited": "That's fantastic! What's making you feel so excited?",
            "calm": "It sounds like you're feeling calm. Is there anything specific on your mind?",
            "confused": "It's okay to feel confused. Let's work together to clear things up.",
            "loved": "Feeling loved is wonderful! Who or what is bringing joy to your life?",
            "motivated": "Great to hear you're feeling motivated! What inspired you?",
            "fearful": "I hear you're feeling fearful. It's okay; we can talk through your fears together.",
            "grateful": "Expressing gratitude is a beautiful thing! What are you thankful for today?",
            "hopeful": "Maintaining hope is important. What are you hopeful for in the near future?",
            "proud": "Feeling proud is an accomplishment! What have you achieved that makes you proud?",
            "curious": "Curiosity is a wonderful trait! What are you curious about right now?",
            "relieved": "I'm glad to hear you're feeling relieved. What brought you a sense of relief?",
            "inspired": "Inspiration is a powerful force! What or who inspired you recently?",
            "hopeless": "Feeling hopeless is tough. Let's explore together and find a way to bring hope back.",
            "overwhelmed": "Being overwhelmed is a common feeling. What's overwhelming you right now?",
            "isolated": "Feeling isolated can be challenging. I'm here to provide support. What's going on?",
            "numb": "If you're feeling numb, it's okay. Let's work together to understand and address these emotions.",
            "empty": "Feeling empty is difficult. Can you share more about what might be contributing to this feeling?",
            "worthless": "You are not worthless. Your feelings are valid, and I'm here to listen and support you.",
            "fatigue": "Fatigue can impact both the body and mind. What's been draining your energy?",
            "disconnected": "Feeling disconnected is tough. Let's talk about what might be causing this disconnect.",
            "unmotivated": "Lack of motivation is a common struggle. What's been making it hard to find motivation?",
            "despair": "If you're feeling despair, I'm here to provide support. You don't have to face it alone.",
            "guilt": "Guilt can weigh heavily on the mind. Let's explore these feelings and find ways to cope.",
            "depressed": "Feeling depressed is tough. What positive changes can we make, even small ones, to improve your mood?",
            "suicidal": "I'm really sorry to hear that you're feeling this way, but I can't provide the help that you need. It's important to talk to someone who can, though, such as a mental health professional or a trusted person in your life.",
            "hello": "Hello! How can I support you today?",
            "hi": "Hi there! What's on your mind?",
            "how are you": "I'm here to listen. How are you feeling? (respond: i feel...?)",
            "i feel good":"Thats good to hear :)",
            "who are you": "I am a therapy bot made by Sulthana, a Third-year B.Eng \n computer system student at Middlesex University Dubai"
        }

        self.label1 = Label(self.root, bg="white", fg="black", text="Chat Bot",
                            font=self.FONT_BOLD, pady=10, width=60, height=1)
        self.label1.grid(row=0)

        self.txt = Text(self.root, bg="white", fg=self.BG_COLOR, font=self.FONT, width=60)
        self.txt.grid(row=1, column=0, columnspan=2)
        self.scrollbar = Scrollbar(self.txt)
        self.scrollbar.place(relheight=1, relx=0.974)

        self.entry = Entry(self.root, bg=self.BG_GRAY, fg=self.TEXT_COLOR, font=self.FONT, width=55)
        self.entry.grid(row=2, column=0)

        self.send_button = Button(self.root, text="Send ♡", font=self.FONT_BOLD,fg=self.TEXT_COLOR, bg=self.BG_GRAY, command=self.send)
        self.send_button.grid(row=2, column=1)

        self.root.mainloop()

    def send(self):
        user_input = self.entry.get().lower()
        response = ""

        for emotion, trigger_phrases in self.emotional_responses.items():
            if emotion in user_input:
                response = self.emotional_responses[emotion]
                break

        if not response:
            # If no emotion trigger is found, use default responses
            if user_input == "hello":
                response = "Hello! How can I support you today?"
            elif user_input in ["hi", "hii", "hiiii"]:
                response = "Hi there! What's on your mind?"
            elif user_input == "how are you":
                response = "I'm here to listen. How are you feeling? (respond: i feel...?)"
            elif user_input in ["who are you", "what are you", "who created you", "whats your purpose",
                                "Can you tell me a little bit about yourself?", "What's your name?", "Tell me your name.",
                                "Please introduce yourself.", "Who made you?", "Who built you?", "Who programmed you?"]:
                response = "i am a therapy bot made by sulthana, third year b.eng computer system student"
            else:
                response = "im not sure i understand but Tell me more bout it."

        # Display the bot's response
        self.txt.insert(END, "\nYou -> " + self.entry.get())
        self.txt.insert(END, "\n 🤖 -> " + response)
        self.entry.delete(0, END)

# Create an instance of the Chatbot class


 


if __name__ == "__main__":
    root = Tk()
    obj = ChatbotWindow(root)
    root.protocol("WM_DELETE_WINDOW", obj.on_closing)
    root.mainloop()