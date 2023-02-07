from django.shortcuts import render, redirect
from .forms import UserForm

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'userapp/add_user.html', {'form': form})



# Create your views here.
