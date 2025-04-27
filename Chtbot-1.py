import random

class MoodAnalyzer:
    def __init__(self, user_input):
        self.user_input = user_input.lower()

    def analyze_mood(self):
        """Analyzes user input and returns a mood."""
        if "happy" in self.user_input or "good" in self.user_input or "excited" in self.user_input:
            return "happy"
        elif "sad" in self.user_input or "depressed" in self.user_input or "down" in self.user_input:
            return "sad"
        elif "angry" in self.user_input or "mad" in self.user_input or "furious" in self.user_input:
            return "angry"
        elif "bored" in self.user_input or "tired" in self.user_input:
            return "bored"
        else:
            return "neutral"

class CrazyMoodChatbot:
    def __init__(self):
        self.sarcastic_responses = {
            "happy": ["Oh, wow, you're happy? That’s so rare!", "Wow, someone’s having a good day. Can I borrow some of that energy?"],
            "sad": ["Feeling sad? How shocking... Not.", "Oh, you're sad? I thought the world was just one big rainbow!"],
            "angry": ["Angry, huh? Well, calm down before you break something!", "Someone’s temper is as hot as a boiling kettle!"],
            "bored": ["Bored? Why don’t you try a hobby, like throwing spaghetti at the wall?", "How about taking a nap? Or better yet, both!"],
            "neutral": ["Neutral? What’s that like? A life of complete indifference? Meh.", "You're as neutral as Switzerland right now!"]
        }
        self.random_events = ["Oops! Something just broke! 🤦", "A wild pigeon flies by! 🕊️", "A robot just tried to take over the world! 🤖"]
        self.user_mood_history = {}  
    def mood_response(self, mood):
        """Responds to the user's mood with sarcasm or humor."""
        return random.choice(self.sarcastic_responses.get(mood, ["Hmm, that's interesting."]))

    def random_event(self):
        """Randomly trigger an event."""
        if random.choice([True, False]):
            print(random.choice(self.random_events))
            return True
        return False

    def remember_user_mood(self, user_name, mood):
        """Remembers user's mood over time."""
        self.user_mood_history[user_name] = mood
        print(f"Remembering your mood: {mood} for {user_name}.")

    def greet_user(self, user_name):
        """Greets the user, remembering their previous mood."""
        if user_name in self.user_mood_history:
            print(f"Welcome back, {user_name}! Last time you were feeling {self.user_mood_history[user_name]}!")
        else:
            print(f"Hello, {user_name}! How are you feeling today?")

    def interact(self):
        """Starts the chatbot interaction with the user."""
        user_name = input("What's your name? ")
        self.greet_user(user_name)

        while True:
            user_input = input(f"How are you feeling today, {user_name}? ")

            if user_input.lower() == "exit":
                print("Goodbye! Stay weird. 😜")
                break

            analyzer = MoodAnalyzer(user_input)
            mood = analyzer.analyze_mood()

           
            self.remember_user_mood(user_name, mood)

            if self.random_event():
                continue

            response = self.mood_response(mood)
            print(response)

class CrazyMoodChatbotWithMemory(CrazyMoodChatbot):
    def __init__(self):
        super().__init__()

    def greet_user(self, user_name):
        """Greets the user and remembers their previous mood."""
        if user_name in self.user_mood_history:
            print(f"Welcome back, {user_name}! Last time you were feeling {self.user_mood_history[user_name]}.")
        else:
            print(f"Hello, {user_name}! How are you feeling today?")

# Start the chatbot
if __name__ == "__main__":
    chatbot = CrazyMoodChatbotWithMemory()
    chatbot.interact()
