import os
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .feedly_utils import get_feedly_data
from .models import FeedlyItem
from django.http import FileResponse
from main.forms import SignupForm
from main.models import Recipient



def my_view(request):


   data = get_feedly_data()
   results = data['items']

   for result in results:
      title = result['title']
      feedly_item = FeedlyItem(title=title)
      feedly_item.save()
      items = FeedlyItem.objects.all()
      #return render(request, 'design.html', {'items': items})
   #return render(request, 'design.html', {'results': results})
   disclosures = NewDisclosure.objects.all()
   return render(request, 'design_update_smaller.html', {'results': results, 'disclosures':disclosures})



def unsubscribe(request):
    return render(request, 'unsubscribe.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            recipient, created = Recipient.objects.get_or_create(email=email)
            if created:
                # Optionally, you can perform additional actions
                # (e.g., send a confirmation email, display a success message)
                return render(request, 'signup_success.html')
                pass
            #return redirectalert("gg")  # Redirect to the newsletter page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')


from django.shortcuts import render
from .models import NewDisclosure


def disclosures_view(request):
    disclosures = NewDisclosure.objects.all()
    
    print(disclosures)
    
    return render(request, 'design_update.html', {'disclosures': disclosures})



