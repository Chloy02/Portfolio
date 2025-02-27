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
                "GitHub": "#",  # Replace with actual link
                "Research Paper": "#",
                "Presentation": "#"
            }
        },
        {
            "title": "Uber Data Analysis & Visualization",
            "description": """A **Streamlit-based interactive data exploration app** with AutoML capabilities.
            - **Data Upload & Preprocessing:** Users can upload CSV/Excel files.
            - **AI-Powered Data Insights:** Uses **Google Gemini-1.5-Flash-Latest** for data exploration.
            - **Automated Machine Learning (AutoML)** for model training & optimization.
            - **Visualizations:** Generates charts dynamically using **PygWalker & AutoViz**.
            - **Data Profiling:** Uses **YData Profiling** for deep insights.
            """,
            "tools": ["Python", "Pandas", "Streamlit", "Google Gemini", "PyCaret", "PygWalker", "AutoViz", "YData Profiling"],
            "links": {
                "App": "https://insightful-data-explorer-001.streamlit.app",
                "GitHub": "https://github.com/archanags001/Insightful-Data-Explorer",
                "LinkedIn": "https://www.linkedin.com/feed/update/urn:li:activity:7220172770226102272/",
                "X": "https://x.com/streamlit/status/1814406829075542029",
                "Streamlit Community": "https://buff.ly/3WqhYiB",
                "YouTube": "https://www.youtube.com/watch?v=dwlE4p2uF6k"
            }
        },
        {
            "title": "California Housing Price Prediction",
            "description": """A project predicting housing prices in California using machine learning.
            - **Data Source:** California Housing Dataset.
            - **Regression Models:** Implemented Linear Regression, Decision Trees, Random Forest.
            - **Feature Engineering & Hyperparameter Tuning** to improve accuracy.
            """,
            "tools": ["R"],
            "links": {
                "GitHub": "https://github.com/archanags001/ml_projects/blob/main/California_Housing_Price_Prediction.ipynb"
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

                        c1, c2, c3, c4 = st.columns(4)
                        links = list(project["links"].items())
                        for j, col_link in enumerate([c1, c2, c3, c4]):
                            if j < len(links):
                                col_link.markdown(f"**[{links[j][0]}]({links[j][1]})**")

    st.markdown("---")
