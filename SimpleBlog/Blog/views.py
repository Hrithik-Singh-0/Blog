from django.shortcuts import render, HttpResponseRedirect
from Blog.models import blogger

def homepage(request):
    allblogs = blogger.objects.all()
    context = {'blogs': allblogs}
    return render(request, 'Blog/index.html', context)

def create(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        image = request.POST.get('img')
        content = request.POST.get('content')
        blog = blogger(ID=id, Name=name, Date=date, Image=image, Content=content)
        blog.save()
    return render(request, 'Blog/create.html')

def delete(request, Name):
    if request.method == 'POST':
        user = blogger.objects.get(pk=Name)
        user.delete()
        return HttpResponseRedirect('#')