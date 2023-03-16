from main.feedly_utils import get_feedly_data
from main.feedly_utils import send_newsletter


# Fetch the data from the Feedly API
data = get_feedly_data()
recipient_list = ['negrea.balazs@yahoo.com']
# Send the newsletter email to the list of recipients
send_newsletter(recipient_list, data)