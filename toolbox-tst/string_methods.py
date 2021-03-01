# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    return ', '.join(a_string.split()) # or a_string.replace(' ', ', ')

def belongs_to(a_string, a_word):
    return a_word in a_string

def count_repetition(a_string, a_substring):
    return a_string.count(a_substring)

def is_a_question(a_string):
    return a_string.endswith('?')

def remove_surrounding_whitespaces(a_string):
    return a_string.strip()

def replace(initial_string, old_letter, new_letter):
    return initial_string.replace(old_letter, new_letter)

def full_description_concatenation(first_name, last_name, age):
    return first_name.capitalize() + ' ' + last_name.capitalize() + ' is ' + str(age)

def full_description_formatting(first_name, last_name, age):
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
