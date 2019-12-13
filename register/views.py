from django.contrib.auth.models import User
from django.views.generic import CreateView


# Create your views here.
class UserCreate(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'signup.html'
    success_url = '/'
