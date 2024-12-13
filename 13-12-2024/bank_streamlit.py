import streamlit as st

class Bank:
    if "accbal" not in st.session_state:
        st.session_state.accbal = 10000
    if "num" not in st.session_state:
        st.session_state.num = 0
    if "pin" not in st.session_state:
        st.session_state.pin = 1234
    if "pin_no" not in st.session_state:
        st.session_state.pin_no = 0

    def deposit(self, deposit_amount):
        if 50000 >= deposit_amount >= 100 and deposit_amount % 100 == 0:
            st.session_state.accbal += deposit_amount
            return f"Deposit successful! New balance: {st.session_state.accbal}"
        else:
            return "Deposit amount should be between 100 and 50k, and in multiples of 100."

    def withdraw(self, withdraw_amount):
        if st.session_state.num < 3:
            if (20000 >= withdraw_amount >= 100 and withdraw_amount % 100 == 0 and withdraw_amount < st.session_state.accbal):
                if st.session_state.accbal - withdraw_amount >= 500:
                    st.session_state.accbal -= withdraw_amount
                    st.session_state.num += 1

                    notes = ""
                    for denom in [500, 200, 100]:
                        if withdraw_amount >= denom:
                            count = withdraw_amount // denom
                            notes += f"{denom} notes: {count}\n\n"
                            withdraw_amount %= denom

                    return f"Withdraw successful!\n\n{notes}New balance: {st.session_state.accbal}"
                else:
                    return "Minimum balance must remain above 500."
            else:
                return (
                    "Withdraw amount should be a minimum of 100, a maximum of 20k, "
                    "and less than the account balance."
                )
        else:
            return "You have exceeded the daily transaction limit of 3 withdrawls."

# Streamlit app implementation
st.title("Banking Application")

# Create a Bank object
bank = Bank()

# Login validation
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:

    pin_input = st.text_input("Enter your PIN", type="password")
    if st.session_state.pin_no < 3:
        if st.button("Login"):
            if pin_input and int(pin_input) == st.session_state.pin:
                st.session_state.authenticated = True
                st.success("Login successful!")

            else:
                st.error(f"Invalid PIN, Please try again.You have {3-st.session_state.pin_no} chances left")
                st.session_state.pin_no +=1
    else:
        st.info('Maximum Attempts reached try again after sometime')
else:
    if st.session_state.authenticated:
        option = st.radio(
            "Choose an option:", ["Deposit", "Withdraw", "Balance Enquiry", "Exit"]
        )
        # st.write('1.Deposit\n\n2.Withdraw\n\n3.Bal Enquiry\n\n0.Exit\n\n')
        # option=st.number_input("Choose your option",step=100)
        # while(option<4):
        match option:
            case "Deposit":
                deposit_amount = st.number_input("Enter deposit amount", step=100)
                if st.button("Submit Deposit"):
                    result = bank.deposit(deposit_amount)
                    st.info(result)

            case "Withdraw":
                withdraw_amount = st.number_input("Enter withdraw amount", step=100)
                if st.button("Submit Withdrawl"):
                    result = bank.withdraw(withdraw_amount)
                    st.info(result)

            case "Balance Enquiry":
                st.info(f"Your current balance is: {st.session_state.accbal}")

            case "Exit":
                st.session_state.authenticated = False
                st.info("You have been logged out.")

