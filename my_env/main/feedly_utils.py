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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_env.settings')
django.setup()



def get_feedly_data():
    stream_id = 'feed/http://rss.packetstormsecurity.org/news/tags/zero_day/'  
    #stream_id = 'feed/https://advisories.feedly.com/google/chrome/feed.json'
    count = 3
    url = f"https://cloud.feedly.com/v3/streams/contents?streamId={stream_id}&count={count}"
    access_token = "A8JCTCabGqCwwF3bAf2j_xHaE3fx52K_12RZ-fHzNfes0JGW5xvoYHTV7XBMmBhQ0noppF-pdgI4dExKDEUT0Mda4QhNUVlB5TjyRV6d1c-4NNCCgi75-Uhk_q2uw4Ar5X_rQsvipPNAtciO9rtm-LmP5AuvkKhEqYU4B0TyaCxqlO_gvfzuTLAhacfmHYwReFeOxKN4qfmoPoyGPHHn34KVuRw0O6o8kFoGAQUR3eR7wuq_W9XlXfxdj18:feedlydev"
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
    html_message = render_to_string('my_template.html', {'results': data})
<<<<<<< Updated upstream
   
=======
>>>>>>> Stashed changes
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