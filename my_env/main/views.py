import os
import requests
from django.shortcuts import render
from django.conf import settings
from .feedly_utils import get_feedly_data
from .models import FeedlyItem
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse



def my_view(request):


   data = get_feedly_data()
   results = data['items']

   for result in results:
      title = result['title']
      feedly_item = FeedlyItem(title=title)
      feedly_item.save()
      items = FeedlyItem.objects.all()
      #return render(request, 'my_template.html', {'items': items})
   return render(request, 'my_template.html', {'results': results})




def send_newsletter(request):
    # Get the list of users to send the newsletter to
    recipients = ['user1@example.com', 'user2@example.com', 'user3@example.com']

    # Render the newsletter template
    html_message = render_to_string('template.html')

    # Send the email using Django's send_mail function
    send_mail(
        subject='Your Feedly Newsletter',
        message='Here is your newsletter from Feedly!',
        html_message=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
    )

    return HttpResponse('Newsletter sent successfully!')

