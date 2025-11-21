import random as random
from chatbot_base import ChatbotBase
from generative_ai_instruct import InstructLLMChatbot
import time
import sys
from standard_llm import StandardLLM

class TheGameofHope(ChatbotBase):
    def __init__(self, name="Chatbot"):
        ChatbotBase.__init__(self,name)
        self.user_name = "unknown"
        self.mood = "unknown"
        self.llmbot = InstructLLMChatbot() #if you want your own variable of type InstructLLMChatbot
        self.sllm = StandardLLM()

    
    def type_text(self, text, speed=0.03):
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    # Example of main interaction loop 
    def respond(self):
        if self.user_name == "unknown":
            print("Enter your name to start the game  ")
            user_input = input()
            self.user_name = user_input
            print(f"Hello {user_input}. Welcome to The Game of Hope.") 
            time.sleep(1.5)
            self.type_text("You open your eyes to a soft, golden glow drifting through a canopy of ancient trees. The air is cool and sweet, carrying the scent of moss, wildflowers, and something faintly magical. Dewdrops cling to giant fern leaves, shimmering with iridescent colors. You breathe the fresh air and take in the peaceful sounds of nature.")
        elif self.mood == "unknown":
            time.sleep(1.5)
            print("Take a moment to check in. Rate your mood right now. 1 (lowest) to 10 (excellent)")
            user_input = int(input())
            self.mood = user_input
            if self.mood <= 5:
                print("Sorry to hear your mood is low. Take the journey to see if it changes")
            else:
                print("Okay, you are not doing so bad. Take the journey to make it even better")
                time.sleep(2)  
            self.type_text("The forest is dark and quiet, lit only by the soft glow of a firefly drifting ahead of you. Moonlight barely reaches the forest floor, turning the trees into tall silver shadows. Up ahead, the firefly hovers, waiting. But to your right, a narrow path curves deeper into the woods.")  

        else:
            print("Do you follow the firefly, or take the forest path?") 

            user_input = input().lower()
            
            if user_input.lower() == "firefly":
                self.type_text("You follow the firefly deeper into the forest, its warm glow drifting ahead like a tiny lantern. Gradually, the woods open into a quiet clearing where moonlight spills across the ground, soft and silver. A gentle river winds through the space, its surface shimmering between the trunks as it moves quietly over smooth stones. The air feels cool and peaceful here, the kind of quiet that makes you breathe a little easier.")
                time.sleep(2)
                print("Talk to Otter or Read the sign")
                user_input = input().lower()
                user_input = str(user_input)
                if "otter" in user_input:
                    self.type_text("A small ripple breaks the surface of the lake, followed by a tiny, curious otter popping his head out of the water. His fur glistens like damp velvet, and bright amber eyes blink up at you with gentle excitement. He looks soft, round-cheeked, and undeniably adorable. The kind of creature who seems to smile even when he isn’t trying. With a little plip of water running down his whiskers, he tilts his head, radiating kindness and a shy, playful energy, as if he’s been waiting for someone exactly like you to talk to.") 
                    self.talkToOtter()
                else:
                    self.readSign()
                #no matter whether they talk to the otter or read the sign, they're now both here:



            else:
                self.type_text("You decide to leave the firefly and take the forest path on your own. As soon as you step forward, the ground beneath you glows softly. Smooth stone slabs shimmer into existence, one by one, forming a gentle glowing walkway that guides your steps. Soon, the distant sound of rushing water grows clearer, not booming or frightening, but soothings like a lullaby carried on the night breeze. The path opens into a serene clearing where a moonlit waterfall cascades into a clear pool, mist drifting like silver dust. Beside the water sits a small wooden sign, and near it, a gentle turtle watches you with quiet, welcoming eyes. Peaceful, patient, and happy you’ve arrived.")
                time.sleep(2)
                print("Talk to Turtle or Read the sign")
                user_input = input().lower()
                user_input = str(user_input)
                if "turtle" in user_input:
                    print("The turtle slowly turns his head towards you. He blinks slow, kind eyes at you warm, steady, and full of quiet wisdom as if he’s been expecting you all along.")
                    self.talkToTurtle()
                else:
                    self.readSign()

            self.conversation_is_active = False   
        
    def talkToOtter(self):
        print("Oh wow a visitor! It's so nice to see you here. What brings you to my part of the forest?")
        time.sleep(5)
        self.type_text("The firefly floats beside you and replies")
        print(f"This is {self.user_name}. We'er on a journey today to improve {self.user_name}'s mood.")
        time.sleep(3)
        print("You've come to the right place. Someone came by here not too long ago and told me story that lifted my mood. I'd like to share it with you.")

        self.llmbot.system_prompt = {
            "role": "system",
            "content": 
            "You are a warm, friendly otter who speaks kindly and gently. Your task right now is to tell a short, complete, uplifting storythat makes the user feel hopeful and comforted. Keep it concise and magical. The story must have an ending before the tokens run out"
            "Write 6 to 10 sentences and do not stop early. "
            "Finish the story with a clear ending."
        }
        prompt = "tell the uplifting story with a complete uplifiting ending in 6-8 sentances."
        bot_reply = self.llmbot.respond_with_LLM(prompt)
        self.type_text(bot_reply)
    

    def talkToTurtle(self):
        self.type_text("The turtle speaks softly but firmly...")
        time.sleep(2)
        prompt = "the key to happiness is as follows"

        turtle_reply = self.sllm.generate_response(prompt)
        self.type_text(turtle_reply)

    def readSign(self): 
        quotes = [
            "Since you get more joy out of giving joy to others, you should put a good deal of thought into the happiness that you are able to give. —Eleanor Roosevelt",
            "Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway. ―Earl Nightingale",
            "You alone are enough. You have nothing to prove to anybody. - Maya Angelou",
            "Whenever you find yourself doubting how far you can go, just remember how far you have come. ―Unknown",
            "It is worth remembering that the time of greatest gain in terms of wisdom and inner strength is often that of greatest difficulty. – Dalai Lama",
            "It is those who get lost, who find the new ways. – Nils Kjaer",
            "Good decisions come from experience. Experience comes from making bad decisions. – Mark Twain",
            "There is no such thing as a hopeless situation. Every single circumstance of your life can change. – Ritu Ghatourey"
        ]
 
        sign_quote = random.choice(quotes)
        print(sign_quote) 


if __name__ == "__main__":
    
    memory = TheGameofHope()
    

    while memory.conversation_is_active:
        memory.respond() 