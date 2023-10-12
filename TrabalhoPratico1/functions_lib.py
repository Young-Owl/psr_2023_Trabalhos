import random 
import readchar
from colorama import Fore, Style


def carater():
    """
    Function to generate a random character.
    
    :return Crt:       Generated character
    """
    Num = random.randint(97,122)

    Crt = chr(Num)
    
    return Crt

def printer(flag, word):
    """
    Function to print text relative to the words or letters that have to be pressed and the ones the user pressed
    Receives as arguments a flag, to know which color has to be used, as well as if it was the letter/word
    generated or pressed by the user.
    The flags
    0 - Letter generated by the PC
    1 - Correct letter pressed by the user
    2 - Incorrect letter pressed by the user
    
    :param flag:       Flag to be used
    :param word:       Letter or word to be printed
    """
    if flag == 0:
        print("Type " + "\t\t" + Fore.BLUE + word + Style.RESET_ALL)
    elif flag == 1:
        print("You typed: " + '\t' + Fore.GREEN + word + Style.RESET_ALL)
    elif flag == 2:
        print("You typed: " + '\t' + Fore.RED + word + Style.RESET_ALL)
    
def compare(Str_rec, Str_digi):
    """
    Function responsible for comparing the letter/word generated by the PC with the one pressed by the user.
    If they are equal, the function returns True, otherwise it returns False.
    
    :param Str_rec:       Letter/word generated by the PC
    :param Str_digi:      Letter/word pressed by the user
    :return True/False:   True if the letters/words are equal, False otherwise
    """
    if Str_rec == Str_digi:
        printer(1,Str_digi)
        return True
    else:
        printer(2,Str_digi)
        return False

def average(X, n):
    """
    Basic function to calculate the average of a given value X and a given number of inputs n.
    
    :param X:       Value to be averaged
    :param n:       Number of inputs
    :return X/n:    Average of X
    """
    if n != 0:
        return X/n
    else:
        return 0