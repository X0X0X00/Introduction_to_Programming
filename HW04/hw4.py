"""
Zhenhao Zhang zzh133@u.rochester.edu 32277234 HW4
"""

def main():

    # Ask user to input the correct file name
    filename = input("Please enter the filename of the financial data: ")
    print()  # Adding a newline

    # Open and read the file
    with open(filename, 'r') as testfile:


        principal = testfile.readline().split()[1].strip()
        principal = float(principal)
        print(f"The initial principal is: ${principal}")

        interest = testfile.readline().split()[1].strip()
        interest = float(interest)
        print("Annual percentage rate is: {:.1f}%".format(interest *100))


        term = testfile.readline().split()[1].strip()
        term = int(term)
        print(f"Length of the term: {term}")

        balances = [principal] + [float(line.strip()) for line in testfile]

    print()

    print(f"{'Year':>4} {'Value':>5}")

    # for year, balance in enumerate(balances):
    #     print(f"{year:>4} ${balance:>7.2f}")

    for i in range(11):
        print(f"{i:>4} {balances[i]:>7.2f}")
        i += 1



    testfile.close()
main()

















































