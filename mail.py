import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "vaishalibhosleksit@@gmail.com"
app_password = "**** **** **** ****"
receiver_email = "vaishalibhosleksit@example.com"
subject = "Underpass Management System Update"

# Water level and vehicle status
water_level = 70  # Percentage of water level
vehicle_status = "No vehicles stuck"

# HTML body
body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .container {{
            width: 100%;
            max-width: 600px;
            margin: 20px auto;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background-color: #0044cc;
            color: #fff;
            padding: 20px;
            text-align: center;
        }}
        .content {{
            padding: 20px;
        }}
        .status-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        .status-table th, .status-table td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        .status-table th {{
            background-color: #f4f4f4;
        }}
        .underpass {{
            position: relative;
            width: 100%;
            height: 200px;
            background-color: #999;
            border-bottom: 40px solid #666;
            margin-top: 20px;
        }}
        .waves {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: {water_level}%;
            background: linear-gradient(180deg, rgba(0,119,255,0.7) 0%, rgba(0,119,255,0.5) 70%);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Underpass Management System Update</h1>
        </div>
        <div class="content">
            <p>Dear Authority,</p>
            <p>Here is the current status of the underpass:</p>
            <div class="underpass">
                <div class="waves"></div>
            </div>
            <table class="status-table">
                <tr>
                    <th>Parameter</th>
                    <th>Status</th>
                </tr>
                <tr>
                    <td>Water Level</td>
                    <td>{water_level}%</td>
                </tr>
                <tr>
                    <td>Vehicle Status</td>
                    <td>{vehicle_status}</td>
                </tr>
            </table>
            <p>Please take necessary actions if required.</p>
            <p>Best regards,</p>
            <p>Your Underpass Management System</p>
        </div>
    </div>
</body>
</html>
"""

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach HTML body to email
msg.attach(MIMEText(body, 'html'))

# Create SMTP session for sending the mail
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Enable security
        server.login(sender_email, app_password)  # Log in to the server
        text = msg.as_string()  # Convert the message to a string
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
