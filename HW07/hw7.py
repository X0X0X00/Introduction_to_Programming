"""
Zhenhao Zhang 11/6/23 HW7
"""


"""
This function takes no parameters, but will ask the user for input. For all inputs,
you will need to use an indefinite loop and exception handling like we discussed in
class. It is required to catch user input error and gracefully recover. The only error
you need to consider is a ValueError.
First, it will ask for an integer, n (the number of element in the list)
Then it will ask for n numbers (if a value is given that is a bad input, do not
count that as an element).
Finally, it will ask for a target value (as an integer), k
The function will return the list of integers and k.
"""


def get_input():

    # 第一个
    while True:
        try:
            z_total_number = int(input("Enter the number of integers in the list: "))
            break

        except ValueError:
            print("Bad input!")


    z_number_list = [] # 创建数组

    count = 0

    # 第二个
    while count < z_total_number:
        try:
            z_user_input_numbers = int(input("Enter an integer: "))
            z_number_list.append(z_user_input_numbers)
            count = count + 1

        except ValueError:
            print("Bad input!")


    # 第三个
    while True:
        try:
            z_user_input_target = int(input("Enter the target number: "))
            break

        except ValueError:
            print("Bad input!")

    return z_number_list, z_user_input_target



"""
This function will take two parameters: a list of integers (nums), and a target value
(k). It then will return the number of pairs of numbers in nums that sum to exactly
k.
Hint: try nesting two loops, one keeping track of the first number, one keeping
track of the second number. If you ensure that the second number is always later
than the first number in the list then you won't get duplicate solutions (we should
not count 3 + 7 and 7 + 3 as two separate solutions).
"""

def sum_to_k(nums, k):

    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if int(nums[i]) + int(nums[j]) == int(k):
                count = count + 1

    return count



'''
This mostly links the two above functions together. You will call get_input() and
sum_to_k(nums, k) from main(). It will then print out the number of pairs that sum to k
'''

def main():
    nums, k = get_input()
    z_number_of_pairs_that_sum_to_k = sum_to_k(nums, k)
    print(f"{z_number_of_pairs_that_sum_to_k} pairs sum to {k}")



if __name__ == "__main__":
    main()


