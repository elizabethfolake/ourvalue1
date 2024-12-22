from django.shortcuts import render
def home(request):
    return render(request, 'index.html')
def about(request):
  username =  request.GET["username"]
  username ='you just enter: ' + username.upper() + 'Thank you'
  return render(request, 'contact.html', {'username': username})