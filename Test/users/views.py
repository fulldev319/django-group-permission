from django.shortcuts import render
from django.http import HttpResponse

####### I love pineapples. ################
@group_required('Group1')
def view1(request):
    return HttpResponse('This is View1')

@group_required('Group2')
def view2(request):
    return HttpResponse('This is View2')