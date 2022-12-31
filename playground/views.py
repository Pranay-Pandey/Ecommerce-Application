from django.shortcuts import render
from django.db.models import Q, F
from store.models import Customer
#Q will be used to wrap filter argument - can pass OR AND NOT operation
#F will be used to  reference another column

# Create your views here.
def home(request):

    queryset = Customer.objects.filter(phone__gt=18000)

    return render(request, 'template/landingpage.html', {"name":"Pranay", 'customers':list(queryset) , 'len_customers':len(list(queryset))})
