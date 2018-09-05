from django import forms

from .models import ItemToBuy


class AddItemForm(forms.ModelForm):
    class Meta:
        model = ItemToBuy
        fields = ("title", "description", 'sizes', 'number', 'estimate_price', 'created_date', "estimate_date")

