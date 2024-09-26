# BootBuddy - Bootcamp Administration Tool

**BootBuddy** is a lightweight web application designed to streamline content delivery and participant management during bootcamps. It allows bootcamp participants to access curated content, while mentors (admins) can manage teams, feedback, and content through embedded Google Docs. This project focuses on delivering an MVP with a clean and functional experience for users.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

### For Bootcamp Participants:
- **Login/Signup**: Users can log in to access bootcamp content.
- **Dashboard**: The main dashboard displays curated content depending on the bootcamp day.
- **Content Delivery**: Content is embedded from Google Docs, including text, images, videos, and links to Google Forms for quizzes.

### For Admins (Mentors):
- **Team Management**: Admins can view which mentors are assigned to which groups (coming soon).
- **Feedback Collection**: Admins can receive feedback from participants (coming soon).
- **Content Management**: Admins can update the Google Docs that are embedded in the participants' dashboard.

## Tech Stack

### Frontend:
- **Streamlit**: For building the interactive web interface.
- **Google Docs API**: To embed Google Docs content in the dashboard.

### Backend:
- **Streamlit Session State**: Manages user sessions (login/logout).
- **MySQL**: Database for storing participant and admin data (future enhancement).
  
### Deployment:
- **Streamlit Community Cloud**: Used for deploying the MVP.

## Setup and Installation

### Prerequisites
- Python 3.8+
- Pip (Python package manager)
- Streamlit installed (`pip install streamlit`)
- A Google account with access to the Google Docs API

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bootbuddy.git
    cd bootbuddy
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Google Docs API credentials:
    - Follow [Google's guide](https://developers.google.com/docs/api/quickstart/python) to enable the Google Docs API and obtain your credentials.
    - Save your credentials in the project root as `credentials.json`.

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## How to Use

### For Participants:
1. **Login**: Use the provided login form to access your dashboard.
2. **View Content**: On your dashboard, you will see content based on the current day of the bootcamp. This content is embedded directly from Google Docs.
3. **Complete Quizzes**: Links to quizzes (Google Forms) will be embedded in the Google Docs content.

### For Admins:
1. **Login**: Admins can log in using a special account.
2. **Manage Content**: Use Google Docs to curate content that will be shown on the participant dashboards.
3. **View Teams & Feedback**: Features for managing teams and receiving feedback are coming soon.

## Future Enhancements
- **Admin Interface**: The MVP focuses on the participant experience, but future iterations will include a full admin interface.
- **Team and Feedback Management**: The ability for admins to manage teams and receive participant feedback will be added.
- **Google Forms Integration**: Currently, Google Forms links are manually embedded in Google Docs. We may automate this in future releases.
- **Database Integration**: We'll eventually connect the app to a MySQL database for storing participant and admin information, allowing more robust user management.

---

## Contributions

If you'd like to contribute to BootBuddy, feel free to submit a pull request or open an issue with any suggestions or bugs you encounter.
