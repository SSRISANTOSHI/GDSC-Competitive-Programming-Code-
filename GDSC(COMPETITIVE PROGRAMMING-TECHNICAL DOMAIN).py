




# Q:Arrange words in a string in the order of their length

def sort_by_word_length(input_string):
    # Split the input string into a list of words
    words = input_string.split()
    
    # Sort the words by their length using the built-in sorted function
    sorted_words = sorted(words, key=len)
    
    # Join the sorted words back into a single string
    return ' '.join(sorted_words)

input_string =input("Enter a string: ")
sorted_string = sort_by_word_length(input_string)
print(sorted_string)





# Q: To remove duplicate elements from a sorted array

def remove_duplicates(sorted_array):
    if not sorted_array:
        return [] # If array is empty, return an empty list
    result=[sorted_array[0]] # Add first element to the result list
    #Traverse the array and check for unique elements
    for i in range(1,len(sorted_array)):
        if sorted_array[i]!=sorted_array[i-1]:
            result.append(sorted_array[i])
    return result
sorted_array=[2,3,4,4,6,7,7]
unique_array=remove_duplicates(sorted_array)
print(unique_array)
remove_duplicates(sorted_array)





# Q: To print the data based on the entered day and year

def is_leap_year(year):
    # Check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year_to_date(day_num, year):
    # Define the days in each month for normal and leap years
    if is_leap_year(year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Leap year
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Non-leap year

    # Check if day number is valid
    max_day = 366 if is_leap_year(year) else 365
    if day_num < 1 or day_num > max_day:
        return "Invalid day number"

    # Determine the month and day
    month = 1
    while day_num > days_in_month[month - 1]:
        day_num -= days_in_month[month - 1]
        month += 1

    # Generate the date string in the format "Day Month Year"
    months_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    return f"{day_num} {months_names[month - 1]} {year}"

day_num = int(input("Enter the day number(between 1 and 365 if it is a non-leap year or between 1 and 366 if it is a leap year): "))
year =int(input("Enter the year: "))
date_string = day_of_year_to_date(day_num, year)
print(date_string)
is_leap_year(year)
day_of_year_to_date(day_num, year)





# Q: The bottle shipping problem

def calculate_cartons(bottles):
    # Carton sizes
    xl = 48
    large = 24
    medium = 12
    small = 6

    # Calculate the number of cartons needed
    count_xl = bottles // xl
    bottles = bottles % xl

    count_large = bottles // large
    bottles = bottles % large

    count_medium = bottles // medium
    bottles = bottles % medium

    count_small = bottles // small
    bottles = bottles % small

    # If there are leftover bottles, add an additional small carton
    if bottles > 0:
        count_small += 1

    # Output the number of cartons used in descending order
    result = []
    if count_xl > 0:
        result.append(f"{count_xl} xl")
    if count_large > 0:
        result.append(f"{count_large} large")
    if count_medium > 0:
        result.append(f"{count_medium} medium")
    if count_small > 0:
        result.append(f"{count_small} small")
    print(", ".join(result))

bottles = int(input("Enter the number of bottles: "))
calculate_cartons(bottles)




# Q: Design your own stack

# Initialize an empty list to represent the stack
stack = []

# Push function to add an element to the stack
def push(stack, value):
    stack.append(value)  # Add element to the end of the list
    print(f"Pushed {value} onto the stack.")

# Pop function to remove and return the top element of the stack
def pop(stack):
    if not is_empty(stack):
        value = stack.pop()  # Remove and return the top element
        print(f"Popped {value} from the stack.")
        return value
    else:
        print("Stack is empty, cannot pop.")
        return None

# Peek function to return the top element without removing it
def peek(stack):
    if not is_empty(stack):
        return stack[-1]  # Return the last element in the list (top of stack)
    else:
        print("Stack is empty, nothing to peek.")
        return None

# Helper function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

push(stack,10)
push(stack,20)
push(stack,30)

print("Top element (peek):", peek(stack)) 

pop(stack)  # Should remove 30
pop(stack)  # Should remove 20

print("Top element (peek):", peek(stack))  # Should print 10

pop(stack)  # Should remove 10
pop(stack)  # Should print that the stack is empty


    
