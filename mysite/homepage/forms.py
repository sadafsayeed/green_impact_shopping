from django import forms

class PurchaseInfo(forms.Form):
    amount_spent = forms.DecimalField(max_digits=10, decimal_places=2)
    store_name = forms.CharField(max_length=100)
    purchase_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    products = forms.CharField(max_length=1000)
    