from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]
    
    def clean_mood(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_feelings(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)