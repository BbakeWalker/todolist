from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'Enter a new todo'}))

    # text = forms.CharField(max_length=50,
    #     widget=forms.TextInput(
    #         attrs={'class' : 'form-control', 'placeholder' : 'Enter a new todo', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
