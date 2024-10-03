




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
    # Define carton sizes and corresponding bottle capacities
    carton_sizes = {'XL': 48, 'Large': 24, 'Medium': 12, 'Small': 6}
    
    # Dictionary to store the number of cartons used for each size
    cartons_used = {'XL': 0, 'Large': 0, 'Medium': 0, 'Small': 0}
    
    # Calculate the number of cartons needed for each size in descending order of capacity
    for size, capacity in carton_sizes.items():
        if bottles >= capacity:
            cartons_used[size] = bottles // capacity  # Determine how many cartons of this size are needed
            bottles %= capacity  # Get the remaining bottles that don't fit into this size carton
    
    # Print the break-up of the number of cartons used
    print("Carton Break-up:")
    for size in ['XL', 'Large', 'Medium', 'Small']:
        if cartons_used[size] > 0:
            print(f"{size}: {cartons_used[size]} carton(s)")
    
    if bottles > 0:
        print(f"Remaining bottles: {bottles} (not enough to fill a Small carton)")

bottles =int(input("Enter the total number of bootles: "))
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


    
