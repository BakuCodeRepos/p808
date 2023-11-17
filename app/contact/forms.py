from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Appealing


class AppealingForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": _("Full name")}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": _("Email")}
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": _("Subject")}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": _("Message"), "rows": 6}
        )
    )

    class Meta:
        model = Appealing
        fields = ["full_name", "email", "subject", "message"]
