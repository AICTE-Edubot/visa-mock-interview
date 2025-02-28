# Visa Mock Interview

## Project Overview
This is a Flask-based web application that simulates a visa interview. Users can select a visa type, answer relevant questions, and view their responses at the end.

## Features
- User can enter personal details (name, age, nationality, visa type)
- Dynamic questions based on selected visa type
- Stores user responses during the session
- Displays results after submission

## Project Structure
```
/visa_mock_interview
├── /static
│   ├── /css
│   │   └── style.css
├── /templates
│   ├── index.html
│   ├── interview.html
│   ├── results.html
├── app.py
├── data.json
```

## Installation and Setup
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/visa-mock-interview.git
cd visa-mock-interview
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```
Activate the virtual environment:
- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
```sh
pip install flask
```

### 4. Run the Application
```sh
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## File Descriptions
- **app.py**: Main Flask application
- **data.json**: Stores visa-related questions
- **templates/**: Contains HTML files for different pages
- **static/css/style.css**: Styles for the web pages

## Technologies Used
- Python (Flask)
- HTML, CSS (Jinja2 for templating)
- JSON (for question storage)



