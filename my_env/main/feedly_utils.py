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
    access_token = "A52LWkW9aRVfp4iPDvPfPkBtI9Gki_Kdv1T8oFndsZdAZsIwc0MfN7BR6DYzjrxFif65zmhZ8gKDk83C5q3NkYsN84igEwsYepFLMr66GpYjhEkihWe5ADyElK_T5i3ZYdPdzBQRixx8tzAd24Jen8Zhf--JG2dmdPkDcshntylpN8fFpgJbsfM2D67hFrjbJt_laHZ2nIawX4yaFbaoIHxM4lAwbMTFjhMSJZjec-9__Ynsu0GMA7l2AmY:feedlydev"
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