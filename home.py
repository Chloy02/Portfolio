import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import requests
import json
import os
from reume_page import resume
from experience_page import experience
from upwork_page import feedbackRating
from project_page import projects
from contact_form import contact

# Page setup with improved configuration
st.set_page_config(
    page_title="Chloy Costa | Portfolio",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Chloy02',
        'Report a bug': 'https://github.com/Chloy02',
        'About': "# Chloy Costa's Portfolio\nData Scientist and Developer"
    }
)

# Add custom CSS
st.markdown("""
<style>
    /* Adaptable background */
    .main {
        background-color: transparent;
    }

    /* Universal font and adaptable text color */
    .stApp {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: inherit;
    }

    /* Sidebar adjustments */
    .stSidebar {
        background-color: #1a1a1a;
    }

    /* Headers inherit theme color */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 600;
        color: inherit;
    }

    /* Custom card styling */
    .custom-card {
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: rgba(255, 255, 255, 0.8); /* Slight transparency for dark mode */
        margin-bottom: 20px;
        color: inherit;
    }

    /* Sidebar text styling */
    .sidebar-text {
        color: inherit;
        text-align: center;
        padding: 10px 0;
    }

    /* Link styles */
    a {
        text-decoration: none;
        font-weight: 500;
        color: inherit;  /* Adapt to theme */
        transition: color 0.3s;
    }

    a:hover {
        color: #4e89ae;
    }

    /* Social icons */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 15px;
    }

    .social-icon {
        font-size: 24px;
        transition: transform 0.3s;
        color: inherit;
    }

    .social-icon:hover {
        transform: scale(1.2);
    }

    /* Sidebar navigation */
    .stSidebar .stButton>button {
        color: inherit;
    }

    /* Footer */
    footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        border-top: 1px solid #ddd;
        color: inherit;
    }
</style>
""", unsafe_allow_html=True)


# Improved gradient function with better styling
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'''
    <div style="background-image: linear-gradient(to right,{color1}, {color2}); 
                padding: 20px; 
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                text-align: center;">
        <h1 style="color:{color3}; font-size: 48px; margin-bottom: 10px;">{content1}</h1>
        <p style="color:white; font-size: 18px;">{content2}</p>
    </div>
    ''', unsafe_allow_html=True)

# Enhanced about me section with better formatting
def about_me():
    # Header section
    gradient("#4e89ae", "#43658b", "white", "Chloy Costa", "Data Scientist & Developer")
    
    # Main content
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Hello! I'm Chloy Costa! 👋</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: justify; line-height: 1.6;">
            <p>I am a developer with a strong analytical mindset, combining my background in Physics with a Master's in Computer Applications. 
            My transition from scientific problem-solving to software development has given me a unique perspective on tackling complex challenges 
            with logic and creativity.</p>
            <p>I have a deep interest in machine learning and data science, always striving to build efficient and impactful solutions. 
            Whether it's writing clean code, optimizing algorithms, or crafting user-friendly applications, I enjoy the process of learning and improving.</p>
            <p>Beyond tech, I value deep connections, creative expression, and personal growth, which shape both my professional and personal pursuits.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Skills section
        st.markdown("<h3>Technical Skills</h3>", unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("**Languages**")
            st.markdown("- Python\n- SQL\n- R")
        with col_b:
            st.markdown("**Data Science**")
            st.markdown("- Machine Learning\n- Statistical Analysis\n- Data Visualization\n- Deep Learning")
        with col_c:
            st.markdown("**Tools**")
            st.markdown("- Streamlit\n- TensorFlow\n- PyTorch\n- Pandas/NumPy\n - Scikit-Learn\n - Matplotlib/Seaborn")
        
        # Social links with icons
        st.markdown("<div class='social-icons'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.markdown("""<a href="https://github.com/Chloy02" target="_blank"><i class="fab fa-github social-icon"></i> GitHub</a>""", unsafe_allow_html=True)
        c2.markdown("""<a href="https://www.linkedin.com/in/chloycosta" target="_blank"><i class="fab fa-linkedin social-icon"></i> LinkedIn</a>""", unsafe_allow_html=True)
        c3.markdown("""<a href="https://www.instagram.com/chloy_costa" target="_blank"><i class="fab fa-instagram social-icon"></i> Instagram</a>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Animation column
    with col2:
        st.markdown('<div class="custom-card" style="height: 100%;">', unsafe_allow_html=True)
        # Try to load animation from local file, with fallback to URL
        try:
            path = "Animation_blue_robo.json"
            if os.path.exists(path):
                with open(path, "r") as file:
                    animation_data = json.load(file)
            else:
                # Fallback to a default Lottie animation URL if file not found
                animation_data = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qp1q7sce.json")
                
            st_lottie(
                animation_data,
                reverse=True,
                height=400,
                width=None,
                speed=1,
                loop=True,
                quality='high',
                key="main_animation"
            )
        except Exception as e:
            st.error(f"Could not load animation: {e}")
            # Display a placeholder image if animation fails
            st.image("https://via.placeholder.com/400", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Improved function to load Lottie animations from URL with error handling
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return r.json()
    except Exception as e:
        st.error(f"Error loading animation: {e}")
        return None

# Enhanced base64 image loading with error handling
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# Set up the sidebar with improved styling
try:
    # Get the base64 string of the image with fallback
    logo_base64 = get_base64_image("Me.jpg")
    
    if logo_base64:
        # Logo styling
        logo_html = f"""
            <style>
            .logo-container {{
                display: flex;
                justify-content: center;
                margin: 20px 0;
            }}
            .logo {{
                width: 120px;
                height: 120px;
                border-radius: 50%;
                object-fit: cover;
                border: 3px solid #4e89ae;
                transition: transform 0.3s;
            }}
            .logo:hover {{
                transform: scale(1.05);
            }}
            </style>
            <div class="logo-container">
                <img src="data:image/jpeg;base64,{logo_base64}" class="logo" alt="Chloy Costa">
            </div>
        """
        
        # Display logo in the sidebar
        st.sidebar.markdown(logo_html, unsafe_allow_html=True)
    else:
        # Fallback if image can't be loaded
        st.sidebar.markdown("### Chloy Costa")
except Exception as e:
    st.sidebar.error(f"Error displaying profile image: {e}")

# Add FontAwesome for icons
st.sidebar.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <div class="sidebar-text">
        <p>Data Scientist & Developer</p>
        <p>Master's in Computer Applications</p>
    </div>
""", unsafe_allow_html=True)

# Option menu in sidebar with improved styling
with st.sidebar:
    pages = ["About Me", "Resume", "Experience", "Projects", "Contact"]
    icons = ['person-fill', 'file-text', 'briefcase', 'folder', 'envelope']
    
    nav_tab_op = option_menu(
        menu_title="Navigation",
        options=pages,
        icons=icons,
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#1a1a1a"},
            "icon": {"color": "#4e89ae", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#2c3e50"
            },
            "nav-link-selected": {"background-color": "#4e89ae"},
        }
    )

# Main content of the app with error handling
try:
    if nav_tab_op == "About Me":
        about_me()
    elif nav_tab_op == "Resume":
        resume()
    elif nav_tab_op == "Experience":
        experience()
    elif nav_tab_op == "Testimonials":
        feedbackRating()
    elif nav_tab_op == "Projects":
        projects()
    elif nav_tab_op == "Contact":
        contact()
except Exception as e:
    st.error(f"An error occurred loading the {nav_tab_op} page: {e}")
    st.info("Please make sure all required modules and files are available.")

# Footer section
st.markdown("""
<footer style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #ddd;">
    <p>© 2025 Chloy Costa. All rights reserved.</p>
    <p style="font-size: 14px; color: #666;">Built with Streamlit & ❤️</p>
</footer>
""", unsafe_allow_html=True)