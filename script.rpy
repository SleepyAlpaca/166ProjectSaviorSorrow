# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aayush") #brother/ghost
define i = Character("Idhant") #mc
define f = Character("Ajay") #father
define m = Character("Alia") #mother


# The game starts here.

label start:
    scene bg house1
    show idhant i
    "CHAPTER 1"
    "My name is Idhant."
    "I live in New Delhi, a rising utopian city in India. The people here live in harmony and are trusting of one another to a fault."
    "There is a place for everyone resulting in a nonexistent crime rate, I love my city."
    "I work in my family pharmaceutical business."
    i "Finally I'm home. It's tiring standing for so long without rest, good thing the people here live a clean life so there weren't many customers."
    i "Looks like father and mother went out for their daily walks. With no crime in this city, I don't really have to worry about their wellbeing outside the house despite them being so old now."

    scene bg bedroom
    show Idhant i

    "*After washing my face, I headed to my bedroom.*"
    i "*sigh* huuuup, my legs are so sore, I could go for a good nap right now."
    "*I lay down on my bed about to drift off to my dream wonderland but a sudden thought pulled me back to reality.*"
    i "I almost forget to pray today. If mother found out, she'll be mad and I don't want to lie to her about it. *sigh* You have to do what you have to do, I'll just make it a quick prayer."


    scene bg prayroom
    show Idhant i

    "*I started doing my usual prayer but when I finish, I see something I've never saw during my other praying sessions.*"
    i "Why is there a broken amulet? Why did it suddenly appear? Did mother accidentally leave this here? No that can't be right I would've seen it as a I walked in. Hmm, strange."
    "*I place my hand on the amulet bringing it in for closer inspection.*"

    scene bg famaly_photo
    with Dissolve(.5)

    pause .5

    m "Smile!" #(Taking family photos)
    "*A quick camera flash goes off*"

    scene bg prayroom
    show Idhant i

    i "Huh, why did I suddenly think of mother taking a family photo? Is it because it's that photo right there? *I reach out to grab it*"
    i "This is our family photo, but why are there 4 people? Who is the man there? Why haven't I noticed him before? I've been praying in here for 5 years and I've never seen him...something's wrong with me today."

    hide bg prayroom
    hide Idhant i
    show Aayush a

    "A little boy" "Idhant, do you want to play with me?"
    "A little boy" "Let’s play together."

    scene bg prayroom
    show Idhant i

    i "What is that? Why am I seeing it? Who is that little boy? "
    "I have many questions."

    show Idhant i at left
    show Aayush a at right

    a "Hello, Idhant. "
    "*A spirit appears in front of me*"
    "I stepped back in shock."
    i "Who are you? How did you get into my house?"
    a "You don't remember me? How tragic."
    i "I have never met you, so how can I remember you? Tell me who you are or I'll call the police!"
    a "*sigh* My name is Aayush. I am a ghost, and only you can see me, if you call the police they might take you away instead..."
    i "What are you talking about? why would they take me away?! You're the intruder here. I may be religious but I don't believe in ghosts."
    a "Try to touch me. If I am a not ethereal, you'll be able to touch me."
    "*I reached out towards Aayush's outstretched arm*."
    "*With my hands where I thought his arm would be, I felt nothing...my hand phased through with nothing in its way."
    a "Do you believe me now?"
    i "How, how is this possible? Why is this happening to me?"
    a "Patience, Idhant, so many questions - all will be revealed..."
    i "Why are you in my house? What are you doing here?"
    a "Idhant, stop asking questions and listen I am here to show you the truth."
    i "The truth? What truth? This is all too much to take in at once..."

    show Mom at center
    m "Idhant? Why are you being so loud in the praying room?"
    i "I'm sorry mother, I'll quiet down"
    m "It doesn't sound like you are praying. Who were you talking to?"
    i "No one, mom, I was just thinking out loud."
    a "If you are going to think out loud, go do it in your bedroom!"
    i "I got it, I'm sorry! I'll be in my room if you need anything mother."


    scene bg bedroom

    show Idhant i at left
    show Aayush a at right

    "*I stumbled back to my bedroom, the short conversation with the ghost was too much for me.*"
    i "What is going on? Why did the ghost suddenly appear	?"
    a "You can see me because you touch the amulet "
    "I look at the amulet, it’s still in my hand."
    i "You said you are here to help me. How?"
    a "I am here to help you learn the secret of New Delhi."
    i "Secret? What are you talking about? There's no secret in this society, this is paradise!"
    a "Well, it seems Delhi is doing a great job hiding its secrets."
    a "Did you see anything when you first touch the amulet?"
    "*I thought back to the random memory scene I saw*"
    i "Yeah, how'd you know? I saw my mother setting up the camera for the annual family photo."
    a "That was your true memories returning. That was a part of you that was lost."
    i "*Exasperated* What are you talking about? You suddenly appear and say all these things, I hope you know it's a lot to take in at once."
    a "You have to believe me. I have yet to say a single lie to you, what would I stand to gain by lying? I'm already dead."
    a "Tell me what you saw in the vision and I'll explain it to you."
    "*My curiosity was greater than my doubt, I want to find out what that vision meant.*"
    i "I saw I was taking the family photo with my parents. And there is a man that I do not know."
    a "That person is your brother."
    i "My brother? But I don’t have a brother."
    a "That's what they want you to think. What else did you see?"
    i "I also saw another boy, and he asked me if I wanted to play with him. Was that my brother? Another friend?"
    a "Yes, like I said earlier, that is - or should I say, was your brother."
    i "But I don't remember having a brother at all!"
    a "That’s the secret of New Delhi I'm revealing to you. They remove all the memories of your brother fromm you, your parents, and everyone who knew your brother."
    a "No one remembers your brother."
    i "Why would they do that?"
    a "And this is part of the secret of New Delhi I want to help you uncover."
    i "How would you do that, you're just a ghost and why did you choose to help me. Why appear now and not earlier or later?"
    a "You don’t have to know the reason, those details are trivial. Just know I can help you know why your brother disappeared. Look at your amulet. It’s broken into three pieces. Find all the pieces and you will understand everything."
    "*doubtful, but curious* Maybe he is right. I want to know why I can see this ghost, why I lost the memories of my brother and why the city would do such a thing."
    a "I understand that you need some time to accept and procecss the information."
    a "I will tell you more information tomorrow."
    i "Yeah, I'd appreciate that greatly, there's just too much to think about and your mysterious appearance isn't exactly making this easy to digest. I'm just going to sleep and worry about it tomorrow."


    hide Aayush
    hide Idhant
    jump Chapter_Two
    #End Chapter One

    #Begin Chapter Two




# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Idhant = Character("Idhant")
define Young_Idhant = Character("Young Idhant")
define Aayush = Character("Aayush")
define Young_Aayush = Character("Young Aayush")
define Alia = Character("Alia")
define Ghost = Character("Ghost Aayush")
define Police = Character("Delhi Officer")


# The game starts here.

label Chapter_Two:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house
    pause
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Idhant

    # These display lines of dialogue.
    "CHAPTER 2"
    Idhant "Aayush told me to go the place where it all started"

    Idhant "But I don't know where that is"

    Idhant "Well I guess I could start looking for clues around the house. I'll
    start in my room"

    scene room

    show Idhant

    Idhant "Since our family lives in a two bedroom house, that means Aayush had to
    have shared this room with me"

    Idhant "I wonder if anything in this room belongs to him.
    What items should I examine?"

label Examination1:

    menu:
        "Trophy":
            Idhant "I don't remeber winning this trophy maybe this belongs to Aayush. I'll
            check the plaque in the trophy to see what the competition was."
            "Men's Bowling Champions"
            Idhant "This is one of my dad's bowling trophies."
            jump Examination1

        "Telescope":
            Idhant "This telescope has been in my room since I was a baby. It was
            a gift from my grandparents."
            jump Examination1

        "Clay Statue":
            Idhant "This clay statue has always been in my room but, I don't know where it came from. I should
            should check if the artist left their identity anywhere on the statue."

            jump Flashback

label Flashback:

    scene blackscreen
    "Haha over here Idhant! Follow me this way!"
    Idhant "I recognize that voice! It's Aayush!"

    scene caveOpening
    show YoungAayush

    Young_Aayush "This is what I wanted to show you. Follow me this way!"
    show YoungIdhant

    Young_Idhant "What is this place?"
    Young_Aayush "Hurry up Idhant! I don't want anyone to follow us in here."

    scene room
    show Idhant

    Idhant "That must have been something that happened in the past"
    Idhant "I wish I could remember where that cave is."
    Idhant "I think I've seen that opening at one of the parks near my house."
    Idhant "I have seen that opening at:"

label parkDecision:
    menu:
        "Mughal Gardens":
            Idhant "No it can't be in the Mughal Gardens, that park is man-made
            there can't be a cave there."
            jump parkDecision

        "Delhi Ridge":
            Idhant "Yes! it was the Delhi Ridge. I remember there is a
            smiliar cave opening in the South-Central Ridge."
            Idhant "I should grab a flashlight and head over there now."
            jump leavingForPark

        "Gulmohar Park":
            Idhant "There is no way the cave opening is in Gulmohar park.
            That is where all the government officials live I am not allowed
            to hang out in that park."
            jump parkDecision

label leavingForPark:

    scene house
    show Alia

    Alia "Idhant are you going somewhere? Curfew is in an hour minutes."
    Idhant "I promise to be back before curfew is over."
    Alia "Don't stay out to long. You know the punishments for not being home
    after curfew."
    Idhant "I know mom."

    scene park

    "Thirty minutes later..."

    show Idhant

    Idhant "I didn't think it would take me this long to get here.
    Curfew is in half an hour, but I can't turn back. I have to find the
    pieces of the amulet."

    scene blackout

    Idhant "Wow it is super dark in here. Good thing I brought my
    flashlight with me."

    scene caveOpening

    show Idhant

    Idhant "This is the place that was in my flash back. I have
    no time to waste I have to go inside."

    scene insideCave

    show Idhant

    Idhant "There seems to be a two pathways, I bet one leads to a
    dead end."

    Idhant "There is something written in the dirt in between the two
    pathways, maybe it will lead me to the right way."

label firstRiddle:

    "John Locke said that life, liberty, and property are
    natural _______ to mankind."

    Idhant "Which way should I go?"

    menu:

        "Right":
            jump nextPathway

        "Left":
            scene deadEnd
            show Idhant
            Idhant "Its a dead end. I better head back."
            jump firstRiddle

label nextPathway:

    scene insideCave
    show Idhant

    Idhant "Another fork in the road. Let's see if I can solve
    this puzzle too."

    ##RIDDLE # 2



label secondRiddle:

    Idhant "Left is right. Right is wrong. Right is right. Left is left."
    Idhant "Which way should I go?"

    menu:
        "Right":
            scene deadEnd
            show Idhant
            Idhant "Its a dead end. I better head back."
            jump secondRiddle
        "Left":
            jump finalPathway

label finalPathway:

    scene insideCave
    show Idhant

    Idhant "This is long maze, but I can't stop now. I need to solve
    this next riddle."

    ##RIDDLE #3
label thirdRiddle:

    Idhant "If you screw a light bulb into a socket by turning the bulb
    toward the right with your right hand, which way would you turn the
    socket with your left hand in order to unscrew it while holding the
    bulb stationary?"
    Idhant "Which way should I go?"

    menu:
        "Right":
            jump hideaway

        "Left":
            scene deadEnd
            show Idhant
            Idhant "Its a dead end. I better head back."
            jump thirdRiddle

label hideaway:

    scene hideaway
    show Idhant

    Idhant "I finally made it!"
    Idhant "This place seems so familiar to me. I can tell I have been here
    before."
    "Written into the wall are the names Idhant and Aayush."
    Idhant "This must have been some place Aayush and I hung out."
    Idhant "I wonder what we used to do in here."
    "Logeged into the wall of the cave underneath the name is a small
    gem piece."
    Idhant "That must be a piece of the amulet."
    "Idhant takes the amulet piece"

    scene hideaway
    show YoungAayush

    Young_Aayush "This is what I wanted to show you. This cave
    is just for the two of us."

    hide YoungAayush
    show YoungIdhant

    Young_Idhant "Wow this is so cool. Is this place our secret
    headquarters."

    hide YoungIdhant
    show YoungAayush

    Young_Aayush "This place can be whatever you want it to be.
    This is the start of a new chapter in our lives."
    Young_Aayush "In a world of complete surveillance. We now have
    somewhere for oursleves."
    Young_Aayush "We need to make sure no one else can find this place.
    Promise me you won't tell anyone about this place."

    hide YoungAayush
    show YoungIdhant

    Young_Idhant "I promise."

    scene hideaway
    show Idhant

    Idhant "I remember now. This was our place."

    hide Idhant
    show ghost

    Ghost "It our place indeed. We were the kings."

    hide ghost
    show Idhant

    Idhant "Are you and me still the only people who know about this place."

    hide Idhant
    show ghost

    Ghost "Probably not, nothing stays unknown in this place."
    Ghost "I see you have found a piece of
    the amulet. Now you need to find the next piece. And I can show you the general area of where to find it."

    hide ghost
    show Idhant

    Idhant "What are you waiting for? Tell me where find
    the next piece."

    hide Idhant
    show ghost

    Ghost "I think you are going to need help in order to retrieve
    the next piece of the amulet. Do you know anyone that can help you?"

    hide ghost
    show Idhant

    Idhant "Yes, I think I know someone that can help me. My friend Zenya"

    hide Idhant
    show ghost

    Ghost "You're going to need all the help you can get. Talk to Zenya
    and bring him  along with you to the ."

    hide ghost
    show Idhant

    Idhant "I should start heading home it's getting late, I wonder what time it is."

    "11:00 pm"

    Idhant "Dang! It's past curfew! I can't let anyone catch me on my way home."

    scene park
    show Idhant

    Idhant "I can't go home they way I came because someone will see me. I
    have to go around the city center so I don't get caught."

    scene alley
    show Idhant

    Idhant "I wonder what I should tell Zenya. He'll probably think I am crazy."

    hide Idhant
    show officer
    hide officer
    show Idhant

    Idhant "A Delhi officer! I need to hide somewhere."

    Idhant "Where should I hide."

    menu:
        "Inside the trash container":
            "I'll just jump in here and hide until he leaves."
            jump goinghome

        "Turn into the alley":
            "I'll just turn into this alley right here."

            scene deadalleyend
            show Idhant

            "It's a dead end. If the officer walks past he will see me.
            I have to hide in the trash so I don't get caught."

            jump goinghome

        "Turn around and find another way home":
            Idhant "I don't think I should find another way home. I think I'll
            run into another patrol officer."
            Idhant "I'll just hide in the trash until the patrol officer leaves."

            jump goinghome

label goinghome:

    scene blackout

    "15 minutes later..."
    Idhant "I think it's safe now."

    scene alley
    show Idhant

    Idhant "That was too risky. I need to start being more careful."

jump Chapter_Three

# The game starts here.
define z = Character("Zenya") #mc friend
scene plaza
label Chapter_Three:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show idhant at left
    with fade

    # These display lines of dialogue.
    "CHAPTER 3"
    "After some time walking, I arrive at the plaza"
    i "I cannot stop thinking about this amulet"
    i "What could it mean?"
    i "And what do these memories have to do with it?"
    i "...."
    pause .5
    "I spot my friend on the other side of the block."
    i "Is that Zenya?"
    "I walk towards Zenya"

    show zenya at right
    with fade

    z "Hey Idhant! Haven't seen you in a while! How have you been?"
    i "Good, Zenya. Been busy a lot recently."
    i "How have you been?"
    z "As best as I can, Idhant. Was there something you needed?"

    menu:
        "Tell Zenya about the amulet.":
            jump reveal1
        "Describe memory to Zenya (do not reveal amulet)":
            jump not_reveal

label reveal1:

    scene plaza
    show idhant at left
    show zenya at right

    i "Look at this..."
    pause 1
    "*I show Zenya the amulet in the palm of my hand.*"
    pause 1
    "*Zenya stares at the palm of my hand, with visible confusion.*"
    z "What is it?"
    i "I think its some kind of amulet"
    z "Hmmm...."
    z "It looks incomplete...."
    z "Like there are parts missing to it"
    i "Exactly my thought Zenya. I'm trying to figure out what its used for, if it indeed has a purpose"
    z "If it actually does something you'll probably need to find the missing pieces"
    i "My thoughts exactly!"
    i "I could use your help finding the missing pieces. Will you help me?"
    z "Sure, but where do we even start?"
    "Zenya is looking around. I think he is trying to find someone who might help us?"
    "If I tell him about the memories, he'll think I'm crazy!"
    "...."
    pause 1
    "*Suppose I don't have a choice.*"
    i "Well that's the thing, I've been having these memories ever since I held this amulet"
    z "Memories? Like what?"
    i "Places. I think they might be clues to where the other pieces of the amulet are"
    z "What did you see?"
    "*I show Zenya the drawing*"
    i "This is what I saw."
    "He stares at it, trying to work it out"
    pause 1
    z "Hmm...."
    i "Do you know where this could be?"
    z "Actually yes..."
    i "Really?!"
    "I'm surprised he recoginised it so quickly."
    z "Follow me.."
    "I follow Zenya to where he thinks it will be"
    scene black
    hide idhant
    hide zenya
    "I keep thinking to myself where this could lead us, where we could end up."
    "There's something strange about this amulet, it's like its trying to tell me something"
    "Something that I shouldn't know..."
    pause 1
    "Something dark..."

    return

label not_reveal:

    scene plaza
    show idhant at left
    show zenya at right

    "I don't know who I can trust with this, best keep it to myself...."
    "But I need to get some help, otherwise I'll never find where this leads"
    i "Actually yes, I need your help on something."
    z "Go on."
    "I need to find where that memory was showing me"
    i "Last night I had a dream, a strange dream..."
    i "I dreamnt of a place, and I'm not sure where it is"
    z "What did this place look like?"
    i "I drew it, or some of it, can you tell where this is?"
    "I show Zenya the drawing in my hand"
    "He stares at it for a while... trying to discern the fragmented scribblings in my hand"
    pause 1
    z "Hmm..."
    i "Do you know where this could be?"
    z "I think so..."
    i "Really?!"
    z "Yeah, I recoginise this place"
    i "Where is it?"
    z "If you head down there..."
    "Zenya points to a direction right behind me"
    z "...and keep following the path you should find it."
    i "Great! Thank you Zenya!"
    z "No problem. Do you want me to come with you?"
    "I hesitate for a moment. I start having a debate in my head instantly"
    "I want to bring Zenya along, but what will we discover along the way?"
    "I don't want to put Zenya in danger because of my curiosity, but I also don't want to shut him out"
    "I suppose it isnt worth the risk."
    i "Actually Zenya, I think I'll check it out on my own."
    "Zenya looks a bit disappointed but comes to an understanding"
    z "Oh ok, well let me know if you need anything else."
    i "Definitely, thank you Zenya"
    hide zenya
    hide idhant
    show idhant
    "I keep wondering to myself what this all will lead up to."
    "Is there something this amulet is trying to tell me? And what about the ghost encounter?"
    "Something feels wrong with this, something that I should not know..."
    pause 1
    "Something dark..."



    jump Chapter_Four
    # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Zenya") #mc's  zenya


# The game starts here.

label Chapter_Four:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene main_park

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    show zenya_neutral at right
    show Idhant_neutral at left
    with fade

    default park_bench = False
    default park_field = False
    default reveal_amulet = False
    default amulet_piece2 = False
    # These display lines of dialogue.

    b "Do you think this is the right park? Based on your drawing it can be any of the parks around here."
    i "Yeah, it's a little  hazy from my memories but this place matches best with my drawing. I can feel it."
    b "If you say so, let's take a walk around the park then, maybe we'll spot something."
    i "That sounds like a good idea."
    b "Where do you want to check first?"

    menu:
        "I want to go to the benches." if not park_bench:
            $park_bench = True
            jump park_bench
        "I want to take a stroll across the field." if not park_field:
            $park_field = True
            jump park_field

label park_field:

    scene bg field
    with fade
    $park_field = True
    "*As we walked over to the field in the center of the park, I start seeing fragmented images*"
    i "It...It's all coming back to me!"
    "*I subconciously reached for the necklace, a loud voice blares in my head*"
    a "That's right Idhant, remember! Remember me!"
    i "*feels an intense headache*"
    jump field_flashback

label field_flashback:
    scene bg fragmented_field
    show child_Idhant at left
    show child_Aayush at right
    with fade

    i  "Hah! are you ready for my ultimate throw, Aayush?"
    a "Bring it on Idhant, I know you have no strength in that small arm of yours"
    i "Hmph! let's see you hit this one!"
    "*I throw the cricket ball with all my might at Aayush. Thwack! Aayush smashed the ball high up  and into a nearby tree.*"
    i "What! you lost the ball!"

    "*Aayush smiles all smug acting like he broke a world record.*"
    show child_Aayush at center

    a "HAHAHA! Idhant did you see that? Did you see how hard I hit the ball! I think I  won this one."

    "*I point to the tree*"

    i "And do you see that? You lost the ball, and now we can't play cricket anymore! You lost us the game, literally."
    a "Big deaaal we can just climb up the tree to get it."
    i "Are  you crazy?! look at how high up that tree is, what if you fall down. All this for a ball? That's not worth it."
    a "Come  on, stop being a big baby, help out your brother and we can get the ball down in no time."
    i "Fine if you're the one thats climbing the tree."
    a "Of course! How could I ever~ endanger you, mother would kill me if she finds out."
    i "Alright let's go, I'll give you a boost then."
    a "That's the spirit!"
    "*I watched as Aayush climb up the tree after giving him a boost*"
    i "Have you found it yet?! We need to grab it before father and mother comes back from their walk!"
    a "Yeah! It's right there, I can almost reach it! *Points at the ball*"

    "*I follow Aayush's finger to the ball, but instead I see a shiny glimmer.*"
    jump transition

label transition:
    scene bg field
    show zenya_neutral at right
    show idhant_neutral at left
    with fade

    if park_bench and not park_field: #if visited park bench alrdy then check out next place
        b "Idhant! Idhant! Are you okay? You shouted and just stood there!"
        i " yeah, yeah I’m fine let’s continue, I think we are on the right track."
        b "Alright, let's check out the next place"
        i "Wait, I'm looking for a tree nearby, I feel something calling out to me. I'll feel it."
        b "A tree?"
        i "Yeah, I'll need you to give me a boost to climb thee tree though."
        b "Umm, okay?"
        "*Zenya boosts me up the tree where I saw the glimmer in my dream*"
        hide zenya_neutral
        i "*whispering* I-It's really here. *I picked up the missing amulet piece and placed it in my pocket*."
        $amulet_piece2 = True
        i "Zenya, I'll need you to catch me if I fall from this tree haha."
        "*I slowly climbed down from the tree, I can see people passing me by looking at me weird but I was too excited to care*."
        show zenya_neutral at center
        b "I hope whatever you did that for was worth it."
        i "I hope so too. Are you ready to move on?"
        b "Yeah, let's go, where are we headed next?"
        i "let's head to the benches, I remember we spent a lot of time there when we were younger."

        jump park_bench
    elif park_field and not park_bench: #if field visited alrdy check out field
        i "pheeew, I think we sat here long enough"
        b "you think so? We sat on this bench for 10 minutes, you went all quiet and stopped responding to anything I said"
        i "*looking sorry* Ah Zenya! Sorry I was a little lost in my  thoughts, it's nothing. Let's keep going"

        jump park_bench
    elif park_field and park_bench:
        b  "Idhant! there you go scaring me again. Can you stop please zoning out for 10 minutes everywhere we go?"
        i "I'm sorry I zoned out again, let's head leave before I actually fall asleep zoning out haha"
        b "wait Idhant we need to talk, you've been dragging me around and I don't even know why...you're asking me these questions about all these places
        and you've just said it came from a dream...do you have anything else to tell me?"

        jump preending

label park_bench:
    scene bg field
    show zenya_neutral at right
    show idhant_neutral at left
    with fade
    $park_bench=True

    i "Let’s head to the bench area"
    b "sure, you take the lead"

    scene bg park_bench
    show zenya_neutral at right
    show idhant_neutral at left
    with fade

    "Hmm, I remember resting here after walking with my father and mother. Now with the other memory I know there’s a missing piece."
    b "So why are we here?"
    i "*stutters* I-I saw this place in my dream and it's happening alot recently so I want to check it out, that's all!"
    b "Haha, you came all this way for that? It’s probably because we use to play here all the time!"
    i "Yeah probably, give me a few more minutes"
    b "yeah sure, we’re here now anyways"
    i "Thanks"
    "*I grabbed the amulet and close my eyes*."
    a "Remember all the times we spent here, all the times you would drop your ice cream, the times we fed the ducks together"
    i "*murmuring* yeah, yeah I’m beginning to remember it"

    "*I start to feel a flashback.*"
    jump bench_flashback

label bench_flashback:
    show child_Idhant at left
    show child_Aayush at right
    with fade

    a "What a day at the park huh Idhant"
    i "Yeah! I would never get bored of coming here, just being able to run around and play cricket makes my day"
    a "Haha mine too, little brother, mine too. I wonder what’s taking father and mother so long, do you think they left us behind?"
    i "*tearing up* Wh-why would you joke about that"
    a "*panicking* Aah Idhant you know I’m only joking, look at that here they come now! Don't tell dad!"
    i "*pouting* you’re a jerk sometimes, you know that!"
    a "*grinning* and you’re such a crybaby! Look at you, you’re 10 years old now crying over a small joke!"

    jump transition

label preending: #knows a little truth
    i "No, it's nothing. I just had a weird dream that lead me to this place that's all"
    b "What weird dream requires you to climb up a tree, what was that for anyways"
    i "I just remebered that I use to play cricket out here with my parents and one time the ball got stuck in the tree but never got it down - I wanted to check if the ball was still there"
    b "Well was it?"
    i "No, I couldn't find it anywhere maybe the wind knocked it out. That dream made the ball worth a lot to me you know, thats why I asked for your help."
    b "Really? That's all we came out here for?"
    i "That's why I didn't want to tell you, I knew you wouldn't believe me."
    b "Alright alright, I'll back off, I take your word for it. Can we leave now?"
    i "You can head on out first, I want to stay here a little longer and reminisce, it's been so long."
    b "Sure, I'll see you later then."

    hide zenya_neutral
    jump ending

label ending:

    i "*sigh* That was tiring, I wonder if I made the right decision including Zenya."
    "*You reached for the amulet making sure it's still there*"
    "*Suddenly, you feel a headache, lights start going off in your head slowly fading to reveal a silhoutte of what seems like an ancient temple."
    i "I don't know how many more of these I can take. They hurt more everytime! Dang these memories, what do they want from me."
    show ghost
    a "Go! You must finish this amulet and discover the truth about me. Follow the silhoutte from your mind, it is a place nearby. We are almost done uncovering the truth..."
    i "Wah! you scared me, you know it would be a lot easier if  you just told me where to go instead of giving me hints everytime I hold the amulet."
    a "That I cannot do, for you must discover the location by digging into your feelings and connection to the location. Now go! You've been to this place before"
    hide ghost

    i "Damned ghost, I sometimes wonder who's helping who here. It doesn't feel like he's doing this for me at all."

    "END CHAP 4"
    jump Chapter_Five



label Chapter_Five:
    # adding images here
    #keep
    image templeBackground = "Temple.png"

    #change this
    image main = "MC.png"
    image friend = "friend.png"

    #keep
    image friendHold = "friend_holding_red.png"
    image femaleRandom = "female_random.png"
    image maleRandom = "male_random.png"

    #adding characters here
    #change this
    define idhant = Character("Idhant")
    define zenya = Character("Zenya")

    #keep
    #add color to their names
    define maleStranger = Character("Random Person")
    define femaleStranger = Character("Random Person")
    # adding the background
    scene templeBackground
    "CHAPTER FIVE"
    "You arrive at the temple, the final place to find the last piece of the amulet"
    show main at left

    idhant "This looks like the area where I can find the last piece to the amulet."
    idhant "I should look around and ask if anyone has seen anything."

    "*I walk up to a random stranger.*"

    show maleRandom at right

    idhant "Excuse me sir? I dropped a shiny jewel that attaches to a amulet around here, have you seen anything?"
    maleStranger "No, sorry, I haven’t seen anything. Have you tried the lost and found?
        I once found my jacket there when I lost it about two weeks ago."
    idhant "No I haven’t.  Where is it located?"
    maleStranger "It is over by the entrance to the left."
    idhant "I’ll go look for it there, thanks for your help."
    maleStranger "No problem."

    hide maleRandom
    "*I arrive at the lost and found area and walk up to someone who looks like they work here.*"

    show femaleRandom at right

    idhant "Hello ma’am, have you seen a small piece of an amulet? It's my family’s and I accidentally dropped it."
    femaleStranger "What does it look like?"
    idhant "It's small and green, almost like a small emerald."

    femaleStranger "I haven’t seen anything, but maybe someone else found it.  You are welcome to look in that box on the shelf.
        It has items in there that people have lost."
    idhant "Thank you so much!"

    hide femaleRandom

    "You look in the box and find nothing of interest"
    idhant "Hmm.  The last part of the amulet doesn’t seem to be here."

    show femaleRandom at right

    femaleStranger "Did you find it?"
    idhant "No, it wasn't here, but thanks for your help."
    femaleStranger "My pleasure, I hope you find it."
    idhant "I hope I do too."

    hide femaleRandom

    "You search underneath the benches, chairs, and tables"
    "You ask everyone around the temple if they have seen anything"
    "Nothing..."
    "After hours of searching around the temple, I become frustrated and walk outside the temple to get some fresh air"

    idhant "I swear this is the place, I know it is. I have been searching for hours and have gotten nowhere."

    show friend at right

    zenya "Hey Idhant, what are you doing here? You seem mad about something?"
    idhant "Zenya!? Where did you come from? You scared the sh-"
    zenya "Oh sorry, didn’t mean to scare you like that, I just saw you and it looked like you needed something."
    idhant "Yeah, do you remember when you helped me get that one piece of my amulet, I am looking for the last piece."
    zenya "I see..."
    idhant "You wouldn’t have happened to see part of an amulet around here have you?"
    zenya "Are you talking about this?"

    hide friend
    show friendHold at right

    "*Zenya holds up the last piece to the amulet*"
    idhant "Yes! That is the last piece! I can finally know the truth.  Thank you so much Zenya! Where did you find it?"
    zenya "Well, I just happened to stumble across it while on my way to a meeting I was supposed to go to."
    idhant "Thanks so much Zenya, if you give it to me I will just be on my way.  You are probably going to be late to your meeting anyways."
    zenya "No it’s fine.  If they knew what I was up to, they wouldn’t mind if I was late.
        I actually just wanted to talk to you about this.  You have been acting so weird lately, Idhant, are you feeling okay?"
    idhant "What are you talking about?  I am fine, now just give me that and I’ll be on my way."
    zenya "Are you sure? You seem-"
    idhant "I am FINE! Zenya, just give me the piece!"
    zenya "No! There is seriously something wrong with you, you need help Idhant.
        What is this amulet and why are you so obsessed with it."
    "*People start to notice the commotion.*"
    "*Zenya looks around nervously.*"

    zenya "Idhant, please don't shout.  Come on, I am your friend, don't you trust me? You can tell me."

    #---------add a bool here for the ending for ch7---------------
    $ friendEnding = False
    menu reveal_secret:
        "You wouldn’t understand.":
            idhant "You wouldn't undertand, Zenya."

        "This has nothing to do with you.":
            idhant "This has nothing to do with you. Leave me alone Zenya."

        "Give it to me NOW!!!":
            idhant "Give it to me NOW!!!"

        "Fine I will tell you, but promise me you won’t tell anybody about this.":
            $ friendEnding = True
            jump reveal

label after_reveal:
    #Idhant doesnt reveal anything

    hide friendHold
    hide main

    show maleRandom at right
    maleStranger "Hey can you two keep it done over there! You are distracting everyone!"

    hide maleRandom
    show main at left

    idhant "Sorry about that"

    show friendHold at right
    zenya "I just want to help you Idhant. Ever since I helped you find that one piece to the amulet, you have been acting weird.
        This amulet is changing you."

    idhant "I am over this Zenya, hand me the last piece or I'll just have to take it from you."
    zenya "Come on Idhant, we are friends.  You dont have to be so aggressive."
    idhant "Hand it over, I wont ask again."
    zenya "Fine, I dont want to cause a scene.  Just promise me you will stay out of trouble."
    "Zenya hands you the final piece of the amulet"

    hide friendHold
    show friend at right

    idhant "Finally, thanks for understanding Zenya, now I can finally help you."
    zenya "What are you talking about? I don't need help, who are you talking to?"
    idhant "Don't worry about it, we are fine."
    zenya "Who is we?  See Idhant, you are talking nonsense!  I need to know if you are feeling okay?"
    idhant "Just leave me alone, Zenya.  If you really want to know since you keep bothering me..."

    menu lies:
        "(Lie) Fathers amulet":
            idhant "This is my father's amulet and I accidentally broke it.
                He was devastated that it was broken so he forced me to find the pieces."
            idhant "I am sad that I broke it too, but he doesn't talk to me anymore.
                I just need the last piece and everything will be fine."
        "(Lie) A freinds amulet":
            idhant "I have a friend that is looking for this amulet and I wanted to help him out.
                He has been stressing about it for days."
            idhant "I owe him a favor, but its been a long stressful day trying to find it."
        "(Lie) Family's amulet":
            idhant "I broke my family's amulet and they were very mad at me.
                They said that it's been in the family for generations.
                It’s just been a stressful few days trying to find all of the pieces."

    zenya "Oh, I see, I am sorry Idhant, I had no idea."
    idhant "Yeah, well, now you know after you've been pressuring me to say something since we started talking."
    zenya "I am truly sorry.  I thought you were in trouble and I didn't want you to get hurt."
    idhant "It's fine, I hope you realize that you can't just push for answers because you want to know everything.
        Sometimes you can hurt others trying too hard, you know."
    zenya "Yes, I see now.  Again I am sorry, I didn't mean any harm, just wanted to help you."
    idhant "See you, zenya.  Just leave us-, I mean, just leave me alone.
        I got some important things to do."
    zenya "Good bye, Idhant."

    jump Chapter_Six

label reveal:
    #Idhant reveals the truth about the amulet
    idhant "Fine I will tell you, but promise me you won’t tell anybody about this."

    zenya "Yeah sure.  I am here for you Idhant, your secret is safe with me."

    idhant "I have been having these visions about this person."

    zenya "What are you talking about? Does this have to do with the amulet?
        Is the amulet giving you those visions?"

    idhant "Yeah, it’s hard to explain, but these visions…
        I feel like there is more to them.
        This person seems so familiar and he has been trying to help me find all of the pieces to the amulet."

    zenya "Who is this person you are talking about?"

    idhant "I dont know, but he seems so familiar, like he's my-"

    zenya "Like a brother?"

    idhant "Zenya, how did..."

    zenya "Uh, err, just a guess.  But you don't have any siblings, right?
        I have known you for a long time and you havent told me about a brother."

    idhant "I know, I don't have any siblings, but ever since I found this amulet,
        I have been finding more and more clues."

    zenya "What happens when you collect all of the pieces to the amulet?"

    idhant "I am not sure.  I am trying to find that out right now,
        but I feel like this someone is trying to tell me something."

    zenya "What do you think this person is trying to tell you?"

    idhant "The truth,  I think he is leading me to the truth."

    zenya "The truth to what?"

    idhant "Something bad, but something good.  I dont know yet, it is hard to tell."

    zenya "Is something wrong? Do you think this person is trying to warn you of something?"

    idhant "Well, we will just have to find out won’t we? All I need is the last piece Zenya."

    zenya "Idhant, what if this information that this person is giving you is something that is dangerous?
        What if this \"truth\” you speak of is something that will ruin your life?"

    idhant "Listen, I am going to do anything I can to help this person.
        I need to know what is going on around here."

    zenya "Even if you get hurt or killed?"

    idhant "Look, Zenya, thank you for looking out for me, but I am fine."

    zenya "Idhant, please listen to me.  You are going to get hurt or killed trying to do this."

    idhant "I am fine, Zenya.  You do not have to worry about me."

    zenya "Idhant, I dont think you understand the severity of the situation here.
        Do you even hear yourself.  Visions, people in your memory telling you to do things.
        It sounds crazy!  You sound crazy!"

    zenya "Don't you see what this amulet is doing to you Idhant?  It is making you crazy!
        I mean, do you not even notice what you are talking about?"

    idhant "I told you everything, and I know it sounds crazy,
        but didn't you say you were here for me?  You wanted to know and now your not even helping."

    zenya "I am trying to help you Idhant, I don't want you to get in trouble or get hurt."

    idhant "I know this sounds crazy, I realize that,
        but there is no way I am getting hurt over this, Zenya.
        The world isn't that bad and there is nothing out there that will stop me or hurt me."

    idhant "So I don't need you to look out for me, if anything you are the one who is in my way."

    zenya "I guess you are right. I am sorry."
    zenya "Very well, here you go. Just remember, you may not like what you see."

    "You receive the final piece of the amulet"

    hide friendHold
    show friend at right

    idhant "Thank you so much, Zenya, I really appreciate it.
        Listen, when I find out what is going on, I will let you know.  Got it?"

    zenya "I know."

    idhant "Well see you around Zenya."

    zenya "Sure. It was nice kn- seeing you Idhant."

    hide main
    "You walk off and disappear in the distance"

    zenya "I'm sorry Idhant. I truly am."

    jump Chapter_Six
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define i = Character("Idhant")
define g = Character("Ghost")
define z = Character("Zenya")
define m = Character("???")
define zm = Character("Zenya's Mom")
#characters
image MC = "MC.png"
image MC_KO = "MC_KO.png"
image MC_holding = "MC_holding.png"
image MC_possessed = "MC_possessed.png"
image MC_ghost = "MC_ghost.png"
image MC_tied = "MC_tied.png"
image mom_friend = "mom_friend.png"
image outline = "outline.png"
image friend_uniform = "friend_uniform.png"
image friend_holding = "friend_holding.png"
image brother_ghost = "brother_ghost.png"

#locations/backgrounds
image MC_room = "images/MC_room.png"
image friend_house = "images/friend_house.png"
image black = "black.png"
image cell = "cell.jpg"
image white = "white.png"
# The game starts here.


label Chapter_Six:
    $secret_told = True
    "CHAPTER SIX"
    scene MC_room
    show MC at left
    with dissolve
    i "Man I'm so tired..."
    if secret_told:
        jump friend7
    else:
        jump ghost7

label friend7:
    scene black
    with fade
    scene MC_room
    show MC at left
    with fade
    "*Bzz*... *Bzz*... *Bzz*"
    i "Ugh... who's calling me?"
    show outline at right
    with dissolve
    m "We have Zenya, meet us at the park or we might not guarantee his safety."
    i "Wha-Wh-who is this?"
    hide outline
    "*click* *beep* *beep* *beep*"
    $rcall = True
    jump ghost7

label fmenu7:
    menu:
        "I should try to call Zenya to see if he's okay." if rcall:
            jump rcall7
        "This might be a prank I should check in on Zenya.":
            jump f_house7
        "I'll head to the park, Zenya might be in danger.":
            jump park7

label rcall7:
    $rcall = False
    "*ring*  *ring* *click*...
     The person you are trying to reach is unavailable at this time,
     please try again later."
    i "This might be more serious than I thought."
    i "Let me try something else."
    jump fmenu7

label f_house7:
    scene friend_house
    with dissolve
    show MC at left
    with dissolve
    "Maybe he's at his house."
    "*Ding-dong*"
    i "Zenya, you there?"
    show mom_friend at right
    with dissolve
    zm "Who is this? Oh, Idhant it's you. How are you doing?"
    i "I'm good. Is Zenya home right now?"
    zm "Sorry he left just a little while ago."
    i "Do you know where he went?"
    zm "I think he said he was heading for the park."
    "That's where the voice said to go, I'll have to go to save Zenya."
    jump park7

label park7:
    scene park
    with fade
    show MC at left
    with dissolve
    i "There's nobody here, maybe I can find some clues to find Zenya."
    "*Bzz*... *Bzz*..."
    show outline at right
    with dissolve
    m "I see you've arrived at the park."
    i "Where is Zenya?!"
    m "You'll se him very soon."
    hide outline
    "*click* *beep* *beep* *beep*"
    i "Wha-"
    "*Thunk*"
    hide MC
    with hpunch
    show MC_KO at left
    scene black
    with fade
    scene cell
    with fade
    show MC_tied at left
    with fade
    "Wha-Where am I? What should I do?"
    menu:
        "I've got to try to scream for help.":
            jump scream7
        "Maybe I can find an exit around here.":
            jump look7

label scream7:
    i"SOMEBODY HELP ME! I'M TRAPPED!"
    show friend_uniform at right
    with dissolve
    i "Zenya! What's with that getup? Quick let's get out of here."
    z "I'm sorry Idhant, I didn't want this to end this way."
    i "Huh? What are you saying Zenya?"
    jump reveal7

label look7:
    "All I can see is a light and a door, I wonder where it leads."
    show friend_uniform at right
    with dissolve
    z "It's no use Idhant, there's no way out of here."
    i "Zenya, what are you wearing? Where are we?"
    z "This is the Dehli Abnormality Purification Center."
    i "What-what does that mean?"
    jump reveal7

label reveal7:
    z "You know too much Idhant, you've stuck your nose where it doesn't belong."
    i "Who are you? Where did you put Zenya?"
    z "I am Special Investigator Zenya,
       I work to ensure this society is free from defects like you and your brother"
    i "My brother? what brother..?"
    menu:
        "SCREW YOU!":
            jump yell7
        "Why are you doing this to me?":
            jump why7
        "What happened to my brother?":
            jump bro7

label yell7:
    z "Being upset isnt going to change anything now, Idhant."
    jump friend_end

label why7:
    z "I've already told you,
       It's my job to keep this society running even if I havev to get my hands dirty."
    i "You don't have to do this."
    z "There's no stopping this now idhant."
    jump friend_end

label bro7:
    z "Don't worry about that, I'll reunite you two soon."
    jump friend_end

label friend_end:
    z "I'll be taking this."
    hide friend_uniform
    show friend_holding at right
    with dissolve
    i "That's my amulet!"
    z "Don't worry about your family, I doubt they'll remember you."
    i "Zenya, please!"
    hide friend_holding
    with dissolve
    scene black
    with fade
    return

#start of ghost end
label ghost7:
    show brother_ghost at right
    with dissolve
    g "Quick! Finish the amulet, then you'll remember everything."
    if secret_told:
        "Zenya might be in trouble, what should I do?"
        menu:
            "I shouldn't complete it.":
                jump refuse17
            "Alright, I'll finish it.":
                jump accept7
    else:
        jump accept7

label refuse17:
    i "I don't think I should complete it."
    g "You've come this far already, why give up now?"
    i "I have to check on Zenya first, maybe I should just leave it."
    g "He knows nothing about the amulet; you lied to him then, why trust him now?"
    menu:
        "I really don't want to complete the amulet":
            jump refuse27
        "Alright, I'll finish it.":
            jump accept7
label refuse27:
    i "No, Zenya has stayed with me through all this, I have to help him."
    g "But don't you want to learn about this world's secrets,
       regain your lost memories?"
    menu:
        "For the last time, I won't do it!":
            jump refuse_end
        "Alright, I'll finish it.":
            jump accept7
label refuse_end:
    i "Why are you pushing me to do this? I'm not gonna complete the amulet."
    g "I am your long lost brother, Aayush, Idhant please."
    i "I don't remember any brother! I don't have any time for this amulet."
    g "NO!"
    hide brother_ghost
    with dissolve
    #maybe animation of idhant dropping amulet
    jump fmenu7

label accept7:
    hide MC
    show MC_holding at left
    with dissolve
    "I've done this much, might as well finish it."
    g "Finally, it's complete!"
    scene white
    with dissolve
    #memory regained sequence
    scene MC_room
    show MC_holding at left
    show brother_ghost
    with dissolve
    i "Aayush, my brother! How could I have forgotten you?"
    g "Don't worry Idhant, it won't matter soon enough"
    hide MC_holding
    show MC_ghost at left
    with hpunch
    #maybe flash here instead with chains appearing
    i "Aayush what are you doing?"
    g "All these years I've been dead, missing out on life because I saved you."
    i "What do you mean?"
    g "After saving you from the accident,
       the government wiped away my very existence because I was crippled!"
    g "But I found this amulet. Now through you body I can relive my life."
    menu:
        "I have to release the amulet.":
            jump break7
        "There's no use in struggling now, I just have to accept this.":
            jump give_up7

label break7:
    with vpunch
    i "Why can't I let go?!"
    g "It's no use Idhant, from the moment you completed the
       amulet this was all predetermined just give up now."
    i "Please, Aayush! NO!"
    jump ghost_end

label give_up7:
    i "I give up brother."
    g "Now it's my turn to live."
    jump ghost_end

label ghost_end:
    hide brother_ghost
    with dissolve
    #flash
    scene white
    with dissolve
    scene MC_room
    with dissolve
    show MC_possessed
    with dissolve
    g "hahaHaHaHAHAHA! It worked!"
    g "Finally, a new body!"
    scene black
    with fade


    return
