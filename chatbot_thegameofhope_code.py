import random as random
from chatbot_base import ChatbotBase
from generative_ai_instruct import InstructLLMChatbot

class TheGameofHope(ChatbotBase):
    def __init__(self, name="Chatbot"):
        ChatbotBase.__init__(self,name)
        self.user_name = "unknown"
        self.mood = "unknown"
        self.llm = InstructLLMChatbot(device="cpu")

    
    # Example of main interaction loop 
    def respond(self):
        if self.user_name == "unknown":
            print("Enter your name to start the game  ")
            user_input = input()
            self.user_name = user_input
            print(f"Hello {user_input}. Welcome to The Game of Hope. You open your eyes to a soft, golden glow drifting through a canopy of ancient trees. The air is cool and sweet, carrying the scent of moss, wildflowers, and something faintly magical. Dewdrops cling to giant fern leaves, shimmering with iridescent colors. You breathe the fresh air and take in the peaceful sounds of nature.")
        elif self.mood == "unknown":
            print("Take a moment to check in. Rate your mood right now. 1 (lowest) to 10 (excellent)")
            user_input = int(input())
            self.mood = user_input
            if self.mood <= 5:
                print("Sorry to hear that")
            else:
                print("That's great. Start your journey")  
            print("SECOND FOREST DESCRIPTION")  

        else:
            print("Firefly desciption option for path or firefly") 

            user_input = input()
            
            if user_input == "firefly":
                print("Description of RIVER - options 'Talk to Otter' or ' Read Sign'")
                user_input = str(user_input)

            else:
                print("Description of WATERFALL - with options")

            self.conversation_is_active = False   
        

    
if __name__ == "__main__":
    
    memory = TheGameofHope()
    

    while memory.conversation_is_active:
        memory.respond()