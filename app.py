import streamlit as st
import re

def check_password_strength(password):
    strength = "Weak"
    score = 0
    
    # Conditions for strength
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Escaped the double quotes
        score += 1
    
    # Determine strength
    if score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    
    return strength, score

def main():
    st.title("Password Strength Meter.")
    st.markdown("💡 *'A Strong Password is the first step to Digital Security.'*")
    st.write("Enter a Password to Check its Strength.")
    
    password = st.text_input("Enter Password:", type="password")
    
    if password:
        strength, score = check_password_strength(password)
        
        st.subheader(f"Password Strength: {strength}")
        
        # Motivational Quote Based on Strength
        if strength == "Weak":
            st.info("🔴 'A Weak Password is like an Unlocked Door—Secure it before it's too late.'")
        elif strength == "Moderate":
            st.info("🟡 'A Good Password is a Shield; make it Stronger to Guard your data!'")
        else:
            st.info("🟢 'A Strong Password is your Digital Armor—well done!'")
        
        st.progress(score / 5)
        
        # Strength Messages
        if strength == "Weak":
            st.error("Your Password is Weak! Try Adding uppercase, lowercase, numbers, and Special Characters.")
        elif strength == "Moderate":
            st.warning("Your Password is Moderate! Consider Adding more Complexity.")
        else:
            st.success("Your Password is Strong! Well done.")
    
    # Show creator name in the browser
    st.markdown("---")
    st.markdown("Created by A.Salam")
    
if __name__ == "__main__":
    main()