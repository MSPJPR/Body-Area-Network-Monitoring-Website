Body Area Network Monitoring Website

A simulated monitoring website for Body Area Networks (BAN), specifically designed for healthcare applications. This project allows users to view and analyze health data simulated from BAN sensors on a clean, responsive interface.

Features

Simulated Health Data Monitoring: Display health metrics like heart rate, temperature, and more.

User-Friendly Interface: Organized layout for easy navigation and readability.

Responsive Design: Works well on desktop and mobile devices.


Technologies Used

HTML/CSS: Basic structure and styling for the website.

JavaScript: Fetching and displaying simulated data from sensors.

Python (Flask): Backend server (if needed) for handling data and API requests.


Requirements

Termux installed on your mobile device

Python 3.8 or higher

Flask (optional, if backend processing is required)


Setup Instructions

1. Install Termux and Set Up Environment

1. Install Termux on your Android device.


2. Open Termux and update package lists:

pkg update && pkg upgrade


3. Install Python:

pkg install python


4. (Optional) Install Flask for backend:

pip install flask



2. Clone the Repository

1. Clone your GitHub repository:

git clone https://github.com/your-username/your-repo-name.git


2. Navigate to the project folder:

cd your-repo-name



3. Run the Project

1. If running as a static site, open index.html in a browser.


2. For running with Flask (if you have a backend):

python app.py



4. Access the Website

Open a browser and go to http://localhost:5000 (if using Flask).

If using a static HTML page, you can directly open the index.html file in a browser.


Project Structure

.
├── index.html              # Main HTML file
├── static/
│   ├── style.css           # Stylesheet
│   └── scripts.js          # JavaScript for fetching/displaying simulated data
└── app.py                  # Flask server (optional)

Usage

1. Open the website and monitor simulated health data.


2. You can adjust the data values in the code to simulate various health conditions.
