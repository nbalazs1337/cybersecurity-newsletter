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
    #print(response.json())
#get_feedly_data()



def send_newsletter(recipient_list, data):
    # Get the list of recipients
    recipients = ['negrea.balazs@yahoo.com']

    # Render the newsletter template with data from Feedly API
    html_message = render_to_string('my_template.html', {'data': data})
    

    # Set up the email message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Your Feedly Newsletter'
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = ', '.join(recipients)
    msg.attach(MIMEText(html_message, 'html'))
    

    # Set up the SMTP server connection
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_HOST_USER, os.environ.get('EMAIL_PASSWORD'))

    # Send the email
    server.sendmail(settings.EMAIL_HOST_USER, recipients, msg.as_string())
    server.quit()

    print('Newsletter sent successfully!')