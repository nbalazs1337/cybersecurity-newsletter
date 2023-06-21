import requests
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import django
import boto3
from botocore.exceptions import ClientError
# from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_env.settings')
django.setup()



def get_feedly_data():
    stream_id = 'feed/http://rss.packetstormsecurity.org/news/tags/zero_day/'  
    #stream_id = 'feed/https://advisories.feedly.com/google/chrome/feed.json'
    count = 3
    url = f"https://cloud.feedly.com/v3/streams/contents?streamId={stream_id}&count={count}"
    access_token = "A4lDry3Lm6rRgHzx9vib59d8Vved8Yg01ve6tNHsy1U9HfVQdQ-edV1wJSstyITivrnSYQI410tqiuX0Xn6l4G59E5Qa--KYSStqORulRs7zS7lpZ0eVRTa_PywuKg7fSd35f5IRVma-eJcXBRcCvWr_sxvuDRbKw22wwg_EP2n0eYrvafFAUrAqdL0gsqxKWAMwX4T33Lm4WigXN7wV2iq1yGc9E0mGHyrJo_T_sV9njyYl6fwsqR9USn4:feedlydev"
    headers = {
        "Authorization": f"OAuth {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()




def send_newsletter(recipient_list, data):
   
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_env.settings')
    django.setup()


    # Render the newsletter template with data from Feedly API
    html_message = render_to_string('design_update.html', {'data': data})
   
    plain_message = "Your Feedly Newsletter"

    # create an instance of the SES client
    ses_client = boto3.client('ses', 
        region_name='eu-north-1', 
        aws_access_key_id=settings.AWS_ACCESS_KEY, 
        aws_secret_access_key=settings.AWS_SECRET_KEY
    )

    # Set up the email message
    message = {
        
        'Subject': {'Data': 'Your Feedly Newsletter'},
        'Body' : {'Html':{'Data': html_message}},
       
           
    }

    # Send the email
    try:
        response = ses_client.send_email(
            Source=settings.DEFAULT_FROM_EMAIL,
            Destination={'ToAddresses': recipient_list},
            Message=message,
            
          
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print('Email sent! Message ID:'),
        print(response['MessageId'])

from django.template.loader import render_to_string

from .models import NewDisclosure

def send_newsletter_smtp(recipient_list, data):
    disclosures = NewDisclosure.objects.all()
    # Render the newsletter template with data from Feedly API
    html_message = render_to_string('design_update_smaller.html', {'disclosures': disclosures, 'data': data})
    plain_message = "Your Feedly Newsletter"
    

    # Set up the email message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Your Feedly Newsletter'
    message['From'] = settings.DEFAULT_FROM_EMAIL
    message['To'] = ', '.join(recipient_list)
    message.attach(MIMEText(plain_message, 'plain'))
    message.attach(MIMEText(html_message, 'html'))
    
    # Set up the SMTP server
    smtp_server = smtplib.SMTP(settings.EMAIL_HOST_SMTP, settings.EMAIL_PORT)
    #smtp_server.ehlo()
    smtp_server.starttls()
    #smtp_server.ehlo()
    # load_dotenv()
    #email_password = os.getenv('EMAIL_HOST_PASSWORD')
    email_password = settings.EMAIL_HOST_PASSWORD
    
    smtp_server.login(settings.DEFAULT_FROM_EMAIL, email_password)
    

    # Send the email
    try:
        smtp_server.sendmail(settings.DEFAULT_FROM_EMAIL, recipient_list, message.as_string())
    except smtplib.SMTPException as e:
        print('Error: ', e)
    else:
        print('Email sent!')
    finally:
        smtp_server.quit()


        

from django.shortcuts import render, redirect
from .models import Recipient

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Assuming the form field has the name 'email'
        subscriber = Recipient(email=email)
        subscriber.save()
        # Additional logic or redirect after saving the subscriber
        return redirect('success')  # Redirect to a success page or any other desired page

    return render(request, 'signup.html')

