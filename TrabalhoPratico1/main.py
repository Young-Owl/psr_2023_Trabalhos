#!/usr/bin/env python3
import argparse
import readchar
import time 
import termios
import functions_lib as fl
from colorama import Fore, Style
from collections import namedtuple
from pprint import pprint
from random_word import RandomWords

words_letter = namedtuple('Inputs', ['requested', 'received', 'duration'])

def main():

    # Information declared via argparse
    parser = argparse.ArgumentParser(description='Definition of '+ Fore.BLUE+'test' + Style.RESET_ALL +' mode')
    parser.add_argument('-utm', '--use_time_mode', action="store_true", help='Max number of secs '+ Fore.RED + 'for time' + Style.RESET_ALL + ' mode or maximum number of inputs '+ Fore.RED + 'for' + Style.RESET_ALL +' number of inputs mode.')
    parser.add_argument('-mv', '--max_value', type = int , help='Max number of seconds '+ Fore.RED + 'for time' + Style.RESET_ALL + ' mode or maximum number of inputs '+ Fore.RED + 'for' + Style.RESET_ALL +' number of inputs mode.', required=True)
    parser.add_argument('-uw', '--use_words',action="store_true", help = ' Use word typing mode, instead of single character typing.')
    args = parser.parse_args()
    
    # Variable initialization
    correct = 0
    incorr = 0
    total_time = 0
    types = 0

    time_hit = 0
    dictionary_stat = {"Inputs" : []}

    # Wait for the user's input to start the test
    print("------------------------ PSR Typing Test ------------------------")
    if args.use_words:
        print("Type the words that appear on the screen as fast as you can!")  
        print("\nMode: " + Fore.BLUE + "Words" + Style.RESET_ALL)  
        print("Max number of words: " + Fore.BLUE + str(args.max_value) + Style.RESET_ALL)
        print("Use Time: " + Fore.BLUE + str(args.use_time_mode) + Style.RESET_ALL)
           
    else:
        print("Type the characters that appear on the screen as fast as you can!")
        print("\nMode: " + Fore.BLUE + "Chars" + Style.RESET_ALL)  
        print("Max number of chars: " + Fore.BLUE + str(args.max_value) + Style.RESET_ALL)
        print("Use Time: " + Fore.BLUE + str(args.use_time_mode) + Style.RESET_ALL)
    
    print("-----------------------------------------------------------------")
    
    
    
    print(Fore.LIGHTRED_EX + "Press any key to start!" + Fore.RESET)
    
    key_typed = readchar.readkey()

    if ord(key_typed) != 32:
            
        # Start time info
        start = time.ctime()

        counter = 0

        while True:
            word_cnt = 0
            word_len = 0
            word_full = ""
            if args.use_words:
                r = RandomWords()

                # Generate a random word
                letter_word_requested = r.get_random_word()
                word_len = len(letter_word_requested)
            else:
                # Generate a random letter
                letter_word_requested = fl.carater()
            
            print("------------------------------------------------")
            fl.printer(0, letter_word_requested)
            
            if args.use_words:
                if word_len < 8:
                    print("\n", end = '\t\t')
                else:
                    print("\n", end = '\t')

                t1 = time.time()
                while True:
                    termios.ECHO = True
                    letter_word_received = readchar.readchar()
                    if letter_word_received == readchar.key.SPACE:
                        print("Typing game stopped.")
                        break
                    elif letter_word_received == letter_word_requested[word_cnt]:
                        print(Fore.GREEN + letter_word_received + Style.RESET_ALL, end = '')
                    else:
                        print(Fore.RED + letter_word_received + Style.RESET_ALL, end = '')
                        
                    word_cnt += 1
                    word_full += letter_word_received
                    if word_cnt == word_len:
                        t2 = time.time()
                        letter_word_received = word_full
                        termios.ECHO = False
                        print(" ")
                        break
            else:
                t1 = time.time()
                letter_word_received = readchar.readchar()
                t2 = time.time()

            if letter_word_received == readchar.key.SPACE:
                print("Typing game stopped.")
                break
            
            tf = t2 - t1

            st = 'W' + str(counter+1)
            globals()[st] = words_letter(letter_word_requested, letter_word_received, str(tf))
            dictionary_stat["Inputs"].append([globals()[st]])

            types += 1

            if fl.compare(letter_word_requested, letter_word_received):
                correct += 1
                time_hit += tf
            else:
                incorr += 1
            
            counter += 1
            total_time += tf

            
            if args.use_time_mode and args.max_value < total_time:
                print(" ")
                print('Current test duration (' + str(total_time) + ') exceeds maximum of ' + str(args.max_value))
                break

            elif not args.use_time_mode and args.max_value == types:
                print(" ")
                print('Current test inputs (' + str(types) + ') are equal to ' + str(args.max_value))
                break
        
        end = time.ctime()

        tp_av_dur = fl.average(total_time, types)
        tp_h_av_dur = fl.average(time_hit, correct)
        time_miss = total_time - time_hit
        tp_m_av_dur = fl.average(time_miss, incorr)
        
        dictionary_stat.update({'accuracy' : fl.average(correct, types), 'number of hits' : correct, 'number of types' : types, \
                                'test duration' : total_time, 'test end':end, 'test start' : start, 'type average duration' : tp_av_dur, \
                                'type hit average duration' : tp_h_av_dur, 'type miss average duration' : tp_m_av_dur})
        
        print("\n")
        pprint(dictionary_stat)
    else:
        print('Typing game stopped.')
     
    
if __name__ == '__main__':
    main()
