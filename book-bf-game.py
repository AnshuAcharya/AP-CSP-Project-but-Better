import random
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome! This game will provide a brief description of a book boyfriend, and your job is to guess the boyfriend. At the end, based on your score, the program will tell you your booktok and reading proficiency. You need to answer at least six of the ten right to be considered proficient! If you win, you will get a coveted book boyfriend.")
print()
print("There are three modes: EASY, MEDIUM, and HARD.")
print()
print("EASY will give easy descriptions and you only need to provide the boyfriends first name.")
print()
print("MEDIUM will make the descriptions slightly harder, and  first and last name will be needed. Some may not have a last name, such as Odysseus or Clytemnestra. That is ok--just put what you know.")
print()
print("HARD will be much more niche descriptions, and you will need to say their name as how the female main character refers to them MOST OFTEN, or if they do not have one, just their first name. Click enter immideatley after typing your answer.")
print()


def check_results(correct):
    '''
Function purpose: Check to see how many points they have, and depending on how many points they have, it will pair them with a book boyfriend and tell them how many points they.

Parameters: correct variable

Return type: none

Algorithmic efficiency: linear, O(n)
'''
    bookBoyfriend = ["Aaron Warner", "Kai Azer", "Jacks", "Rhysand", "Percy Jackson", "Ridoc", "Leo Valdez", "Odysseus", "Jason Grace", "Conrad Fischer", "Finny Smith", "Winston Smith", "Cassian", "Kaz Brekker", "Matthias Helvar", "Jesper Fahey", "Edward Cullen", "Jacob Black", "Peeta Mellark", "Finnick Odair", "Rowan Whitethorn", "Dorian Havilliard", "Chaol Westfall", "Cardan Greenbriar", "Maxon Schreave", "Mr. Darcy", "Captain Wentworth", "Day (Daniel Wing)", "Maven Calore", "Josh Templeman", "The Darkling", "Marco Alisdair"]

    if correct <= 2:
        print("You must not read that much...you did not win the game. You only got", correct ,"correct. Time to start reading! Check out the Shatter Me series for a dystopian romantasy, Fourth Wing for a peppery dragon-riding and school book, or just honestly any book, you need to get reading.")
    elif correct <= 6:
        print("Sadly, you did not win, but you are halfway there. You only got", correct ,"correct. Keep on reading, diving into new worlds, and check booktok for some more recs!")
    else:
        print("Congrats! You won! You correctly answered", correct ," of the questions. You know your book men realll well 😉")
        time.sleep(3)
        clear_screen()
        print("Now... for the big reveal...")
        print("Your book boyfriend is...")
        time.sleep(2)
        print(random.choice(bookBoyfriend))
        print("🥳 🥳 🥳 🥳 🥳 🥳 🥳 🥳 🥳 🥳 🥳 🥳")
        print("Lucky you!")


def play_game(questions):
    '''
Function purpose: Randomly selects 10 questions from the question bank and asks them to the user. After getting input, the function makes all the letters lowercase, then compares it to the answer of the key-value pair. If correct, the correct variable counter increases and at the end another function (check_results) is called to display the results.

Parameters: questions dictionary

Return type: none

Algorithmic efficiency: linear, O(n)
'''
    selected = random.sample(list(questions.items()), 10)
    correct = 0

    for question, answer in selected:
        print(question)
        guess = input("What is your guess? ").lower()
        if guess == answer:
            correct += 1
            print("Right!")
        else:
            print("Wrong.")

    clear_screen()
    print("Calculating Results...")
    time.sleep(3)
    check_results(correct)


easy_questions = {
    'Prince and Future Enforcer of Ilya': 'kai',
    'Chief Commander and Regent of Sector 45': 'aaron',
    'Son of Poseidon and loves blue food': 'percy',
    '__ Valdez, Bad Boy Supreme': 'leo',
    'Former third-year rider and wingleader of the Fourth Wing': 'xaden',
    'Son of an Illyrian lord': 'azriel',
    'High Lord and ruler of the Night Court': 'rhysand',
    'Notices 28 freckles on the FMC face': 'kai',
    'Blonde son of Zeus': 'jason',
    'In love with Payden Gray': 'kai',
    'MMC in Fourth Wing': 'xaden',
    'Nickname for Phineas Smith': 'finny',
    'Dates a girl named Annabeth': 'percy',
    'Wizard living at Hogwarts with circle glasses': 'harry',
    'Red-head at Hogwarts': 'ron',
    'Brother to Kitt Azer': 'kai',
    'Spends summer in Cousins with his brother, Jeremiah': 'conrad',
    'Buys his love an infinity necklace': 'conrad',
    'Said: "I would be in the bed next to you if my brother had not slipped a ring on your finger"': 'kai',
    'His tail is used to show his emotions': 'cardan',
    'The first MMC in the Twisted series by Ana Huang': 'alex',
    'Prince of hearts': 'jacks',
    'Captain of the Fjerdan army who falls for a Grisha': 'matthias',
    'Barrel boss of the Dregs in Ketterdam': 'kaz',
    'Vampire who watches Bella sleep': 'edward',
    'Werewolf best friend in Twilight': 'jacob',
    'District 12 baker who loves Katniss': 'peeta',
    'The boy on fire from District 12 who hunts with Katniss': 'gale',
    'Fae warrior with a territorial streak and Illyrian wings, mate to Nesta': 'cassian',
    'King of Adarlan turned rebel in Throne of Glass': 'dorian',
    'Fae prince and warrior, Aelin\'s mate in Throne of Glass': 'rowan',
    'Captain of the Guard in Throne of Glass': 'chaol',
    'Sharpshooter and gambler from Ketterdam': 'jesper',
    'Prince of Illea who falls for a Five named America': 'maxon',
    'Mr. __, the brooding gentleman of Pemberley': 'darcy',
    'Legend of the criminal underworld in Marie Lu\'s book': 'day',
    'Silver-blooded prince with the ability to control metal': 'maven',
    'Said "to whatever end" to his queen': 'rowan',
    'Has a blood duel with the Autumn Court heir for his mate': 'rhysand',
    'MMC in the Hating Game who is very tall and loves to argue': 'josh',
}

medium_questions = {
    'Defeats Ares on a beach in Santa Monica, California': 'percy jackson',
    'Falls into Tartarus to be with her': 'percy jackson',
    'Calls himself Nobody while fighting the Cyclopes': 'odysseus',
    'Eats cookies with a fork': 'aaron warner',
    'Son of the head of the reestablishment': 'aaron warner',
    'Can bench press 315 lbs in grey sweatpants': 'aaron warner',
    'Killed a girl he calls "Gray"s father': 'kai azer',
    'Has a panic attack when his girlfriend breaks up with him': 'aaron warner',
    'He is the reason people say they would "want to be Feyre in chapter 55"': 'rhysand',
    'Boyfriend to the modern architect of Olympus': 'percy jackson',
    'Brother to someone who proposed soely for the benefit of the kingdom': 'kai azer',
    'Attempts to defy the party, but conforms in the end, writing "2 + 2 = 6"': 'winston smith',
    'Makes Echo say "Kiss me, you fool"': 'leo valdez',
    'Buys all of her paintings so no one else can own what she made': 'alex volkov',
    'Wears gloves to hide his touch and runs the Crow Club': 'kaz brekker',
    'Says "I will have you without armor, or I will not have you at all"': 'kaz brekker',
    'Sparkling vampire who plays the piano': 'edward cullen',
    'Gave up his memories and went to a Roman camp as a praetor': 'jason grace',
    'Paints stars on the inside of her drawer to remind her of him': 'rhysand',
    'Son of Hephaestus who dies and comes back to life on Ogygia': 'leo valdez',
    'Decorated war hero from District 2 who volunteers as tribute in the Quarter Quell': 'finnick odair',
    'Ties knots with rope to cope with his trauma in the Hunger Games': 'finnick odair',
    'Bakes bread and paints camouflage in the Hunger Games arena': 'peeta mellark',
    'Declares his love on live television before the Hunger Games': 'peeta mellark',
    'King who places a crown of flowers on her head rather than gold': 'cardan greenbriar',
    'Fae warrior who says "to whatever end" as a pledge to his queen': 'rowan whitethorn',
    'Prince who secretly sends his love letters through a palace maid': 'maxon schreave',
    'Said "You pierce my soul. I am half agony, half hope"': 'captain wentworth',
    'His proposal was so insulting she rejected him at Hunsford': 'mr darcy',
    'Criminal mastermind from the Republic who is known as a legend on the streets': 'daniel wing',
    'Former assassin from Adarlan who becomes King of the North': 'dorian havilliard',
    'MMC whose love interest makes a deal with the villain to save him from a prison camp': 'rowan whitethorn',
}

hard_questions = {
    'Husband to a girl who tried to cut her finger off to please her captor/master': 'warner',
    'Zeus turned his love into a tree to protect her from him': 'apollo',
    'This MMC is from a series lots of people label is a romantasy, but is more focused on the politics and kingdom-building': 'cardan',
    'They have a one day relationship before he dies picking up his girlfriend': 'finny',
    'When he met Aphrodite, he thought "This looks like <friends name>"': 'seaweed brain',
    'Knowledgeable in physics and RSC navigation': 'ridoc',
    'Speculated to have another dragon besides Aotrom': 'ridoc',
    'The MMC in one of Shakespeares top ten and the MMC in the retelling, "These Violent Delights"': 'romeo',
    'He chains himself to her, and she says "Possessive much?"': 'azer',
    'Won her a stuffed animal named Junior Mint': 'connie baby',
    'Lets everyone die to save his crew but at first would not kill even something trying to kill him': 'odysseus',
    'Promises to return for Calypso': 'leo',
    'The reason his girlfriend has to watch Percabeth alone': 'jason',
    'His real name is not known until the end of the first book; she calls him "bastard of the barrel"': 'dirtyhands',
    'She calls him by his last name as a term of endearment, and he calls her Wraith': 'brekker',
    'Dies protecting his district partner with a trident and sugar cubes': 'finnick',
    'He asks "Do you want a sugar cube?" as his introduction at a party': 'finnick',
    'The FMC says she hates him for making her fall in love with a boy with a bread name': 'peeta',
    'Crowned himself High King of Elfhame through exile': 'cardan',
    'She finds out he wrote her name on his hand under his glove in Fjerdan': 'matthias',
    'His catch phrase is literally just "fire" and he says it about everything': 'team leo',
    'Known for saying "Dirtyhands" has no heart, but he gave his to a girl from the Menagerie': 'kaz',
    'His love interest is a literal sun summoner': 'the darkling',
    'The FMC draws him with bat wings as an inside joke between them': 'rhys',
    'He tattooed her name in Illyrian on his chest': 'rhys',
    'Called her "Poppet" and ran a traveling circus of dreams': 'marco',
    'The FMC refers to him as her "husband" even before they are actually married in Throne of Glass': 'buzzard',
    'Was known as Celaena\'s "Sam" before she became Aelin': 'sam',
}

while True:
    openingMessage = input("Spelling counts as well--you cannot be a true book nerd if you cannot spell right. Type 'a' for EASY, 'b' for MEDIUM, or 'c' for HARD to begin. If it is a book title, the whole title--no shorthand.").lower()

    if openingMessage == "a":
        time.sleep(.5)
        clear_screen()
        print("EASY mode selected.")
        play_game(easy_questions)
        break
    elif openingMessage == "b":
        time.sleep(.5)
        clear_screen()
        print("MEDIUM mode selected.")
        play_game(medium_questions)
        break
    elif openingMessage == "c":
        time.sleep(.5)
        clear_screen()
        print("HARD mode selected.")
        play_game(hard_questions)
        break
    else:
        print("Error. Please enter letter a or b or c.")
