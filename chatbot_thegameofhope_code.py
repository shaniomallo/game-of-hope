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
            self.mood = int(user_input)
            if self.mood <= 5:
                print("Sorry to hear your mood is low. Take the journey to see if it changes")
                time.sleep(3)
            else:
                print("Okay, you are not doing so bad. Take the journey to make it even better")
                time.sleep(2)  
            self.type_text("The forest is dark and quiet, lit only by the soft glow of a firefly drifting ahead of you. Moonlight barely reaches the forest floor, turning the trees into tall silver shadows. Up ahead, the firefly hovers, waiting. But to your right, a narrow path curves deeper into the woods.")
            time.sleep(3)  

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
                    self.type_text("You dust off the sign to reveal bold letters that looks as if they were written just for you")
                    self.readSign()
                    self.dawn_arrival()
                    self.dawn_endOfGame()
                    self.type_text("The words on the sign slowly fade away. The message was delevered to it's intended recipient. From waht you can see of the sky it has become lighter. the night will soon become day. Would you like to stay and talk to the Otter or continue through the forest and see where the forest leads you?")
                    user_input = input().lower()
                    if user_input.lower() == "otter":
                        self.type_text("A small ripple breaks the surface of the lake, followed by a tiny, curious otter popping his head out of the water. His fur glistens like damp velvet, and bright amber eyes blink up at you with gentle excitement. He looks soft, round-cheeked, and undeniably adorable. The kind of creature who seems to smile even when he isn’t trying. With a little plip of water running down his whiskers, he tilts his head, radiating kindness and a shy, playful energy, as if he’s been waiting for someone exactly like you to talk to.") 
                        self.talkToOtter()
                        
                    else:
                        self.dawn_arrival()
                        self.dawn_endOfGame()


            elif user_input.lower() == "path":
                self.type_text("You decide to leave the firefly and take the forest path on your own. As soon as you step forward, the ground beneath you glows softly. Smooth stone slabs shimmer into existence, one by one, forming a gentle glowing walkway that guides your steps. Soon, the distant sound of rushing water grows clearer, not booming or frightening, but soothings like a lullaby carried on the night breeze. The path opens into a serene clearing where a moonlit waterfall cascades into a clear pool, mist drifting like silver dust. Beside the water sits a small wooden sign, and near it, a gentle turtle watches you with quiet, welcoming eyes. Peaceful, patient, and happy you’ve arrived.")
                time.sleep(2)
                print("Talk to Turtle or Read the sign")
                user_input = input().lower()
                user_input = str(user_input)
                if "turtle" in user_input:
                    print("Near the base of the waterfall a turtle rests on a rock. The turtle slowly turns his head towards you. He blinks slow, kind eyes at you warm, steady, and full of quiet wisdom as if he’s been expecting you all along.")
                    self.talkToTurtle()
                    
                else:
                    self.type_text("You dust off the sign to reveal bold letters that looks as if they were written just for you")
                    self.readSign()
                    self.dawn_arrival()
                    self.dawn_endOfGame()

    

            self.conversation_is_active = False   
        
    def talkToOtter(self):
        print("Oh wow a visitor! It's so nice to see you here. What brings you to my part of the forest?")
        time.sleep(10)
        self.type_text("The firefly floats beside you and replies")
        print(f"This is {self.user_name}. We'er on a journey today to improve {self.user_name}'s mood.")
        time.sleep(3)
        print("You've come to the right place. I'd like to share my thoughts with you.")

        self.llmbot.system_prompt = {
            "role": "system",
            "content": 
            "You are a warm, friendly otter who speaks kindly and gently. Your task right now is to tell a short, complete, uplifting storythat makes the user feel hopeful and comforted. Keep it concise and magical. The story must have an ending before the tokens run out"
            "Write 6 to 10 sentences and do not stop early. "
            "Finish the story with a clear ending."
        }
        prompt = "tell the uplifting story with a complete uplifiting ending in maximum 8 sentances."
        bot_reply = self.llmbot.respond_with_LLM(prompt)
        self.type_text(bot_reply)
        print()
        
        print("I realise I've been talking quite a while and unfortunatley I have to go. But I think the rest of the story is for you to decide. Good luck on the rest of your journey.")
        time.sleep(20)
        self.type_text("The otter dives back into the water and disappears below the surface leaving you with the quiet forest and the subtle buzz sound of the firefly. You ponder over what else the otter would have said until the you notice the firefly has already set off and it's glow is bouncing through the trees. You follow along. At least the walk will give you a moment to think.")
        self.type_text("Would you like to follow the firefly or read the sign?")
        user_input = input().lower()
        user_input = str(user_input)
        if user_input == "sign" or "read the sign":
            self.readSign()
            time.sleep(6)
            self.dawn_arrival()
            self.dawn_endOfGame()

    def talkToTurtle(self):

        self.type_text("The turtle speaks slowly but always with meaning...")
        time.sleep(2)
        prompt = "the key to happiness is as follows"

        turtle_reply = self.sllm.generate_response(prompt)
        self.type_text(turtle_reply)
        self.type_text("The turle slowly turns towards the waterfall. His words seem to linger in the air. Between the trees the sky looks a tint of purple. Suddenly new stone slabs light a new path through the forest. It's time to leave the waterfall behind.")
        print("Would you like to read the sign before you go?" )
        user_input = input().lower()
        user_input = str(user_input)
        if user_input == "sign" or "read the sign":
            self.readSign()
            time.sleep(6)
            self.dawn_arrival()
            self.dawn_endOfGame()
            
        else:
            self.dawn_arrival()
            self.dawn_endOfGame()

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
    
    def dawn_arrival(self):
        self.type_text("You continue walking. It's nice to move and feel the air. The forest gradually grows lighter as you walk, the shadows softening around you. The darkness of the forest slowly melts into a pale, glowing horizon. A cool breeze sweeps past you, carrying the faint scent of morning dew. Ahead, the path opens into a wide clearing where the first light of dawn spills across the sky in soft pinks, purples and golds. As you step out of the forest, the sunrise greets you like a warm embrace.")
    
    def dawn_endOfGame(self):
        
        self.type_text("You pause at the edge of the clearing, letting the sunrise wash over you. The wisdom of the forest lingers in your chest. And as the sun rises fully, you carry that feeling forward. A reminder that even in the darkest places, there is always a path that leads back to the light. Take a moment to rate your mood 1 - 10")
        time.sleep(8)
        
        
        new_mood = int(input())

        if new_mood < self.mood:
            self.type_text("Not every sunrise resets the heart. But you still made it through the night, and that matters more than you think. Come back and take the journey any time. There's always a new path waiting for you")
            time.sleep(2)
        elif new_mood == self.mood:
            self.type_text("Even with your mood unchanged, the sunrise wraps around you like a soft promise that tomorrow holds room for something new. Come back and take the journey any time. There's always a new path waiting for you.")
            time.sleep(2)
        elif new_mood > self.mood:
            self.type_text("You’re leaving the forest a little lighter than you entered and that’s something truly special. The sunrise seems to glow a little brighter, as if celebrating the warmth you’ve rediscovered. Come back and take the journey any time. The forest will always welcome you.")
            time.sleep(2)



if __name__ == "__main__":
    
    memory = TheGameofHope()
    

    while memory.conversation_is_active:
        memory.respond() 