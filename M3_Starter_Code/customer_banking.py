# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please input balance:"))
    savings_interest = float(input("Please input interest rate:"))
    savings_maturity = int(input("Please input number of months:"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('The interest earned on the savings account is: $', format(interest_earned, ',.2f'))
    print('The future savings account balance after',savings_maturity,'months is: $', format(updated_savings_balance, ',.2f'))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Please input balance:"))
    cd_interest = float(input("Please input interest rate:"))
    cd_maturity = float(input("Please input the number of months:"))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print('The interest earned on the cd acount is: $', format(cd_interest, ',.2f'))
    print('The future savings account balance after',cd_maturity,'month is: $', format(updated_cd_balance, ',.2f'))

if __name__ == "__main__":
    # Call the main function.
    main()