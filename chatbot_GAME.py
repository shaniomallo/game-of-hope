from chatbot_base import ChatbotBase

#print("Enter your name to start the game")
user_name = input("Enter your name to start the game  ")
print(f"Hello {user_name}. Welcome to The Game of Hope. You open your eyes to a soft, golden glow drifting through a canopy of ancient trees. The air is cool and sweet, carrying the scent of moss, wildflowers, and something faintly magical. Dewdrops cling to giant fern leaves, shimmering with iridescent colors. You breathe the fresh air and take in the peaceful sounds of nature.")
#print("Take a moment to check in. Rate your mood right now. 1 (lowest) to 10 (excellent)")
user_input = input("Take a moment to check in. Rate your mood right now. 1 (lowest) to 10 (excellent)")
mood = int(user_input)
#low_mood = <5
#high_mood = >5
if mood <= 5:
    print("Sorry to hear that")
else:
    print("That's great. Start your journey")  
print("SECOND FOREST DESCRIPTION - include firefly arival")          


# Jo's example

class ChatbotBase:
    x = 54

class GameInterface:
    y = 66


class GameOfHope(ChatbotBase, GameInterface):
    z = 14




class GameOfHope(ChatbotBase, GameInterface):
    name: str
    mood: str
    x: int

    def __init__(self, x):
        self.x = x


    def get_name(self):
        pass

    def get_mood(self):
        pass

    def game_play(self):
        pass






game_of_hope = GameOfHope(x=)












class ChatbotBase:
    # Constructor 
    def __init__(self, name="Chatbot"):
        self.name = name
        self.conversation_is_active = True

    # Initial greeting message
    def greeting(self):
        print(f'Hello I am {self.name}')

    # Goodbye message
    def farewell(self):
        print('Goodbye!')
    
    # Return true if conversation is active
    def conversation_is_active(self):
        return self.conversation_is_active

    # Take user input from terminal
    def receive_input(self):
        user_input = input()
        return user_input

    # Take user input and do something with it 
    def process_input(self, user_input):
        raise NotImplementedError('process_input() not implemented in base Chatbot class')

    # Generate a text string and return it
    def generate_response(self, processed_input):
        raise NotImplementedError('generate_response() not implemented in base Chatbot class')

    # Example of main interaction loop 
    # Override this or write other function that handle more complex user interactions
    def respond(self, out_message = None):
        if isinstance(out_message, str): 
            print(out_message)

        received_input = self.receive_input()
        processed_input = self.process_input(received_input)
        response = self.generate_response(processed_input)
        return response
    