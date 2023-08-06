from django.shortcuts import render

# Create your views here.
def easy_password(request):
    return render(request, 'password_app/html_file/easy.html')

# def medium_password(request):
#     return render(request, 'html_file/medium.html')
# def hard_password(request):
#     return render(request, 'html_file/hard.html')
