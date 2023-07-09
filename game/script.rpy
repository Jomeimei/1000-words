# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Abigail")
define b = Character("Bianca")
define c = Character("Clementine")
define d = Character("Desiree")
define e = Character(None, window_background="gui/player_textbox.png")


# The game starts here.

label start:

    scene classroom

    ############################## Introduction

    show abigail smile
    a "Miss E, I'd like to express my excitement for the upcoming project."

    show abigail speak
    a "I haven't attempted a self-portrait in a long time..."

    show abigail troubled2
    a "...and if I'm being honest, they sort of stress me out. Art takes me long enough as is."

    ############################## Self Portrait Grading
    
    # scene teacher_desk


    ############################## Self Portrait — Abigail Conversation

    scene classroom

    show abigail neutral
    a "Hi Miss E, I just want to follow up on the feedback I recieved."
    show abigail speak
    a "You said my work felt unfinished, but I received a high grade anyways."

    e "(Your work aligned very closely to the provided prompt.)"

    show abigail troubled1
    a "I know it came out ok,"
    show abigail troubled2
    a "... but I wish it was more, I don't know, personal?"
    show abigail neutral
    a "I was drawing myself, and yet all I could think about was the technique."

    e "(Was there something else you were hoping for?)"

    show abigail speak
    a "I suppose I expected more self-reflection."
    show abigail frown
    a "My art doesn't feel like my own."

    ############################## Still Life Grading
    
    ############################## Still Life — Bianca Conversation
    scene classroom

    show bianca speak
    b "Hey teach, it kinda seemed like you had a problem with my art."

    # Teacher: I need to see more effort from you. I appreciate your enthusiasm but your technique needs improvement.

    show bianca frown
    b "I actually spent a lot of time on it! And like, we can't all be Abigail."
    show bianca smile
    b "Can you even draw a still-life?"

    # Teacher: I demonstrated techniques for painting still lifes on Tuesday. You were absent.

    show bianca neutral
    b "Oh."

    # Teacher: You're taking too many shortcuts with your art by referencing others and neglecting the basics.

    show bianca grit
    b "Are you serious?"

    # Teacher: Yes, Bianca. But I also believe in you as an artist, and I know you're capable of more if you set your mind to it.
    show bianca serious
    b "Ok. What's next week?"

    # Teacher: Scenery. You got this!

    show bianca smile
    b "Ok teach. See ya on Monday."

    ############################## Scenery Grading

    ############################## Scenery — Clementine Conversation

    scene classroom

    show clementine neutral
    c "Hey Miss E,"
    show clementine talk
    c "if it's not too much trouble, I was hoping to maybe get some feedback on my scenery work?"

    # Teacher: Sure Clementine. I liked what you did with the composition, but the texture felt very flat.

    show clementine frown
    c "I noticed that too,"
    show clementine talk
    c "but I don't really know how to shade..."
    show clementine dejected
    c "... and I didn't want to mess up another piece by trying."

    # Teacher: Practice is how you improve! Don't be afraid to take risks.

    show clementine sadsmile
    c "You're right, thanks Miss E."

    # Teacher: Clementine, you're an excellent student. Don't sweat it. Just remember that if you stick to what you know, you won't grow.

    show clementine smile
    c "Ok! I'll try something new for my Master Study then. Bye Miss E, I'll see you on Monday!"

    ############################## Master Study Grading

    ############################## Master Study — Desiree Conversation

    scene classroom

    # This ends the game.

    return
