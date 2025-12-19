# Expense Tracker (Streamlit)

A simple and interactive **Expense Tracker web application** built using **Python and Streamlit**.  
This app allows users to add daily expenses, categorize them, and visualize spending patterns.

---

## Features

- Add expenses with name, amount, date, and category
- View all expenses in a table
- See total spending
- Category-wise expense visualization
- Daily spending trend visualization
- Clear all expenses with one click
- Uses session state (data persists during app runtime)

---

## Tech Stack

- Python
- Streamlit
- Pandas

---

## How to Run the App Locally

### Prerequisites
- Python 3.8 or higher
- pip installed

---

### 1. Clone the Repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
### 2. Create and Activate a Virtual Environment
python -m venv venv
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Run the application
streamlit run app.py
### 5. Open in Browser
The app will automatically open 

---

## Notes

- This application uses **Streamlit session state** to store expense data temporarily.
- All data is cleared when the app is refreshed or restarted.
- The project is designed as a **beginner-friendly implementation** to learn Streamlit and frontend integration with Python.

---

## Future Improvements

- Add persistent storage using a database or CSV file
- Implement user authentication
- Include monthly and yearly expense summaries
- Enable exporting expenses as a CSV file

---

## Key Learnings

- Built a complete frontend application using Streamlit
- Implemented structured user input using Streamlit forms
- Managed application state with `st.session_state`
- Performed data manipulation and grouping using Pandas
- Created basic data visualizations for expense analysis
- Designed a clean and user-friendly layout using Streamlit components

---
