"""
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_6-5
Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)
hint: test the program on lists of 0,1,2 + lengths, as well as lists that do and do not meet specifications!
"""
def find_min_max(input_list):
    # This checks if the list has 2 unique numbers
    unique_numbers = set(input_list)
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"

    # This finds the max and min of the list
    min_value = min(input_list)
    max_value = max(input_list)

    return min_value, max_value

# Example
numbers = [3, 1, 7, 4, 5, 1, 10]
result = find_min_max(numbers)

print("Result:", result)



________________________________________________________________________________
"""
Create a Python file named lab_6-6

Create a program that asks a user to input 5 unique words.
Construct a list of the 5 input values, in the order that the user gave them.
Have the program display a list where each index corresponds to the length of the word given by the user at the corresponding index.
You may assume accurate input values. NO LOOPS
"""
def construct_word_list():
    # This ask the user to input 5 unique words
    word1 = input("Enter the first unique word: ")
    word2 = input("Enter the second unique word: ")
    word3 = input("Enter the third unique word: ")
    word4 = input("Enter the fourth unique word: ")
    word5 = input("Enter the fifth unique word: ")

    # Construct the list based on the order user used
    word_list = [word1, word2, word3, word4, word5]

    length_list = [len(word) for word in word_list]

    print("User input words:", word_list)
    print("Length of words at corresponding indices:", length_list)
construct_word_list()

_________________________________________________________________________________
"""
Create a Python file named lab_6-7
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display a list with each of the values as integers that have been doubled 
You may assume accurate input values.
"""
def double_numeric_values():
    # This will ask the user to input 3 numeric values
    num1 = float(input("Enter the first numeric value: "))
    num2 = float(input("Enter the second numeric value: "))
    num3 = float(input("Enter the third numeric value: "))
    num_list = [num1, num2, num3]
    doubled_list = [int(2 * num) for num in num_list]
    print("User input values:", num_list)
    print("Doubled values as integers:", doubled_list)
double_numeric_values()

_________________________________________________________________________________
"""
Create a Python file named lab_6-8
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display the string “even” if all numbers in the list are even.
Have the program display the string “odd” if all numbers in the list are odd.
Have the program display the string “mixed” if the numbers in the list are both even and odd.
You may assume accurate input values. You may NOT use a loop. 
"""
def check_numbers():
    # this will ask the user to input 3 numeric values
    num1 = int(input("Enter the first numeric value: "))
    num2 = int(input("Enter the second numeric value: "))
    num3 = int(input("Enter the third numeric value: "))

    # THis construcks a list of the input values in the order given by the user
    num_list = [num1, num2, num3]

    # This checks if all numbers in the list are even, odd, or a mix
    is_all_even = all(num % 2 == 0 for num in num_list)
    is_all_odd = all(num % 2 != 0 for num in num_list)

    if is_all_even:
        print("All numbers are even.")
    elif is_all_odd:
        print("All numbers are odd.")
    else:
        print("Numbers are mixed (both even and odd).")

check_numbers()
