import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from chatbot_base import ChatbotBase

#print("Enter your name to start the game")
user_name = input("Enter your name to start the game  ")
print(f"Hello {user_name}. Welcome to The Game of Hope. You open your eyes to a soft, golden glow drifting through a canopy of ancient trees. The air is cool and sweet, carrying the scent of moss, wildflowers, and something faintly magical. Dewdrops cling to giant fern leaves, shimmering with iridescent colors. You breathe the fresh air and take in the peaceful sounds of nature.")
#print("Take a moment to check in. Rate your mood right now. 1 (lowest) to 10 (excellent)")
user_input = input("How are you feeling?")
user_is_upset = str(user_input)

def user_is_upset(user_input):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(user_input)

    if sentiment_scores["neg"] > 0.5:
        return True
    else:
        return False

user_is_upset("sad times")
print("sorry to hear that")