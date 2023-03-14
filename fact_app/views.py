from tkinter.tix import Select
from django.shortcuts import render
from django.views import View
from . models import *

# Create your views here.

class HomeView(View):

    """MAIN VIEW"""

    templates_name = 'index.html'

    invoices = Invoice.objects.select_related('customer', 'save_by').all()

    context = {
        'invoices': invoices
    }
    def get(self, request, *args, **kwags):
       
        return render(request, self.templates_name, self.context)
    
    def post(self, request, *args, **kwagrs):

        return render(request, self.templates_name, self.context) 
    

    class AddCustomerView(View):
        """Add new customer"""

        template_name = 'add_customer.html'

        def get(self, request, *args, **kwags):
         return render(request, self.template_name)   
        
        def post(self, request, *args, **kwagrs): 
         data= {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone':request.POST.get('phone'),
            'address':request.POST.get('address'),
            'sex':request.POST.get('sex'),
            'age':request.POST.get('age'),
            'city':request.POST.get('city'),
            'zip':request.POST.get('zip'),
            'save_by':request.user
            
         }
           
         return render(request, self.template_name)


    




