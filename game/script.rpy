﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Abigail", what_slow_cps=55)
define b = Character("Bianca", what_slow_cps=55)
define c = Character("Clementine",what_slow_cps=55)
define d = Character("Desiree", what_slow_cps=55)
define e = Character("Miss Eileen",what_slow_cps=55)
define n = Character(None, what_slow_cps=55)


# The game starts here.

label splashscreen:
    scene black

    show text "{color=#ffffff}UCLA ACM Studio Presents...{/color}"with dissolve
    with Pause(3)

    scene black with dissolve
    
    show logo with dissolve
    with Pause(3) 

    scene black with dissolve
    with Pause(1)

    return

label start:

    scene black with Pause(1)
    play sound shortschoolbell
    with Pause(4)
    
    scene classroomam with dissolve 
    with Pause(2)

############################## Introduction

    n "The school day begins"

    e "As a teacher, it's my job to guide students towards success."
    e "But art is a tricky subject... I want encourage their creative expression without neglecting the fundamentals."

    show abigail smile
    a "Miss Eileen, I'd like to express my excitement for the upcoming project."

    show abigail speak
    a "I haven't attempted a self-portrait in a long time..."

    show abigail troubled2
    a "...and if I'm being honest, they sort of stress me out. Art takes me long enough as is."

    jump self_portraitA

############################## Self Portrait Grading
label self_portraitA:
    scene teacher_desk
    show abigail portrait

    menu:
        "needs some work":
            jump feedback1_portraitA
        "it's nice...":
            jump feedback2_portraitA
        "looks unfinished":
            jump feedback3_portraitA

label feedback1_portraitA:
    scene teacher_desk
    show abigail portrait f1
    e "This isn't the first time Abigail has submitted incomplete work... such a shame."
    jump self_portraitB

label feedback2_portraitA:
    scene teacher_desk
    show abigail portrait f2
    e "This isn't the first time Abigail has submitted incomplete work... such a shame."
    jump self_portraitB

label feedback3_portraitA:
    scene teacher_desk
    show abigail portrait f3
    e "This isn't the first time Abigail has submitted incomplete work... such a shame."
    jump self_portraitB

label self_portraitB:
    scene teacher_desk
    show bianca portrait

    menu:
        "not a self portrait?":
            jump feedback1_portraitB
        "a character...?":
            jump feedback2_portraitB

label feedback1_portraitB:
    scene teacher_desk
    show bianca portrait f1
    e "Bianca is always taking shortcuts. I wish she'd take the time to learn proper techniques before pulling so much inspiration from the internet."
    jump self_portraitC

label feedback2_portraitB:
    scene teacher_desk
    show bianca portrait f2
    e "Bianca is always taking shortcuts. I wish she'd take the time to learn proper techniques before pulling so much inspiration from the internet."
    jump self_portraitC

label self_portraitC:
    scene teacher_desk
    show clementine portrait

    menu:
        "good effort..":
            jump feedback1_portraitC
        "not what we practiced":
            jump feedback2_portraitC

label feedback1_portraitC:
    scene teacher_desk
    show clementine portrait f1
    e "Clementine is such a nice girl, but she gets so caught up on the details she loses sight of the bigger picture."
    jump self_portraitD

label feedback2_portraitC:
    scene teacher_desk
    show clementine portrait f2
    e "Clementine is such a nice girl, but she gets so caught up on the details she loses sight of the bigger picture."
    jump self_portraitD

label self_portraitD:
    scene teacher_desk
    show desiree portrait

    menu:
        "???":
            jump feedback1_portraitD
        "this is you?":
            jump feedback2_portraitD
        "well, it looks cool":
            jump feedback3_portraitD

label feedback1_portraitD:
    scene teacher_desk
    show desiree portrait f1
    e "I will never understand why Desiree insists on drawing whales for every assignment. Her composition is visually interesting but this is most certainly not a self portrait."
    jump convo1

label feedback2_portraitD:
    scene teacher_desk
    show desiree portrait f2
    e "I will never understand why Desiree insists on drawing whales for every assignment. Her composition is visually interesting but this is most certainly not a self portrait."
    jump convo1

label feedback3_portraitD:
    scene teacher_desk
    show desiree portrait f3
    e "I will never understand why Desiree insists on drawing whales for every assignment. Her composition is visually interesting but this is most certainly not a self portrait."
    jump convo1

    ############################## Self Portrait — Abigail Conversation
label convo1:
    scene classroompm

    show abigail smile
    a "Hi Miss Eileen, I just want to follow up on the feedback I recieved."
    show abigail speak
    a "You said my work felt unfinished, but I received a high grade anyways."

    show abigail neutral
    e "Your work aligned very closely to the provided prompt."

    show abigail troubled1
    a "I know it came out ok,"
    show abigail troubled2
    a "... but I wish it was more, I don't know, personal?"
    show abigail neutral
    a "I was drawing myself, and yet all I could think about was the technique."

    show abigail neutral
    e "Was there something else you were hoping for?"

    show abigail speak
    a "I suppose I expected more self-reflection."
    show abigail frown
    a "My art doesn't feel like my own."

    ############################## Still Life Grading
    
    ############################## Still Life — Bianca Conversation
    scene classroompm

    show bianca speak
    b "Hey teach, it kinda seemed like you had a problem with my art."

    show bianca neutral
    e "I need to see more effort from you. I appreciate your enthusiasm but your technique needs improvement."

    show bianca frown
    b "I actually spent a lot of time on it! And like, we can't all be Abigail."
    show bianca smile
    b "Can you even draw a still-life?"

    e "I demonstrated techniques for painting still lifes on Tuesday. You were absent."

    show bianca neutral
    b "Oh."

    e "You're taking too many shortcuts with your art by referencing others and neglecting the basics."

    show bianca grit
    b "Are you serious?"

    e "Yes, Bianca. But I also believe in you as an artist, and I know you're capable of more if you set your mind to it."

    show bianca serious
    b "Ok. What's next week?"

    e "Scenery. You got this!"

    show bianca smile
    b "Ok teach. See ya on Monday."

    ############################## Scenery Grading

    ############################## Scenery — Clementine Conversation

    scene classroompm

    show clementine neutral
    c "Hey Miss E,"
    show clementine talk
    c "if it's not too much trouble, I was hoping to maybe get some feedback on my scenery work?"

    e "Sure Clementine. I liked what you did with the composition, but the texture felt very flat."

    show clementine frown
    c "I noticed that too,"
    show clementine talk
    c "but I don't really know how to shade..."
    show clementine dejected
    c "... and I didn't want to mess up another piece by trying."

    e "Practice is how you improve! Don't be afraid to take risks."

    show clementine sadsmile
    c "You're right, thanks Miss E."

    e "Clementine, you're an excellent student. Don't sweat it. Just remember that if you stick to what you know, you won't grow."

    show clementine smile
    c "Ok! I'll try something new for my Master Study then. Bye Miss E, I'll see you on Monday!"

    ############################## Master Study Grading

    ############################## Master Study — Desiree Conversation

    scene classroompm

    # This ends the game.

    return
