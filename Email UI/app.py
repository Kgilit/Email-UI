from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, SMTPConfig, EmailLog
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message  # Import Flask-Mail

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mail_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Mail
mail = Mail(app)

# Initialize the database
db.init_app(app)


# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')


@app.route('/smtp_config', methods=['GET', 'POST'])
def smtp_config():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    if request.method == 'POST':
        smtp_server = request.form['smtp_server']
        port = request.form['port']
        sender_email = request.form['sender_email']
        sender_password = request.form['sender_password']

        # Save SMTP configuration to the database
        config = SMTPConfig(user_id=user_id, smtp_server=smtp_server, port=port,
                            sender_email=sender_email, sender_password=sender_password)
        db.session.add(config)
        db.session.commit()

        # Dynamically configure Flask-Mail
        app.config['MAIL_SERVER'] = 'smtp.gmail.com' #This is the mail server for google only
        app.config['MAIL_PORT'] = 587 #This is the mail port for google only
        app.config['MAIL_USE_TLS'] = True  # Assume TLS is used for simplicity
        app.config['MAIL_USERNAME'] = Enter your email here
        app.config['MAIL_PASSWORD'] = Enter your password
        app.config['MAIL_DEFAULT_SENDER'] = Enter your email here

        # Reinitialize Mail with new configuration
        mail.init_app(app)

        flash('SMTP Configuration saved!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('smtp_config.html')


@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        message = request.form['message']
        user_id = session['user_id']

        # Get SMTP configuration from the database
        config = SMTPConfig.query.filter_by(user_id=user_id).first()
        if not config:
            flash('SMTP Configuration not found!', 'danger')
            return redirect(url_for('smtp_config'))

        # Send email using Flask-Mail
        try:
            msg = Message(subject, recipients=[recipient])
            msg.body = message

            # Send the email
            mail.send(msg)

            # Log the email in the database
            email_log = EmailLog(user_id=user_id, recipient=recipient, subject=subject, message=message)
            db.session.add(email_log)
            db.session.commit()

            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending email: {str(e)}', 'danger')

    return render_template('send_email.html')


@app.route('/logs')
def logs():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    logs = EmailLog.query.filter_by(user_id=user_id).all()
    return render_template('logs.html', logs=logs)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
