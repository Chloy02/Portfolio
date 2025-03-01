import streamlit as st
import json
from streamlit_lottie import st_lottie

def load_lottie_animation(path):
    """Safely load a Lottie animation from a JSON file."""
    try:
        with open(path, "r") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading Lottie file: {e}")
        return None

def projects():
    st.markdown("""
        <style>
        .centered {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            margin-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="centered"><h2>Projects</h2></div>', unsafe_allow_html=True)

    lottie_animation = load_lottie_animation("Animation_girl.json")
    if lottie_animation:
        with col2:
            st_lottie(lottie_animation, height=400, width=400, speed=1, loop=True, quality='high')

    st.markdown("---")

    project_data = [
        {
            "title": "Photometric Redshift Estimation using Machine Learning",
            "description": """A research project focused on **estimating photometric redshifts** using a hybrid machine learning approach.
            - **Data Sources:** Sloan Digital Sky Survey (SDSS), JWST, ATLAS.
            - **Feature Engineering:** Extracted flux-based features & color indices.
            - **Clustering Methods:** Implemented K-Means, Gaussian Mixture Models (GMM), and Spectral Clustering.
            - **Regression Models:** Used Random Forest, XGBoost, and LightGBM for redshift estimation.
            - **Final Approach:** Fine-tuned an optimized Stacking Ensemble for the best performance.
            """,
            "tools": ["Python", "Pandas", "Scikit-Learn", "XGBoost", "LightGBM", "Seaborn", "Matplotlib", "Astropy"],
            "links": {
                "GitHub": "https://github.com/Chloy02/Photometric_Redshift_Estimation.git",  
                # "Research Paper": "#",
                "Presentation": "https://1drv.ms/p/c/258e709b69365b6c/EQ5DUGi66ipAlKemr-nWVsgBA1y-tGbdNBzrqYlJySSa2w?e=adOOmp"
            }
        },
        {
            "title": "Transportation and Urban Mobility Analysis",
            "description": """An extensive **exploratory data analysis (EDA)** project using the NYC Yellow Taxi dataset (September 2024) to study urban mobility trends.
            - **Data Preprocessing:** Cleaned and filtered trip data to remove outliers.
            - **Trip Distance Analysis:** Identified key trends in trip distances and durations.
            - **Peak Hour Analysis:** Examined trip patterns across different times of the day.
            - **Fare & Tip Insights:** Investigated fare structures and tipping behaviors.
            - **Statistical Tests:** Conducted hypothesis testing and ANOVA to analyze trip variations.
            """,
            "tools": ["R", "Tidyverse", "ggplot2", "dplyr", "lubridate", "Data Visualization"],
            "links": {
                "GitHub": "https://github.com/Chloy02/Transportation_Analysis.git",  
                "Poster": "https://drive.google.com/file/d/1vBU5rTAlvjB0EcTmzeoQcCKtktbbYZQu/view?usp=sharing"
            }
        }
    ]

    for i in range(0, len(project_data), 2):
        col1, col2 = st.columns(2)
        for idx, col in enumerate([col1, col2]):
            if i + idx < len(project_data):
                project = project_data[i + idx]
                with col:
                    with st.container(border=True):
                        st.title(project["title"])
                        st.markdown(f"**Description:** {project['description']}")
                        st.markdown("**Tools Used:** " + ", ".join(project["tools"]))

                        c1, c2, c3 = st.columns(3)
                        links = list(project["links"].items())
                        for j, col_link in enumerate([c1, c2, c3]):
                            if j < len(links):
                                col_link.markdown(f"**[{links[j][0]}]({links[j][1]})**")

    st.markdown("---")
