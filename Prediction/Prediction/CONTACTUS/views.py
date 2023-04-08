from django.shortcuts import render, redirect
from .models import Contactus
# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user_list')
#     else:
#         form = UserForm()
#     return render(request, 'userapp/add_user.html', {'form': form})

def contactus(request):
    if request.method == "POST":
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        Email = request.POST['email']
        Comment = request.POST['phone']
        Phone = request.POST['comment']
        Newcontacts = Contactus(first_name=Fname, last_name=Lname, email=Email, comment=Comment, phone_number=Phone)
        Newcontacts.save()
        print(Newcontacts)

    return render(request, 'CONTACTUS\contacts.html')

# Create your views here.
