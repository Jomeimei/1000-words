# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Abigail")
define b = Character("Bianca")
define c = Character("Clementine")
define d = Character("Desiree")


# The game starts here.

label start:

    scene classroom

    # Introduction

    show abigail smile
    a "Teacher, I'd like to express my excitement for the upcoming project."

    show abigail speak
    a "I haven't attempted a self-portrait in a long time..."

    show abigail troubled2
    a "...and if I'm being honest, they sort of stress me out. Art takes me long enough as is."

    # Self Portrait Grading
    
    # scene teacher_desk


    # Self Portrait — Abigail Conversation

    scene classroom

    show abigail neutral
    a "Hi Teacher, I just want to follow up on the feedback I recieved."
    show abigail speak
    a "You said my work felt unfinished, but I received a high grade anyways."

    # Teacher: Your work aligned very closely to the provided prompt.

    show abigail troubled1
    a "I know it came out ok,"
    show abigail troubled2
    a "... but I wish it was more, I don't know, personal?"
    show abigail neutral
    a "I was drawing myself, and yet all I could think about was the technique."

    # Teacher: Was there something else you were hoping for?

    show abigail speak
    a "I suppose I expected more self-reflection."
    show abigail frown
    a "My art doesn't feel like my own."

    # Still Life Grading
    
    # Still Life — Bianca Conversation
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

    # Scenery Grading

    # Scenery — Clementine Conversaion

    # Master Study Grading

    # Master Study — Desiree Conversation

    # This ends the game.

    return
