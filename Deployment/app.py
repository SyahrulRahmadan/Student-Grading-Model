# Import pandas and streamlit
import streamlit as st 

# Import other files in the same folder
import eda
import prediction

# Importing image, nanti tinggal di define aja di bawah
from PIL import Image
image_1 = Image.open('school_1.jpg')

page = st.sidebar.selectbox('Choose Your Page: ',
                            ('Welcome Page', 'EDA', 'Prediction'))

if page == 'Welcome Page':
    st.title('Welcome To Final Grading Prediction Using Fine Tuning K-NN For Education Institution')
    st.image(image_1,caption="Credit Account")
    st.write('')
    st.write('Name      : Syahrul Budi Rahmadan')
    st.write('Batch     : 002 SBY')
    st.write('Objective : create a model that can predict the values determined by the school in order to free up the teachers time for overall assessment.')
    st.write('')
    st.write('Please Select menu on the left bar')
   
    with st.expander('Background'):
        st.caption('One day I, a data scientist, was recruited by a school to work at the school. The school is struggling because the semester is ending. In the even 2023/2024 academic year, the school has 5 times as many students as other schools, but the ratio of teaching staff is very low so they need a data scientist like me to create a program that can predict grades quickly and reliably for the future. If successful, this can increase the productivity level of teaching staff so that they dont have to spend a long time assessing the final grades for each student')
    with st.expander('Goal of this project'):
        st.caption('- Analyze the dataset provided by the school')
        st.caption('- Create a model that can automatically create final grades for students')
        st.caption('- Take up the teachers time to assess each students final grade')
    with st.expander('Problem Statement'):
        st.caption("Can a machine learning predict a student final grade ?")

elif page == 'EDA' :
    eda.run()
    
elif page == 'Prediction' :
    prediction.run()