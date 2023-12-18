import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as ps
import seaborn as sns

from PIL import Image
image_1 = Image.open('school_2.jpg')

def run():
    st.title('***Student Grade*** Analysis')
    
    st.subheader('Analysis Data From Student Grade and Behaviour')
    st.image(image_1,caption="Student Grade")
    
    df = pd.read_csv('student_dataset.csv')
    st.dataframe(df)
    
    st.write('Now before we getting into Visualization Analysis, we must know what these dataframe telling us to do.')
    st.write('As we can see, there one colum that can correlate to the target (Grade) like Attendance, Project Work, and others')
    st.write('Now we can analyze those by looking at these plot')
    st.write('More in the python notebook**')
    
    st.write('# Visualization')
    
    st.write('## Visualization Between Grade and Project Work')
    fig = ps.bar(df, x='Grade', y='Project_work', hover_data=['Grade', 'Project_work'])
    st.plotly_chart(fig)
    st.write('This Visualize the amout of students for each Grade that correlate to Project Work')
    
    st.write('## Visualization Between Grade and Attendance')
    fig = ps.bar(df, x='Grade', y='Attendance', hover_data=['Grade', 'Attendance'])
    st.plotly_chart(fig)
    st.write('This Visualize the amout of students for each Grade that correlate to Attendance')
    
    # Visualization (Active)
    st.write('# Visualization active')
    fig = plt.figure(figsize=(15,5))
    choice = st.selectbox('Select Features: ',
                        ('Grade', 'Attendance', 'Project_work','Listening_in_Class'),
                        help='Select the feature you want to see')
    sns.histplot(df[choice],
                bins=50,
                kde=True)
    st.pyplot(fig)
    st.write("This plot explain about the flow for each features")
if __name__=='__main__':
    run()