"""
That file contains functions for working with the project frontend
1. Function 'text_apply' processing the form of word input and output word count calculation
2. The 'date_method' function displays a list of all records in the database
"""
from django.shortcuts import render
from text_output.models import AcceptsText
from django import forms
from text_output.utils import convert, stat

class TextForm(forms.Form):
    text = forms.CharField(max_length=3000, widget=forms.Textarea)

def text_apply(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = convert(text)
            output = stat(result)
            instance = AcceptsText(text=text, small=output[0], medium=output[1], large = output[2])
            instance.save()
            return render(request, 'word.html', {'form': form, 'fr1': output[0], 'fr2': output[1], 'fr3': output[2]})
    else:
        form = TextForm()
    return render(request, 'word.html', {'form': form})


def date_method(request):
    data = AcceptsText.objects.all()
    return render(request,'data.html',{'data' : data})






