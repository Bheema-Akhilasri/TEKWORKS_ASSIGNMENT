import streamlit as st
st.header("Shopping bills")
salary=st.number_input("Enter salary",min_value=0  )
shop1=st.number_input("Enter shop 1 bill" ,min_value=0)
shop2=st.number_input("Enter shop 2 bill" ,min_value=0)
shop3=st.number_input("Enter shop 3 bill",min_value=0 )
if st.button("total and percentage"):
    total=shop1+shop2+shop3
    st.write("Total bill",total)
    percentage=(total/salary)*100
    st.write("Percentage",percentage)
