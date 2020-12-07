from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title=forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email=forms.EmailField()
    description=forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your Description",
                "class":"new-class name",
                "rows":20
    }))
    price=forms.DecimalField(initial=100.0)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price']
 

    def clean_email(self, *args, **kwargs):
        email=self.cleaned_data.get("email")
        if not "@" in email:
            raise form.ValidationError("This is not a valid email ")
        return email
     

class RawProductForm(forms.Form):
    title=forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description=forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your Description",
                "class":"new-class name",
                "rows":20
    }))
    price=forms.DecimalField(initial=100.0)
    