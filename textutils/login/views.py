# i have created this file-hitu
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Sign_Up, Login
from .models import Student


# render is used to create  and impot the templates
# render takes first arg = request, 2nd arg = name of the file you want to import, 3rd arg = parameters or variable name
def index(request):
    return render(request, 'index.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Sign_Up(request.POST)
        # check whether it's valid:
        if form.is_valid():
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            details = Student(first_name=firstName, last_name=lastName, email=email,
                              password=password)  # these are models variable in red
            # process the data in form.cleaned_data as required
            details.save() # this is used to save all the details
            # ...
            # redirect to a new URL:
            return render(request, 'login/new_index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Sign_Up()

    return render(request, 'login/new_index.html', {'form': form})


def login_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            def my_view(request):
                email = request.POST['email']
                password = request.POST['password']
                match = Student(email=email, password=password)
                if match is not None:
                    if match.is_active:
                        Login(request, match)
                        # Redirect to a success page.
                    import logging
                    logger = logging.getLogger("mylogger")
                    logger.info(match)

                else:
                    form = my_view()

                return render(request, 'login/login.html', {'form': form})

            # Return an 'invalid login' error message.

            return render(request, 'login/login.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Login()

    return render(request, 'login/login.html', {'form': form})

