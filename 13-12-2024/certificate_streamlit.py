import streamlit as st

def calculate_results(project, internal, external):
    if project < 50:
        if internal < 50:
            if external < 50:
                return f"Failed in project {project} score, internal {internal} score, and external {external} score."
            else:
                return f"Failed in project {project} score and internal {internal} score."
        else:
            if external < 50:
                return f"Failed in project {project} score and external {external} score."
            else:
                return f"Failed in project {project} score."
    else:
        if internal < 50:
            if external < 50:
                return f"Failed in internal {internal} score and external {external} score."
            else:
                return f"Failed in internal {internal} score."
        else:
            if external < 50:
                return f"Failed in external {external} score."
            else:
                total_marks = project * 0.70 + internal * 0.10 + external * 0.20
                if total_marks >= 90:
                    return 'A grade'
                elif total_marks > 80:
                    return 'B grade'
                else:
                    return 'C grade'


st.title("Student Performance Evaluation")

project = st.number_input("Enter Project score", min_value=0, max_value=100, step=1)
internal = st.number_input("Enter Internal score", min_value=0, max_value=100, step=1)
external = st.number_input("Enter External score", min_value=0, max_value=100, step=1)


if st.button("Evaluate"):
    result = calculate_results(project, internal, external)
    st.info(result)
