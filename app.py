import streamlit as st
from password_strength import PasswordPolicy, PasswordStats
import requests
import secrets
import string
import hashlib
import re


# Function to check password strength
def check_password_strength(password, min_length=8, min_uppercase=1, min_numbers=1, min_special=1):
    # Create a password policy
    policy = PasswordPolicy.from_names(
        length=min_length,  # min length
        uppercase=min_uppercase,  # min uppercase letters
        numbers=min_numbers,  # min numbers
        special=min_special,  # min special characters
    )

    # Get password statistics
    stats = PasswordStats(password)
    
    # Check password against policy
    result = policy.test(password)
    
    # Calculate strength score (0-100)
    strength_score = stats.strength() * 100
    
    # Determine strength level
    if strength_score < 30:
        strength_level = "Weak"
    elif strength_score < 60:
        strength_level = "Medium"
    elif strength_score < 80:
        strength_level = "Strong"
    else:
        strength_level = "Very Strong"
    
    return {
        "score": round(strength_score, 2),
        "level": strength_level,
        "length": len(password),
        "uppercase": len(re.findall(r'[A-Z]', password)),
        "lowercase": len(re.findall(r'[a-z]', password)),
        "numbers": len(re.findall(r'[0-9]', password)),
        "special": len(re.findall(r'[^A-Za-z0-9]', password)),
        "issues": [str(error) for error in result]
    }

# Function to check if password has been breached
def check_breach(password):
    # Hash the password using SHA-1 (required by Have I Been Pwned API)
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    # Make a request to the API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    # Check if the suffix exists in the response
    for line in response.text.splitlines():
        if suffix in line:
            return True, int(line.split(':')[1])  # Return True and breach count
    return False, 0  # Return False if no breach found

# Function to generate a strong password
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Main function
def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
    
    st.title("🔒 Password Strength Checker")
    st.write("Enter a password to check its strength, generate a strong password, or check if it has been breached.")
    
    # Customizable password policy
    with st.expander("Customize Password Policy"):
        min_length = st.slider("Minimum Length", 8, 20, 8)
        min_uppercase = st.slider("Minimum Uppercase Letters", 1, 5, 1)
        min_numbers = st.slider("Minimum Numbers", 1, 5, 1)
        min_special = st.slider("Minimum Special Characters", 1, 5, 1)
    
    # Password input with real-time feedback
    password = st.text_input("Enter your password:", type="password", key="password_input")
    
    if password:
        # Check password strength
        result = check_password_strength(password, min_length, min_uppercase, min_numbers, min_special)
        
        # Display strength score with color-coded progress bar
        st.subheader("Password Strength Score")
        st.progress(result["score"] / 100)
        st.write(f"Strength Level: **{result['level']}**")
        
        # Display detailed statistics
        st.subheader("Password Statistics")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"Length: {result['length']} characters")
            st.write(f"Uppercase letters: {result['uppercase']}")
            st.write(f"Lowercase letters: {result['lowercase']}")
        
        with col2:
            st.write(f"Numbers: {result['numbers']}")
            st.write(f"Special characters: {result['special']}")
        
        # Display issues if any
        if result["issues"]:
            st.subheader("Issues Found")
            for issue in result["issues"]:
                st.error(issue)
        else:
            st.success("No issues found! Your password meets all requirements.")
        
        # Check if password has been breached
        st.subheader("Breach Check")
        if st.button("Check if Password Has Been Breached"):
            breached, breach_count = check_breach(password)
            if breached:
                st.error(f"This password has been breached **{breach_count}** times. Do not use it!")
            else:
                st.success("This password has not been breached. It's safe to use.")
    
    # Password generator
    with st.expander("Generate a Strong Password"):
        gen_length = st.slider("Password Length", 8, 20, 12)
        use_uppercase = st.checkbox("Include Uppercase Letters", True)
        use_numbers = st.checkbox("Include Numbers", True)
        use_special = st.checkbox("Include Special Characters", True)
        
        if st.button("Generate Password"):
            generated_password = generate_password(gen_length, use_uppercase, use_numbers, use_special)
            st.text_input("Generated Password", generated_password, key="generated_password")
    
    # Password tips
    with st.expander("Password Tips"):
        st.write("""
        - Use at least 8 characters
        - Include uppercase and lowercase letters
        - Add numbers and special characters
        - Avoid common words and patterns
        - Don't use personal information
        - Use unique passwords for different accounts
        """)

if __name__ == "__main__":
    main()