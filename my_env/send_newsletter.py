from main.feedly_utils import get_feedly_data
from main.feedly_utils import send_newsletter
from main.feedly_utils import send_newsletter_smtp
from django.core.mail import send_mail
from main.models import Recipient
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_env.settings')
django.setup()

# Fetch the data from the Feedly API
data = get_feedly_data()
# print(data)
recipient_list = Recipient.objects.values_list('email', flat=True)
# Send the newsletter email to the list of recipients
#send_newsletter(recipient_list, data)
# send_newsletter_smtp(recipient_list, data)