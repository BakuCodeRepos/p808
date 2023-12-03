from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": _("Your review"), "rows": 5, "cols": 30}
        )
    )

    class Meta:
        model = Comment
        fields = ["text"]
