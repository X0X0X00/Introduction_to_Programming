# Zhenhao Zhang 10/31/23 zzh133@u.rochester.edu


'''
test cases:
• 585-500-5432 (valid /from Rochester area)
• 500-500-5432 (valid /not from Rochester area) • 500-500-543 (not valid)
• CSC-161-1234 (not valid)
• 585-1633-1234 (not valid)
• 585633-1234 (not valid)
• 585-1633-1234 (not valid)
• Homework 161 (not valid)
'''



def is_valid(phone_number):
    # 先通过“-”分块
    # number_sections contains the split the phone number into its sections
    Zhang_number_sections = phone_number.split('-')

    # 如果没有三个部分 直接报错
    if len(Zhang_number_sections) != 3:
        return False

    """
    z_area_number 将获得 Zhang_number_sections 的第一个元素。
    Z_middle_number 将获得 Zhang_number_sections 的第二个元素。
    h_last_number 将获得 Zhang_number_sections 的第三个元素。
    """
    z_area_number, Z_middle_number, h_last_number = Zhang_number_sections

    # get length
    Z_area_number_length = len(z_area_number)
    z_middle_number_length = len(Z_middle_number)
    H_last_number_length = len(h_last_number)

    # 判断 并且返回 XXX-XXX-XXXX
    return all([Z_area_number_length == 3, z_area_number.isdigit(),
                z_middle_number_length == 3, Z_middle_number.isdigit(),
                H_last_number_length == 4, h_last_number.isdigit()])


def is_Rochester(phone_number):

    # [:3]第一位到第三位
    return phone_number[:3] == "585"


def main():
    # Get the phone number from the user
    ZZH_phone_number = input("Please enter a phone number in format XXX-XXX-XXXX: ")

    # Check if the phone number is valid
    if is_valid(ZZH_phone_number):
        print(f"{ZZH_phone_number} is valid")

        if is_Rochester(ZZH_phone_number):
            print(f"{ZZH_phone_number} is from Rochester area")

    else:
        print(f"{ZZH_phone_number} is not valid")


if __name__ == "__main__":
    main()
