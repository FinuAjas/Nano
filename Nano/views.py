from django.shortcuts import render, redirect
from django.http import HttpResponse
import mimetypes
import os

def download_pdf(request):
    filename = 'Nano-Catalogue.pdf'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '/Nano/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response