import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Define email sender
from_email = "vaishalibhosleksit@gmail.com"
password = 'kyywvflgbbvayftv'  # Consider using environment variables for sensitive information

# Define email receivers
to_emails = ["vmtejusksit@gmail.com", "rakshitagsksit@gmail.com", "ravitejkakhandakiksit@gmail.com" ,"rekhabvenkatapur@ksit.edu.in"]

# Define the water level and corresponding status
water_level = input("Enter the water level as <high> <medium> or <low>: ").lower()

if water_level == "high":
    status = "Underpass clogged, gates are closed, only service roads in action"
    img_path = "High.png"
    img_cid = "water_level_high"
elif water_level == "medium":
    status = "Underpass slightly filled with water, gates are being closed"
    img_path = "Medium.png"
    img_cid = "water_level_medium"
elif water_level == "low":
    status = "Underpass not clogged, all roads are open"
    img_path = "Low.png"
    img_cid = "water_level_low"
else:
    raise ValueError("Invalid water level. Please enter 'high', 'medium', or 'low'.")

# Create the body with HTML
html = f'''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #E5E7E9;
            color: #333;
            margin: 0;
            padding: 0;
        }}
        .container {{
            background-color: #fff;
            margin: 20px auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
        }}
        .header {{
            background-color: #3498DB;
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 10px 10px 0 0;
        }}
        .content {{
            padding: 20px;
            background-color: #E5E7E9;
        }}
        .content h2 {{
            color: #333;
            
        }}
        .details p {{
            margin: 10px 0;
        }}
        .visual {{
            text-align: center;
            margin: 20px 0;
        }}
        .visual img {{
            max-width: 100%;
            height: auto;
        }}
        .footer {{
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #777;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Sample Underpass Management System Alert for {water_level.upper} Water Level</h1>
        </div>
        <div class="content">
            <h2>Underpass Details</h2>
            <div class="details">
                <p><strong>Timestamp:</strong> 2024-07-26 02:07:27</p>
                <p><strong>Water Level:</strong> {water_level.capitalize()}</p>
                <p><strong>Status:</strong> {status}</p>
                <p><strong>Underpass Details:</strong> Underpass ID: 123, Location: XYZ</p>
                <p><strong>Location:</strong> Latitude: 12.345, Longitude: 67.890</p>
            </div>
            <div class="visual">
                <img src="cid:{img_cid}" alt="{water_level.capitalize()} Water Level">
            </div>
        </div>
        <div class="footer">
            <p>Underpass Management System &copy; 2024</p>
        </div>
    </div>
</body>
</html>
'''

# Create the root message and attach HTML part and image
def create_message():
    msg = MIMEMultipart('related')
    msg['Subject'] = 'Underpass Management System Update'
    msg['From'] = from_email

    # Attach HTML part
    msg.attach(MIMEText(html, 'html'))

    # Attach image based on water level
    with open(img_path, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', f'<{img_cid}>')
        msg.attach(img)
    
    return msg

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(from_email, password)
    for to_email in to_emails:
        msg = create_message()
        msg['To'] = to_email
        server.sendmail(from_email, to_email, msg.as_string())
