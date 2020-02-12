#!/bin/python3

import math
import os
import random
import re
import sys

def isOpeningBracket(aCharacter):
    return aCharacter == '(' or aCharacter == '[' or aCharacter == '{'

def areMatchingOpenAndCloseBrackets(anOpeningBracket, aClosingBracket):
    return (anOpeningBracket == '(' and aClosingBracket == ')') \
        or (anOpeningBracket == '[' and aClosingBracket == ']') \
        or (anOpeningBracket == '{' and aClosingBracket == '}')

# Complete the isBalanced function below.
def isBalanced(s):
    result = True
    openingBracketsPile = list()

    for aCharacter in list(s):
        if isOpeningBracket(aCharacter):
            openingBracketsPile.append(aCharacter)
        else:
            if not openingBracketsPile or not (areMatchingOpenAndCloseBrackets(openingBracketsPile.pop(), aCharacter)):
                result = False

    result = result and not openingBracketsPile
    if result:
        return 'YES'
    else:
        return 'NO'



def areBracketsBalanced(numberOfStrings, listOfStrings):
    result = []
    for aString in listOfStrings:
        result.append(isBalanced(aString))

    return result
#if __name__ == '__main__':
#   fptr = open(os.environ['OUTPUT_PATH'], 'w')

#    t = int(input())

#    for t_itr in range(t):
#        s = input()

#        result = isBalanced(s)

#        fptr.write(result + '\n')

#    fptr.close()
