from django.shortcuts import render

# Create your views here.
def contacts_list(request):
    return render(request, 'contacts/contacts_list.html')