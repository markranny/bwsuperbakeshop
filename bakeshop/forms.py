# bakeshop/forms.py

from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number (Optional)'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }


class JobApplicationForm(forms.ModelForm):
    """Job application form"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message', 'resume']
        labels = {
            'message': 'Cover Letter',
            'resume': 'Resume/CV (PDF, DOC, or DOCX)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about your relevant experience and why you want to join our team', 'rows': 5}),
        }


class FranchiseInquiryForm(forms.ModelForm):
    """Franchise inquiry form"""
    INVESTMENT_LEVELS = (
        ('', 'Select Investment Level'),
        ('express', 'Express Store ($75,000)'),
        ('standard', 'Standard Store ($150,000)'),
        ('premium', 'Premium Store ($250,000)'),
    )
    
    investment_level = forms.ChoiceField(
        choices=INVESTMENT_LEVELS,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'preferred_location', 'investment_level', 'message']
        labels = {
            'preferred_location': 'Preferred Location',
            'message': 'Additional Information',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'preferred_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City, State or Region'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about your background and why you are interested in franchising with us', 'rows': 5}),
        }