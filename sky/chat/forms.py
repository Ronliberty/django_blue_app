from django import forms

class StartConversationForm(forms.Form):
    room_name = forms.CharField(max_length=255, label='Room Name')
