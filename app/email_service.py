# app/email_service.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "[Daily Briefing] This is a test"
print("SUBJECT:", subject)

html_content = f"""
<h3>This is a test of the Daily Briefing Service</h3>
<p>Date: Monday, January 1, 2040</p>

<h4>My Stocks</h4>
<ul>
    <li>MSFT: +04%</li>
    <li>WORK: +20%</li>
    <li>ZM: +44%</li>
</ul>

<h4>My Forecast</h4>
<ul>
    <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
    <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
    <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
    <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
    <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
</ul>
"""
print("HTML:", html_content)

message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html_content)

try:
    response = client.send(message)
    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    #print(response.body)
    #print(response.headers)
except Exception as e:
    print("OOPS", e.message)
