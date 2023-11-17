# from django.contrib.auth import get_user_model
from .models import Account
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegisterForm

# User = get_user_model()


class AccountRegistrationView(generic.CreateView):
    #  class based
    """
    Account Register View
    If user is authenticated then redirect to dashboard view
    """

    template_name = "account/register.html"
    form_class = UserRegisterForm
    model = Account
    success_url = reverse_lazy('index')  # 'home/'
