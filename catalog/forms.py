from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

# Слова, которые нельзя использовать в названии и описании продуктов
FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "photo", "category", "price"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        self._validate_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        if description:
            self._validate_forbidden_words(description)
        return description

    def _validate_forbidden_words(self, text):
        # Проверка наличия запрещенных слов в тексте
        for word in FORBIDDEN_WORDS:
            if word.lower() in text.lower():
                raise forms.ValidationError(f"Использование слова '{word}' запрещено.")


    # Проверяет, что цена не может быть отрицательной
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите название продукта"
        })

        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })

        self.fields["price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену продукта"
        })

        self.fields["category"].widget.attrs.update({
            "class": "form-control"
        })


        self.fields["photo"].widget.attrs.update({
            "class": "form-control"
        })

