from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "date",
            "name",
            "mobile_no",
            "alternate_no",
            "email_id",
            "address",
            "course",
            "batch",
            "experience_fresher",
            "how_you_know",
            "contact",
            "counselor",
            "fees",
            "comment",
            "selected_type",
        ]

        widgets = {
            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter student name"
            }),

            "mobile_no": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter mobile number"
            }),

            "alternate_no": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter alternate number"
            }),

            "email_id": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter address",
                "rows": 3
            }),

            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course"
            }),

            "batch": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter batch"
            }),

            "experience_fresher": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Fresher / Experienced"
            }),

            "how_you_know": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "How did you know about us?"
            }),

            "contact": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contact status"
            }),

            "counselor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Counselor name"
            }),

            "fees": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter fees"
            }),

            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter comments",
                "rows": 3
            }),

            "selected_type": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter selected type"
            }),
        }

    def clean_mobile_no(self):
        mobile = self.cleaned_data.get("mobile_no")

        if mobile and len(str(mobile)) < 10:
            raise forms.ValidationError(
                "Mobile number must contain at least 10 digits."
            )

        return mobile