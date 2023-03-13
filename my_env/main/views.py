import os
import requests
from django.shortcuts import render
from django.conf import settings
from .feedly_utils import get_feedly_data
from .models import FeedlyItem



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

