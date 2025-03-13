# Password Strength Checker

## Overview
This is a **Streamlit** web application that allows users to check the strength of their passwords, generate strong passwords, and check if a password has been breached using the **Have I Been Pwned API**.

## Features
- **Password Strength Checker**: Evaluates password strength based on length, uppercase letters, numbers, and special characters.
- **Real-Time Feedback**: Displays password statistics and issues found.
- **Breach Check**: Checks if the entered password has been compromised in past data breaches.
- **Password Generator**: Creates strong passwords based on user preferences.
- **Customizable Policy**: Users can adjust password strength requirements (minimum length, uppercase, numbers, and special characters).
- **Password Tips**: Provides guidelines for creating strong passwords.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **PasswordPolicy** (for password validation)
- **PasswordStats** (for strength evaluation)
- **Requests** (for API calls to check breaches)
- **Secrets & String** (for password generation)
- **Hashlib & Re** (for password security and pattern matching)

## Installation
To run this app locally, follow these steps:


cd password-strength-checker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

## Usage
- Enter a password to check its strength.
- Generate a strong password with custom settings.
- Check if your password has been breached.
- View password security tips.

## API Reference
This app uses the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3) to check if a password has been compromised.

## Contributing
Feel free to submit issues or contribute to the project. Fork the repository and create a pull request with your changes.

## License
This project is licensed under the **MIT License**.

---
### Author: *Mahnoor Ghaffar*

