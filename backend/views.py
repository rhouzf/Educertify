from django.shortcuts import render
from django.http import JsonResponse

def upload_page(request):
    return render(request, 'upload.html')