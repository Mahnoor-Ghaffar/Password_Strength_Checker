# Password Strength Checker

A web application built with Streamlit that helps users check the strength of their passwords. The application provides detailed feedback on password strength, including various metrics and suggestions for improvement.

## Features

- Password strength scoring (0-100)
- Detailed password statistics
- Visual strength indicator
- Password requirements checking
- Helpful password tips
- User-friendly interface

## Requirements

- Python 3.7+
- Streamlit
- password-strength package

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)
3. Enter a password in the input field to check its strength
4. View the detailed analysis and suggestions

## Password Requirements

The application checks for the following requirements:
- Minimum length: 8 characters
- At least 1 uppercase letter
- At least 1 number
- At least 1 special character
- At least 1 non-letter character

## Security Note

This application runs locally on your machine and does not store or transmit any passwords. All password analysis is done client-side. 