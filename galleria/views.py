from django.shortcuts import render
from .models import Location, Category, Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'galleria/index.html', {'images': images})

# search image by category
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_title(search_term)
        print(searched_images)
        message = f"{search_term}"

        return render(request, 'galleria/search.html', {"message": message, "searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'galleria/search.html',{"message":message})
