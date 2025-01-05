# Crossfit WODs Web App

This is a Flask web application that lists Crossfit WOD (Workout of the Day) files from a `data` directory (web scraped from https://rxinfinitybox.com/). Each file is viewable via dynamically generated links.

## Features
- Displays a list of HTML files from the `data` directory.
- Dynamically renders the content of selected WOD files.
- Responsive design with centered content.
- Simple navigation for browsing WOD files.

---

## Prerequisites

- Python 3.10 or later
- Flask (install using `pip install flask`)

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. Install the required dependencies:
    ```bash
    pip install flask
    ```

## Directory Structure
```bash
.
├── app.py             # Main Flask application
├── data               # Directory containing WOD files (HTML)
│   ├── 2022-06-21.html
│   ├── ...
├── static             # Directory for static files (CSS, JS, images)
│   └── styles.css
├── templates          # Directory for Jinja2 templates
|   ├── base.html
│   ├── index.html
│   └── data_template.html
└── README.md          # Documentation for the app
```

## Usage

1. Start the Flask development server:
    ```bash
    python app.py
    ```
2. Open the app in your browser:
    ```bash
    http://127.0.0.1:5000
    ```