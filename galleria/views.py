from django.shortcuts import render, get_object_or_404
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


def details(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'galleria/details.html', {'image': image})

def about(request):
    return render(request, 'galleria/about.html', {})