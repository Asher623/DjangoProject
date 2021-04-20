from django.contrib.auth.forms import forms
from .models import Post, Comment, UserInfo
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):


    class Meta():
        model = Post
        fields = ('title', 'text', 'image')


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment

        fields = ('text',)

class UserInfoForm(forms.ModelForm):


    class Meta():
        model = User

        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserInfo

        fields = ('picture',)
