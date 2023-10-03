from django import forms

UNIT_CHOICES = [
        ("kg", "kg"),
        ("ton", "ton"),
        ("g", "g"),
        ("mg", "mg"),
        ("lb", "lb"),
        ("oz", "oz"),
        ("l", "l"),
        ("kl", "kl"),
        ("ml", "ml"),
        ("pcs", "pcs")
    ]

class add_form(forms.Form):
    name = forms.CharField(max_length= 255, widget=forms.TextInput(attrs={'placeholder': 'Cth: "Beras 1"'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 10000}))
    price_unit = forms.ChoiceField(choices = UNIT_CHOICES)
    stock = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': "60, Opsional"}))
    stock_unit = forms.ChoiceField(choices=UNIT_CHOICES)
    description = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': "Hanya di Pasar 1, Opsional"}))