Enter the game by typing your name print:("Type your name to enter")
Welcome. print:("Welcome to The Game of Hope") #+name
print:("Description of FOREST")
print:"Take a moment to check in. Rate your mood right now. 1 (lowest) - 10 (excellent)" 
respond()print:bot replies based on number given
    if user_input <5
        print: ("Sorry to hear your mood is low. Take the journey to see if it changes")
        print: Second forest discription that leads to an option
    else
        print: ("Okay, you are not doing so bad. Take the journey to make it even better")
        print: Second forest discription that leads to an option

#Choosing where to go
Follow the firefly or follow the path (firefly/path)
    if user_input = firefly
    print: ("Description of RIVER")
    options to READ SIGN or SPEAK TO OTTER #"Type otter or read"
    else
    print: ("Description of WATERFALL")
    options to READ SIGN or SPEAK TO TURTULE #"Type turtle or read"

if user chooses READ SIGN get quote from LLM using prompt "Write an inspirational quote that would make someone feel better about life 50 words or less"
if the user chooses otter
respond: otter quote from tuple #random
if the user choses turtle
respond: turtle quote from tuple #random

#Arriving at dawn
print: Description of a beautiful sunset at the trees opening. 
print: ("Check in again. How do you feel 1 to 10?")
    if user_input is higher than original number 
    print: "I'm glad you're feelling better + wrap up text. Come back and replay any time"
    else
        print: "Sorry you're still feeling low + some gentle advice/encouragement"

End game