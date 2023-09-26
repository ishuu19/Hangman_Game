import random



word_list  = ["banana", "cherry", "tiger", "ocean", "music", "dance", "chair", "mouse", "heart", "watch", "guitar", "plant", "river", "beach", "cloud", "bread", "honey", "smile", "paper", "night", "queen", "horse", "panda", "lemon", "eagle", "robot", "pearl", "dream", "stone", "truck", "pizza", "arrow", "candle", "space", "apple", "grape", "orange", "melon", "apple", "apricot", "banana", "cherry", "lettuce", "onion", "pepper", "tomato", "carrot", "potato", "broccoli", "spinach", "pumpkin", "lettuce", "garlic", "ginger", "celery", "radish", "turnip", "papaya", "cucumber", "asparagus", "avocado", "blueberry", "coconut", "eggplant", "kiwifruit", "mango", "peach", "plum", "rhubarb", "strawberry", "watermelon", "blackberry", "cranberry", "raspberry", "fig", "walnut", "almond", "pecan", "cashew", "peanut", "pistachio", "sunflower", "butterfly", "elephant", "giraffe", "kangaroo", "penguin", "crocodile", "dolphin", "hedgehog", "parrot", "puma", "rhinoceros", "squirrel", "walrus", "dinosaur", "butterfly", "elephant", "giraffe", "kangaroo", "penguin", "crocodile", "dolphin", "hedgehog", "parrot", "puma", "rhinoceros", "squirrel", "walrus", "dinosaur", "astronaut", "scientist", "firefighter", "musician", "athlete", "captain", "detective", "mechanic", "painter", "engineer", "professor", "architect", "waitress", "electrician", "gardener", "journalist", "barista", "veterinarian", "chef", "photographer", "dentist", "librarian", "accountant", "surgeon", "hairdresser", "plumber", "scientist", "firefighter", "musician", "athlete", "captain", "detective", "mechanic", "painter", "engineer", "professor", "architect", "waitress", "electrician", "gardener", "journalist", "barista", "veterinarian", "chef", "photographer", "dentist", "librarian", "accountant", "surgeon", "hairdresser", "plumber", "astronomy", "chemistry", "geometry", "history", "language", "biology", "literature", "medicine", "philosophy", "psychology", "sociology", "nutrition", "economics", "geography", "physics", "computer", "chemistry", "geometry", "history", "language", "biology", "literature", "medicine", "philosophy", "psychology", "sociology", "nutrition", "economics", "geography", "physics", "computer", "baseball", "football", "soccer", "swimming", "tennis", "volleyball", "badminton", "basketball", "cricket", "hockey", "softball", "table", "marble", "mirror", "pillow", "blanket", "cushion", "lamp", "clock", "rug", "curtain", "towel", "furniture", "wardrobe", "shampoo", "conditioner", "toothpaste", "toothbrush", "hairbrush", "comb", "soap", "sponge", "tissue", "lotion", "perfume", "cologne", "deodorant", "lipstick", "eyeliner", "mascara", "eyeshadow", "foundation", "powder", "nail", "polish", "bracelet", "necklace", "earring", "ring", "watch", "sunglasses", "scarf", "tie", "gloves", "umbrella", "wallet", "backpack", "briefcase", "suitcase", "passport", "camera", "headphones", "laptop", "tablet", "keyboard", "mouse", "monitor", "printer", "scanner", "speaker", "microphone", "television", "remote", "control", "projector", "cable", "charger", "battery", "candle", "lighter", "flashlight", "matches", "campfire", "bonfire", "fireplace", "stove", "oven", "microwave", "refrigerator", "freezer", "sink", "faucet", "bathtub", "shower", "towel", "toilet", "sink", "faucet", "mirror", "bathtub", "shower", "towel", "toilet", "mattress", "blanket", "pillow", "sheets", "nightstand", "dresser", "wardrobe", "hammock", "chair", "couch", "sofa", "coffee", "table", "bookshelf", "cabinet", "curtain", "mirror", "painting", "poster", "sculpture", "statue", "vase", "clock", "lamp", "chandelier", "globe", "map", "calendar", "diary", "notebook", "pencil", "pen", "marker", "eraser", "stapler", "tape", "glue", "scissors", "ruler", "calculator", "keyboard", "mouse", "monitor", "printer", "scanner", "speaker", "microphone", "television", "remote", "control", "projector", "cable", "charger", "battery", "outlet", "switch", "plug", "extension", "cord", "wire", "adapter", "screwdriver", "wrench", "hammer", "nail", "screw", "bolt", "nut", "tape", "measure", "level", "pliers", "pliers", "saw", "knife", "scissors", "razor", "toothbrush", "toothpaste", "floss", "mouthwash", "shampoo", "conditioner", "soap", "lotion", "perfume", "cologne", "deodorant", "lipstick", "eyeliner", "mascara", "eyeshadow", "foundation", "powder", "nail", "polish"]


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-1: - Import the logo from hangman_art.py and print it at the start of the game.
logo = '''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                   
'''
print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

  
    if guess in display:
        print(f"You've already guessed {guess}")

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    stages = ['''
      +---+
      O   |
     /|\  |
     / \  |
         ===
    ''',
    '''
      +---+
      O   |
     /|\  |
     /    |
         ===''',
         '''
      +---+
      O   |
     /|\  |
          |
         ===''',
        '''
      +---+
      O   |
     /|   |
          |
         ===''',
        '''
      +---+
      O   |
      |   |
          |
         ===''',
        '''
      +---+
      O   |
          |
          |
         ===''',
         '''

      +---+
          |
          |
          |
         ==='''      ]
    print(stages[lives])