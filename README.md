# Note
The application is not fully complete and functional. Due to time constraints, I was unable to fully complete all the features as planned. Additionally, I had to balance this project with other university commitments, which impacted the time available to finalize everything. Despite this, I put in significant effort to develop the core functionality, and I hope the work demonstrates my skills and dedication.I would appreciate if you could consider giving me a LOR, acknowledging my effort and growth during this period.

# Description
This is a simple Email Sending Application built with Python using Flask. It allows users to configure SMTP settings, log in with their credentials, send emails, and view the logs of sent emails. The application provides a simple web interface with user authentication and email functionality.

# Features
SMTP Configuration: Allows users to configure their SMTP server, email, and password.
Send Email: Users can send emails to recipients by specifying the subject, message, and recipient email address.
Email Logs: View a log of emails sent by the user.
User Authentication: Secure login system that ensures only authenticated users can access the application.
Responsive Web Interface: A simple web interface to manage email settings and send emails.
# Technologies Used
Python 3.x: Programming language used to build the application.
Flask: A micro web framework used to handle web requests and routes.
Flask-Mail: A Flask extension used to send emails.
SQLite: A lightweight database to store user information and email logs.
HTML/CSS: Used for the basic front-end layout of the web interface.
# Requirements 
pip install Flask flask-mail

# Steps to run

Configure SMTP Settings:
Before you can send emails, you need to configure the SMTP settings by providing the details for your email service (such as Gmail).
Start the app and visit the /smtp_config page.
Enter the following details:
SMTP Server: smtp.gmail.com
Port: 587
Sender Email: your_email@gmail.com
Sender Password: your_password
Important: If you're using Gmail, ensure that you've enabled "Less Secure Apps" or have created an App Password for increased security.



Test Login:
Go to the login page (/login) and use the following test credentials:
Test Email: 'testuser@example.com'
Test Password: 'testpassword'
Once logged in, you will be redirected to the dashboard.


Open the server:
Once done with all the above steps go to the directory for app.py and open it in the terminal, once done you can run this command 'python app.py'.
After runnning you should have a link to the server which looks like this 'http://127.0.0.1:5000'
Now you can use the app here



Send a Test Email:
After logging in, go to the /send_email page to send a test email.
Fill out the following details:
Recipient Email: recipient@example.com (you can use any valid email)
Subject: Test Email
Message: This is a test email.
Click the Send Email button.
If the email is sent successfully, you will see a success message. If there is any issue, an error message will appear.
