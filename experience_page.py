import streamlit as st
from streamlit_lottie import st_lottie
import json

def experience():
    # Header section with animation
    st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>Professional Experience</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <style>
            .experience-intro {
                display: flex;
                flex-direction: column;
                justify-content: center;
                height: 100%;
                padding: 20px;
                border-radius: 10px;
                background-color: rgba(240, 240, 240, 0.2);
                margin-top: 50px;
            }
            </style>
            <div class="experience-intro">
                <h3>Building My Professional Journey</h3>
                <p>I am currently focused on developing my skills in data science and machine learning through 
                projects, coursework, and self-study. As I work toward building industry experience,
                I am passionate about applying my technical knowledge to create innovative solutions.</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Load animation
    path = "Animation_exp.json"
    with open(path, "r") as file:
        url = json.load(file)
    
    with col2:
        st_lottie(url,
                  reverse=True,
                  height=400,
                  width=400,
                  speed=1,
                  loop=True,
                  quality='high',
                  )
    
    # Custom CSS for experience cards
    st.markdown("""
        <style>
        .experience-card {
            border-left: 4px solid #2e6eff;
            padding-left: 20px;
            margin-bottom: 30px;
            background-color: rgba(240, 240, 240, 0.1);
            border-radius: 5px;
            padding: 20px;
            transition: transform 0.3s;
        }
        .experience-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .tools-section {
            background-color: rgba(46, 110, 255, 0.1);
            border-radius: 5px;
            padding: 15px;
        }
        .placeholder-message {
            text-align: center;
            padding: 50px 20px;
            background-color: rgba(240, 240, 240, 0.1);
            border-radius: 10px;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Skills showcase section
    st.markdown("<h2 style='text-align: center; margin: 30px 0;'>Technical Skills</h2>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
            <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: rgba(46, 110, 255, 0.1);">
                <h3 style="margin-bottom: 10px;">Programming</h3>
                <p>Python, SQL, R, Java, C, Kotlin, JavaScript, HTML </p>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
            <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: rgba(46, 110, 255, 0.1);">
                <h3 style="margin-bottom: 10px;">Data Science</h3>
                <p>Machine Learning, Data Analysis, Statistics, Maths </p>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
            <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: rgba(46, 110, 255, 0.1);">
                <h3 style="margin-bottom: 10px;">Tools</h3>
                <p>Pandas, Numpy, Scikit-learn, TensorFlow, Matplotlib</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Education section
    st.markdown("<h2 style='text-align: center; margin: 30px 0;'>Education</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="experience-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 3])
        
        with col1:
            st.markdown("""
                ### FR. Agnel Multipurpose higher secondary school
                **Science Stream Physics, Chemistry, Mathematics, Biology**
                
                - Relevant coursework: Data Structures, Algorithms, Machine Learning, Statistics
                - GPA: 3.8/4.0 (or your actual GPA)
                - Participated in hackathons and coding competitions
            """)
        
        with col2:
            st.markdown("""
                <div class="tools-section">
                <h4>Graduation:</h4>
                May 2023 (or your actual date)
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        with col1:
            st.markdown("""
                ### Parvatibai Chowgule College of Arts and Science
                **Bachelor of Science in Physics**
                
                - Relevant coursework: Data Structures, Algorithms, Machine Learning, Statistics
                - GPA: 3.8/4.0 (or your actual GPA)
                - Participated in hackathons and coding competitions
            """)
        
        with col2:
            st.markdown("""
                <div class="tools-section">
                <h4>Graduation:</h4>
                May 2023 (or your actual date)
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        with col1:
            st.markdown("""
                ### Christ Deemed to be University
                **Masters of Computer Application**
                
                - Relevant coursework: Data Structures and Algorithms, Statistics in R, Advanced Python, Data Mining
                - Currently pursuing
            """)
        
        with col2:
            st.markdown("""
                <div class="tools-section">
                <h4>Graduation:</h4>
                May 2023 (or your actual date)
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="experience-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
                ### Personal Project 1
                
                - Developed a machine learning model to predict [specific outcome]
                - Implemented data preprocessing and feature engineering techniques
                - Achieved 85% accuracy on test data
                - Technologies used: Python, scikit-learn, pandas, matplotlib
            """)
        
        with col2:
            st.markdown("""
                <div class="tools-section">
                <h4>Technical Toolkit:</h4>
                
                - 💻 **Languages**: Python
                - 🧠 **ML**: Scikit-Learn
                - 📊 **Visualization**: Matplotlib, Seaborn
                - 📈 **Data**: Pandas, NumPy
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        
        with col1:
            st.markdown("""
                ### Personal Project 2
                
                - Created a web application for [specific purpose]
                - Designed and implemented the database schema
                - Built an interactive dashboard to visualize results
                - Technologies used: Flask, SQLite, HTML/CSS, JavaScript
            """)
        
        with col2:
            st.markdown("""
                <div class="tools-section">
                <h4>Technical Toolkit:</h4>
                
                - 💻 **Languages**: Python, JavaScript, HTML/CSS
                - 🌐 **Web**: Flask
                - 🗄️ **Database**: SQLite
                - 📊 **Frontend**: Bootstrap
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Certifications
    st.markdown("<h2 style='text-align: center; margin: 30px 0;'>Certifications</h2>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    
    with cols[0]:
        st.markdown("""
            <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: rgba(46, 110, 255, 0.1);">
                <h3 style="margin-bottom: 10px;">Data Science Professional Certificate</h3>
                <p>Provider: Coursera / IBM / etc.</p>
                <p>Completed: January 2023</p>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
            <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: rgba(46, 110, 255, 0.1);">
                <h3 style="margin-bottom: 10px;">Machine Learning Specialization</h3>
                <p>Provider: Coursera / Stanford / etc.</p>
                <p>Completed: June 2023</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; padding: 30px; background-color: rgba(46, 110, 255, 0.05); border-radius: 10px;">
            <h3>Looking for Opportunities</h3>
            <p>I am currently seeking entry-level positions or internships in data science and machine learning.
            Please reach out if you'd like to connect!</p>
        </div>
    """, unsafe_allow_html=True)