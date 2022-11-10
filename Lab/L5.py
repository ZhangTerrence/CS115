############################################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 5
############################################################
import time

words = []
HITS = 10

memo = {}
def fastED(first, second):
    """Returns the edit distance between the strings first and second. Uses memoization to speed up the process.
    Returns the edit distance between the strings first and second"""
    if (first, second) in memo:
        return memo[(first, second)]
    elif first == "":
        memo[(first, second)] = len(second)
        return len(second)
    elif second == "":
        memo[(first, second)] = len(first)
        return len(first)
    elif first[0] == second[0]:
        memo[(first, second)] = fastED(first[1:], second[1:])
        return memo[(first, second)]
    else:
        substitute = 1 + fastED(first[1:], second[1:])
        delete = 1 + fastED(first[1:], second)
        insert = 1 + fastED(first, second[1:])
        memo[(first, second)] = min(substitute, delete, insert)
        return memo[(first, second)]

def getSuggestions(user_input):
    """For each word in the global words list, determine the edit distance of the user_input and the word. Return a
    list of tuples containing the (edit distance, word). Hint: Use map and lambda, and it's only one line of code!"""
    return list(map(lambda x: (fastED(x, user_input), x), words))

def spam():
    """Main loop for the program that prompts the user for words to check. If the spelling is correct, it tells the
    user so. Otherwise, it provides up to HITS suggestions.
    To exit the loop, just hit Enter at the prompt"""
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
