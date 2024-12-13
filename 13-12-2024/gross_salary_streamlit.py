import streamlit as st
st.title('Gross Salary')
basic_salary=st.number_input('Enter Basic Salary',step=100)
if st.button('Gross Salary'):
    if basic_salary < 10000:
        hra = basic_salary * 0.67
        da = basic_salary * 0.73
    elif basic_salary < 20000:
        hra = basic_salary * 0.69
        da = basic_salary * 0.76
    else:
        hra = basic_salary * 0.73
        da = basic_salary * 0.89
    gross_salary = hra+da+basic_salary
    st.write("Gross Salary : ", gross_salary)