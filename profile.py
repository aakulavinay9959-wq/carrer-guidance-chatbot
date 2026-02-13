"""
Profile and Authentication module for Career Guidance Chatbot
Handles login, registration, and user profile display
"""

import streamlit as st


def show_login_form():
    """Display login form"""
    st.subheader("🔐 Sign In")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <style>
            .login-container {
                background: linear-gradient(135deg, #f9fff9, #e8f5e9);
                border: 2px solid #2e7d32;
                border-radius: 15px;
                padding: 24px;
                box-shadow: 0 4px 15px rgba(46, 125, 50, 0.1);
            }
            </style>
        """, unsafe_allow_html=True)
        
        email = st.text_input(
            "📧 Email",
            placeholder="example@gmail.com",
            help="Enter your email address"
        )
        
        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Enter your password",
            help="Enter your password"
        )
        
        remember_me = st.checkbox("Remember me")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("🚀 Sign In", use_container_width=True):
                if email and password:
                    st.session_state.user_logged_in = True
                    st.session_state.user_email = email
                    st.success(f"✅ Welcome back, {email.split('@')[0]}!")
                    st.balloons()
                else:
                    st.error("❌ Please enter email and password")
        
        with col_b:
            if st.button("📝 Sign Up", use_container_width=True):
                st.session_state.show_signup = True
        
        st.markdown("---")
        st.markdown("""
            <div style='text-align: center; color: #666; font-size: 14px;'>
            Don't have an account? <b>Click Sign Up</b><br>
            Forgot password? <b>Click Forgot Password</b>
            </div>
        """, unsafe_allow_html=True)


def show_signup_form():
    """Display sign up form"""
    st.subheader("📝 Create Account")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        name = st.text_input("👤 Full Name", placeholder="Your full name")
        
        email = st.text_input("📧 Email", placeholder="your.email@gmail.com")
        
        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Create a password"
        )
        
        confirm_password = st.text_input(
            "🔑 Confirm Password",
            type="password",
            placeholder="Confirm password"
        )
        
        branch = st.selectbox(
            "🏢 Engineering Branch",
            ["Computer Science", "Mechanical", "Electrical", "Civil", "Electronics",
             "Chemical", "Aerospace", "Biomedical", "Other"]
        )
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("✅ Create Account", use_container_width=True):
                if name and email and password and password == confirm_password:
                    st.session_state.user_logged_in = True
                    st.session_state.user_email = email
                    st.session_state.user_name = name
                    st.session_state.user_branch = branch
                    st.success(f"✅ Account created! Welcome {name}!")
                    st.balloons()
                    st.session_state.show_signup = False
                else:
                    st.error("❌ Please check your inputs or passwords don't match")
        
        with col_b:
            if st.button("↩️ Back to Login", use_container_width=True):
                st.session_state.show_signup = False


def show_profile():
    """Display user profile information"""
    st.subheader("👤 My Profile")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <style>
            .profile-card {
                background: linear-gradient(135deg, #f9fff9, #e8f5e9);
                border: 2px solid #2e7d32;
                border-radius: 15px;
                padding: 24px;
                box-shadow: 0 4px 15px rgba(46, 125, 50, 0.1);
            }
            </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style='text-align: center; padding: 20px;'>
                <div style='font-size: 48px; margin-bottom: 10px;'>👤</div>
                <h2 style='color: #2e7d32; margin-bottom: 5px;'>{st.session_state.get("user_name", "User")}</h2>
                <p style='color: #666; font-size: 16px;'>{st.session_state.get("user_email", "Not set")}</p>
                <p style='color: #ff7f11; font-weight: bold;'>📚 {st.session_state.get("user_branch", "Not set")}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### 📊 Profile Stats")
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.metric("Questions Asked", "0")
        
        with col_b:
            st.metric("Paths Explored", "0")
        
        with col_c:
            st.metric("Join Date", "Today")
        
        st.markdown("---")
        
        st.markdown("### ⚙️ Settings")
        
        change_email = st.checkbox("Change Email Address")
        if change_email:
            new_email = st.text_input("📧 New Email", placeholder="new.email@gmail.com")
            if st.button("✅ Update Email", use_container_width=True):
                st.session_state.user_email = new_email
                st.success("✅ Email updated successfully!")
        
        change_branch = st.checkbox("Update Branch")
        if change_branch:
            new_branch = st.selectbox(
                "🏢 Select your branch",
                ["Computer Science", "Mechanical", "Electrical", "Civil", "Electronics",
                 "Chemical", "Aerospace", "Biomedical", "Other"]
            )
            if st.button("✅ Update Branch", use_container_width=True):
                st.session_state.user_branch = new_branch
                st.success("✅ Branch updated successfully!")
        
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.user_logged_in = False
            st.session_state.user_email = None
            st.session_state.user_name = None
            st.success("✅ Logged out successfully!")
            st.rerun()


def show_profile_page():
    """Main profile page handler"""
    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False
    
    if not st.session_state.get("user_logged_in", False):
        if st.session_state.show_signup:
            show_signup_form()
        else:
            show_login_form()
    else:
        show_profile()
