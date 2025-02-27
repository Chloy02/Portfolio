import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import json
import os
import requests
from typing import Optional

def load_lottie_file(filepath: str) -> Optional[dict]:
    """Load a Lottie animation file with error handling"""
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                return json.load(file)
        else:
            st.warning(f"Animation file not found: {filepath}")
            return None
    except Exception as e:
        st.error(f"Error loading animation: {str(e)}")
        return None

def load_lottie_url(url: str) -> Optional[dict]:
    """Load a Lottie animation from URL with error handling"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        return response.json()
    except Exception as e:
        st.error(f"Error loading animation from URL: {str(e)}")
        return None

def contact():
    """Enhanced contact page with better styling and responsiveness"""
    # Apply custom CSS for the contact page
    st.markdown("""
    <style>
        /* Custom styling for the contact page */
        .contact-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        .contact-header {
            color: #2c3e50;
            margin-bottom: 1.5rem;
            text-align: center;
            font-size: 2rem;
            font-weight: 600;
        }
        .contact-description {
            text-align: center;
            color: #555;
            margin-bottom: 2rem;
            line-height: 1.6;
        }
        .contact-methods {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        .contact-method {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1rem;
            border-radius: 8px;
            background-color: #f8f9fa;
            transition: transform 0.3s, box-shadow 0.3s;
            width: 140px;
        }
        .contact-method:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        }
        .contact-icon {
            font-size: 2rem;
            color: #4e89ae;
            margin-bottom: 0.5rem;
        }
        .form-container {
            width: 100%;
            max-width: 768px;
            margin: 0 auto;
            padding: 1rem;
        }
        .centered-iframe {
            display: flex;
            justify-content: center;
            width: 100%;
        }
        @media (max-width: 768px) {
            .contact-methods {
                gap: 1rem;
            }
            .contact-method {
                width: 120px;
                padding: 0.8rem;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Contact header section
    st.markdown("""
    <div class="contact-container">
        <h1 class="contact-header">Get In Touch</h1>
        <p class="contact-description">
            I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.
            Feel free to reach out through any of the methods below or use the contact form.
        </p>
        <div class="contact-methods">
            <div class="contact-method">
                <a href="mailto:Chloy.costa@mca.christuniversity.in" target="_blank" style="text-decoration: none; color: inherit;">
                <i class="fas fa-envelope contact-icon"></i>
                <span>Email</span>
            </div>
            <div class="contact-method">
                <a href="https://www.linkedin.com/in/chloycosta" target="_blank" style="text-decoration: none; color: inherit;">
                <i class="fab fa-linkedin contact-icon"></i>
                <span>LinkedIn</span>
            </div>
            <div class="contact-method">
                <a href="https://github.com/Chloy02" target="_blank" style="text-decoration: none; color: inherit;">
                <i class="fab fa-github contact-icon"></i>
                <span>GitHub</span>
            </div>
            <div class="contact-method">
                <a href="https://www.instagram.com/chloy_costa" target="_blank" style="text-decoration: none; color: inherit;">
                <i class="fab fa-instagram contact-icon"></i>
                <span>Instagram</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Create a two-column layout for the animation and headline
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <div style="background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h2 style="text-align: center; margin-bottom: 1.5rem; color: #2c3e50;">
                <i class="fas fa-paper-plane" style="margin-right: 0.5rem;"></i> Contact Form
            </h2>
            <p style="text-align: center; color: #555; margin-bottom: 1rem;">
                Please fill out the form below, and I'll get back to you as soon as possible!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Load and display the animation in the second column
    with col2:
        try:
            # Try to load the animation file
            animation_data = load_lottie_file("Animation_contact.json")
            
            # If file not found, try to load from a URL as backup
            if animation_data is None:
                animation_data = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_u8ozs4t1.json")
            
            # Display the animation if we have data
            if animation_data:
                st_lottie(
                    animation_data,
                    reverse=True,
                    height=300,
                    width=None,  # Auto width
                    speed=1,
                    loop=True,
                    quality='high',
                    key="contact_animation"
                )
            else:
                # Fallback if no animation data is available
                st.image("https://via.placeholder.com/300?text=Contact+Me", use_column_width=True)
        except Exception as e:
            st.error(f"Failed to display animation: {str(e)}")
            st.image("https://via.placeholder.com/300?text=Contact+Me", use_column_width=True)

    # Contact form section with responsive design
    st.markdown("""
    <div class="form-container">
        <div class="centered-iframe">
    """, unsafe_allow_html=True)
    
    # Embed the Google Form with error handling
    try:
        components.html(
            """
            <iframe 
                src="https://docs.google.com/forms/d/e/1FAIpQLScLaMWyScjbqoo6I5w5MtoQwfSU-Izghn1y_jsTP-yuf5zZOA/viewform?embedded=true" 
                width="100%" 
                height="800" 
                frameborder="0" 
                marginheight="0" 
                marginwidth="0"
                style="max-width: 640px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);"
            >
                Loading form...
            </iframe>
            """,
            height=820,
            width=650,
        )
    except Exception as e:
        st.error(f"Error loading the contact form: {str(e)}")
        st.info("Please try reaching out via email or social media instead.")
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional info section
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; padding: 1rem; color: #666;">
        <p>You can also reach me directly at <b>example@email.com</b></p>
        <p style="font-size: 0.9rem;">I typically respond within 24-48 hours</p>
    </div>
    """, unsafe_allow_html=True)