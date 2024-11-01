from django import forms as f
from .models import *

class AddBookForm(f.ModelForm):
    class Meta:
            model= Book
            fields= "__all__"
            widget= {
        "retal_price_day":f.NumberInput(attrs={"class":"form-control","id":"retalprice"},),
        "retal_period":f.NumberInput(attrs={"class":"form-control" ,"id":"retaldays"},),
        "total_retal":f.NumberInput(attrs={"class":"form-control","id":"totalretal"},),
                    }

class AddCategoryForm(f.ModelForm):
    class Meta:
            model= Category
            fields= ["typename"]
            widget= {
        "typename":f.TextInput(attrs={"class":"form-control"},),
                    }
            labels={"typename":"name"}

