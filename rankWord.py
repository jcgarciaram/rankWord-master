'''
rankWord.py
Author: Juan C. Garcia
Email:  jcgarciaram@gmail.com

Pre-Resiquites:
The program requires Python modules to be installed in the computer being used. The program was tested using Python 2.7.9, 
but it will most likely work with previous Python versions.


Executing the program:
Open a command line window and navigate to the folder where the program was extracted to.
The program takes in a word as an argument in the following manner:

python rankWord.py WORD


Algorithm Overview:
The following program takes a word as a command line argument and prints to standard output its
ranking based on where it falls in an alphabetically sorted list of all words made up of the 
same set of letters.

Solution is divided into two parts:

Part 1: 
1. Determine the total number of letters in word input. 
2. Form a sorted array of distinct letters with the number of times the letter
is repeated in the word. Store this array as a tuple array in lettersSortTuple.

Example:
Input: "ABBCA"
lettersSortTuple: [('A',2), ('B',2), ('C', 1)] 

Part 2:
1. Initialize rank to 1. Iterate through input word and compare each character to the sorted tuple array created above which contains
all distinct letters and the number of times they are repeated.       
2. If the character is not equal to the first letter in the sorted array, compute the number of words
that could be created with the first letter in the sorted array in the initial position using factorials. Add this amount 
to the rank variable.

Example:
Input: 'BAAB'
lettersSortTuple:  [('A', 2), ('B', 2)]
B == A?
No!

Place 'A' in initial position. Three letters left. 'B' is repeated 2 times. 'A' is repeated 1 time.

3!/(2!*1!) = 6/2 = 3

Therefore, 3 words can be formed with remaining letters.

Rank += 3 = 4 for now.


3. Continue comparing the character to all other characters in the sorted array and repeat step 2 until
letter matches.

B == B ?
Yes!

4. Once the character is matched, subtract one from the number of times the letter is repeated in the 
input word and move on to the next character in the input word.

lettersSortTuple:  [('A', 2), ('B', 1)]


5. Repeat steps 2 - 4 until all characters in the input word have been matched. Caution is taken to make 
sure to not compare against any letter which has no repetitions left in the sorted array.

A == A?
yes!
lettersSortTuple:  [('A', 1), ('B', 1)]
A == A?
yes!
lettersSortTuple:  [('A', 0), ('B', 1)]
B == B? (A was skipped because no repetitions were left)
yes!
lettersSortTuple:  [('A', 0), ('B', 0)]

Rank = 4
'''

import math
import sys

def rankWord(word):
    
    # PART 1
    
    # Determine length word. If length = 1, return rank = 1. If length = 0, print text error.
    # Also, in case lowercase letters are found, convert to uppercase.
    word = str.upper(word)
    numLetters = len(word) 
    if (numLetters == 1):
        return 1
    elif (numLetters == 0):
        return "ERROR: Word has to contain at least one letter."
    
    
    # Store all distinct letters in lettersSortTuple along with the number of
    # times the letter is repeated.
    lettersSort = []
    lettersSortTuple = []
    for i in range(numLetters):
        if (word[i] in lettersSort):
            j = lettersSort.index(word[i])
            lettersSortTuple[j] = (word[i],lettersSortTuple[j][1]+1)
        else:
            lettersSort.append(word[i])
            lettersSortTuple.append((word[i],1))
    
    # Sort letters in tuple by alphabetical order.
    lettersSortTuple = sorted(lettersSortTuple, key=lambda letter: letter[0])
    
    #Determine number of distinct letters. If distinct letters = 1, return 1.
    numDistinctLetters = len(lettersSort)
    if (numDistinctLetters == 1):
        return 1
    
    
    # PART 2
    
    #Initialize variables to be used later.    
    rank = 1    #Rank of word = Value to be returned. Initialized to one.
    wordPos = 0 #Word position = Character position when iterating through word.
    sortPos = 0 #Sort position = Position when iterating through sorted tuple created above.

    
    # Iterate until all letters in word have been analyzed.
    while (wordPos < numLetters):
    
        # If all repetitions of a letter have been matched, move on to next letter in sorting array
        if (lettersSortTuple[sortPos][1] == 0):
            sortPos += 1
        
        # If letter is matched, move one character up on input word and substract one from the number
        # of repetitions of letter matched in sorted array. Also, reset position of sorted array to 0
        # to prepare for new matching.
        eli (word[wordPos] == lettersSortTuple[sortPos][0]):
            wordPos += 1
            lettersSortTuple[sortPos] = (lettersSortTuple[sortPos][0],max(lettersSortTuple[sortPos][1]-1,0))
            
            sortPos = 0
        
        # If letter does not match, determine how many words can be created using the character from sorting array in the
        # current position.
        else:
            rankTemp = 0
            
            # Temporary copy of sorted array. Substract one repetition from letter being considered to be placed in current
            # position being compared.
            lettersSortTupleCopy = lettersSortTuple[:]
            lettersSortTupleCopy[sortPos] = (lettersSortTupleCopy[sortPos][0], max(lettersSortTupleCopy[sortPos][1]-1,0))
            
            
            # Use factorials to determine number of permutations with remaining letters.
            rankTemp += math.factorial(numLetters - wordPos - 1)
            for i in range(numDistinctLetters):
                if lettersSortTupleCopy[i][1] != 0:
                    rankTemp = rankTemp/math.factorial(lettersSortTupleCopy[i][1])
            
            #Increase sorting position to compare against next letter in alphabetical order. Add ranking determined above to 
            #overall rank.
            sortPos += 1
            rank += rankTemp
        
    return rank

    
    
if __name__ == "__main__":   
    if (len(sys.argv) == 1):
        print "ERROR: No input word detected"
    elif (str.isalpha(sys.argv[1]) == False):
        print "ERROR: Cannot rank words containing characters that are not letters"
    else:
        print rankWord(sys.argv[1])    