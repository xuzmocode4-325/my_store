from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="User Name", max_length=50,
#         error_messages={
#             "required":"Yo! A username is required fam.",
#             "max_length": "No time to deal with those long ass names, yo!"
#         }
#     )
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "user_name", 
            "review_text",
            "rating"
        ]
        labels = {
           "user_name": "Your Name", 
            "review_text": "Your FeedbacK",
            "rating": "Your Rating" 
        }
        error_messages = {
            "user_name": {
                "required": "Yo! A username is required fam.",
                "max_length": "Ain't nobody gonna remamber that long ass names, yo!",
            },
        }