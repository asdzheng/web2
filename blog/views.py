# Create your views here.
from django.shortcuts import render_to_response
from django import forms
from blog.models import User
from django.http import HttpResponse
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def regist(req):
    print req.method
    if req.method == "POST":
	uf = UserForm(req.POST, req.FILES)
        print 'valid? : ', uf.is_valid()
	if uf.is_valid():
	    print 'uf is valid'
	    user = User()
	    user.name =  uf.cleaned_data['username']
	    user.headImg = uf.cleaned_data['headImg']
	    user.save()
	    print user.name
	    return HttpResponse('ok')
    else:
	uf = UserForm()	    
    return render_to_response('register.html', {'uf':uf})
