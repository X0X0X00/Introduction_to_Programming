# Zhenhao Zhang 10/15/23

"""
Homework 5
Zhenhao Zhang
"""


def square_each(nums):

    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):

    sum_number = 0
    for i in range(len(nums)):
        sum_number = sum_number + nums[i]

    return sum_number



def to_numbers(str_list):

    i = 0

    while i < len(str_list):
        # If the line is empty or just whitespace, remove it
        if str_list[i].strip() == "":
            str_list.pop(i)
        else:
            str_list[i] = int(str_list[i].strip())
            i += 1


def main():

    # Prompt for a file name
    file_name = input("Please enter the file name: ")

    try:
        with open(file_name, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Convert string lines to numbers
            to_numbers(lines)

            # Square each number
            square_each(lines)

            # Compute the sum of squared numbers
            result = sum_list(lines)

            print(f"The sum of the squares of the numbers in the file is {result}")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()