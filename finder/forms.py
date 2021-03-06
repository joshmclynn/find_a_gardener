from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from .models import CustomUser, User
from django import forms


# form updating current allauth form, to include the attributes
# that i need within my user model.
locations = CustomUser.objects.values('location')
CHOICES = [('customer', 'Customer'), ('business', 'Business')]
NEEDS = [('garden-maintenance', 'Garden-Maintenance'),
         ('garden-design', 'Garden-Design'),
         ('landscaping', 'Landscaping'), ('tree-surgery', 'Tree-Surgery')]


class CustomSignupForm(SignupForm):

        fields = ('user_type', 'needs', 'location')

        user_type = forms.ChoiceField(choices=CHOICES,
                                      label="""Are you a Business or a
                                      Customer?"""
                                      )

        needs = forms.MultipleChoiceField(
                                          widget=forms.CheckboxSelectMultiple,
                                          choices=NEEDS,
                                          label="""What services do you
                                          provide or need?"""
                                        )
        location = forms.CharField(
                                   label='What City do you live in?',
                                   required=True
                                    )

        class Meta:
            model = CustomUser

        def save(self, request):
            user = super(CustomSignupForm, self).save(request)
            user.user_type = self.cleaned_data['user_type']
            user.needs = self.cleaned_data['needs']
            user.location = self.cleaned_data['location']
            user.save()
            return user


# Form for users to change attributes when logged in.
class update_profile(forms.ModelForm):
    email = forms.EmailField(required=True)
    needs = forms.MultipleChoiceField(
                                          widget=forms.CheckboxSelectMultiple,
                                          choices=NEEDS,
                                          label="""What services do you
                                          provide or need?"""
                                          )
    location = forms.CharField(
                                max_length=30,
                                label='What City do you live in?',
                                required=True
                                )

    class Meta:
        model = CustomUser
        fields = ['email', 'needs', 'location']
