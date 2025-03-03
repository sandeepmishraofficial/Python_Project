from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .forms import StudentRegistration
from .models import User
from django.http import Http404

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            stud = User.objects.all()
        else:
            stud = User.objects.all()
    else:
        fm = StudentRegistration()
        stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

#this function update and edit



def update_data(request, id):
    # Get the user instance using get_object_or_404 to avoid possible exceptions
    pi = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')  # Redirect after successful update (using redirect instead of HttpResponseRedirect)
    else:
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/update.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    else:
        raise Http404("Page Not Found")
    
   