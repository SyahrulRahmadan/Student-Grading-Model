import streamlit as st 
import pickle
import pandas as pd
import numpy as np

def run():
    #title
    st.title('***Testing**** Model Prediction')

    #load
    with open('best_model.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    #Create Form
    with st.form('student_form'):
        Age = st.slider('Input Student Age', 18, 25, 21)
        Sex = st.radio('Input Student Gender', ('Male','Female'), index=1)
        HighSchool = st.radio('Input Student High School Type', ('State', 'Private'), index=1)
        Scholarship = st.radio('Input Student Scholarship Value', ('25%', '50%', '75%', '100%'), index=1)
        AdditionalWork = st.radio('Input Student Additional Work', ('Yes', 'No'), index=1)
        SportActivity = st.radio('Input Student Sport Activites', ('Yes', 'No'), index=1)
        Transportation = st.radio('Input Student Transportation Type', ('Bus', 'Private'), index=1)
        WeeklyStudyHour = st.slider('Input Student Weeklu Study Hour',1, 20, 8)
        Attendance = st.radio('Input Student Attendance', ('Always', 'Sometimes'), index=1)
        Reading = st.radio('Input Student Reading Behaviour', ('Yes', 'No'), index=1)
        Notes = st.radio('Input Student Taking Notes', ('Yes', 'No'), index=1)
        ListeningInClass = st.radio('Input Student Always Listeing In Class', ('Yes', 'No'), index=1)
        ProjectWork = st.radio('Input Student Project Work', ('Yes', 'No'), index=1)
        
        st.markdown('---')

        submitted = st.form_submit_button('Predict')
            
    data = {
        'Student_Age': Age,
        'Sex': Sex,
        'High_School_Type': HighSchool,
        'Scholarship': Scholarship,
        'Additional_Work': AdditionalWork,
        'Sports_activity': SportActivity,
        'Transportation': Transportation,
        'Weekly_Study_Hours': WeeklyStudyHour,
        'Attendance': Attendance,
        'Reading': Reading,
        'Notes': Notes,
        'Listening_in_Class': ListeningInClass,
        'Project_work': ProjectWork
                    }

    data_inf = pd.DataFrame([data])

    st.dataframe(data_inf)

    if submitted:
            # Data Predict
        data_final_pred = model.predict(data_inf)
        data_final_pred
        
        st.write('# Final Grade: ', data_final_pred)

if __name__=='__main__':
    run()
