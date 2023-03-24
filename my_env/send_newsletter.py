from main.feedly_utils import get_feedly_data
from main.feedly_utils import send_newsletter
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_env.settings')
django.setup()

# Fetch the data from the Feedly API
data = get_feedly_data()
recipient_list = ['florin.negrea@arobs.com']
# Send the newsletter email to the list of recipients
send_newsletter(recipient_list, data)