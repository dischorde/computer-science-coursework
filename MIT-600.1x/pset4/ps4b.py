from ps4a import *
import time


def loadOnly(n):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Only words that are <= length(n) are loaded
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        if len(line.strip()) <= n :
            wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

#
#
# Problem 4-7: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxscore = 0 # Create a new variable to store the maximum score seen so far (initially 0)
    
    best = None # Create a new variable to store the best word seen so far (initially None)  

    for word in wordList: # For each word in the wordList

        if isValidWord(word, hand, wordList): # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            
            earned = getWordScore(word, n) # Find out how much making that word is worth

            if earned > maxscore: # If the score for that word is higher than your best score

                maxscore = earned # Update your best score, and best word accordingly
                best = word

    return best # return the best word you found.
    
#
# Problem 4-8: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0 # Keep track of the total score
    
    while calculateHandlen(hand) > 0: # As long as there are still letters left in the hand:
    
        print 'Current Hand: ',  # Display the hand
        displayHand(hand)  
        
        word = compChooseWord(hand, wordList, n)
        
        if word == None:
            break

        else:

            earned = getWordScore(word, n)
            score += earned
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print '"' + word + '" earned ' + str(earned) + ' points. Total: ' + str(score) + ' points'
            print
            
            # Update the hand 
            hand = updateHand(hand, word)

    print 'Total score: ' + str(score) + ' points.'
    
    
    
    
#
# Problem 4-9: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {} # initialize hand
    
    def play():
        while (True):
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')
            if player == 'c':            
                compPlayHand(hand, wordList, HAND_SIZE)
                break
            elif player == 'u':
                playHand(hand, wordList, HAND_SIZE)
                break
            else:
                print 'Invalid command.'
            
    while (True):
        entered = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if entered == 'n': #for new game
            hand = dealHand(HAND_SIZE)
            play()
        elif entered == 'r': #for repeat
            if hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                play()
        elif entered == 'e': #for exit
            break
        else:
            print 'Invalid command.' 


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


