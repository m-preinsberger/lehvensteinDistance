import requests
# This project should be a CLI
# The user should be able to input a string and the nearest

print("Lehvensteinsche distance english dictionary")
input_word  = input("Enter your word!")

# This is from the colab file
online_dictionary = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
response = requests.get(online_dictionary)
words = response.text.split("\n")   

# TODO take the input word and put it on the zero axis of the 2d table 
# TODO iterate over the word list and call a function that takes the 2d table as an param and the second param is the other word in the table
# TODO do that for every word and then return the 10 closest words. 
# TODO print the nearest word

# At first we need the length of the input word so we can create a 2d array with each word combinations
# My first thought is to create a list of 2d arrays that stores the different combinations
# But more on that later, lets get the length of the input first
input_word_length = len(input_word)

# @description This function creates a new metrix of the combinations of two words using the lehvenstein algorithm

def CreateLehvensteinMatrix(word, input_word):
    """
    This function creates a new matrix of the combinations of two words using the Levenshtein algorithm.

    Args:
        word (str): The word to be compared.
        input_word (str): The input word provided by the user; all other words will be compared to this.

    Returns:
        lehvenstein distance(int): This returns the bottom right element of the matrix which is the lehvenstein distance
    """
    # This is my first try implementing a proper function header with the args etc so when hovered over all the infos are shown
    
    cols, rows = (len(word)+1, len(input_word)+1)  # Correct dimensions based on word lengths
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    # Now that we have the 2d array we need to fill it
    # For this we take a double nested for loop with i and j as iterators
    # The information in the classroom are very useful thank you. 
    # QUESTION Why is it called kernel, a kernel is a layer over the hardware so that application can work with the hardware without knowing the design and architecture behind it -> Kernel.png
    # Fill the first row with incrementing values
    for j in range(cols):
        matrix[0][j] = j
    
    # Fill the first column with incrementing values
    for i in range(rows):
        matrix[i][0] = i
    
    # Fill in the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            # Compare characters, if they match we will add no costs
            if input_word[i-1] == word[j-1]:
                additional_cost = 0 # no subsitionion is needed because the values are the same
            else:
                additional_cost = 1
            matrix[i][j] = min(
                matrix[i-1][j] + 1,        # Deletion
                matrix[i][j-1] + 1,        # Insertion
                matrix[i-1][j-1] + additional_cost    # Substitution (or no cost if characters match)
            )
    return matrix[-1][-1]  # Return the bottom-right corner value, which is the Levenshtein distance
# TODO Find closest words
def findClosestWords(input_word, words, top_n=10):
    """
    This function finds the top N clo
    sest words to the input word from a given list of words using the Levenshtein distance.

    Args:
        input_word (str): The word provided by the user to compare against the list of words.
        words (list): A list of words that will be compared to the input word.
        top_n (int, optional): The number of closest words to return, default is 10.

    Returns:
        list: A list of tuples where each tuple contains a word and its Levenshtein distance from the input word.
              The list is sorted by distance in ascending order.
    """

    # We need a list to save the distances we calculated
    distances = []
    # input_length = len(input_word)  # Not needed anymore
    
    # Now we need to iterate over every word in order to calc all the mins
    
    for word in words:
        word = word.strip()  # Remove any extra whitespace or newlines
        if word:
            distance = CreateLehvensteinMatrix(word, input_word)  # Removed input_length parameter
            distances.append((word, distance))
            
    # After we calculated each and every distance we need to sort them so we can output the n closest
    # Sort words by Levenshtein distance (smallest first)
    distances.sort(key=lambda x: x[1]) # this line will sort distances based on the distance values in ascending order.
    
    # the :top_n returns a slice of the distances list, in our case it will return the 10 first elements of the sorted list
    return distances[:top_n]

# After we created the functions we now need to call them
# Find the 10 closest words
closest_words = findClosestWords(input_word, words, top_n=10)

# Print the closest words and their distances
print("The 10 closest words are:")
for word, distance in closest_words:
    print(f"{word}: {distance}")
