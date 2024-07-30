from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import Image

# Create your views here.

response = requests.get('https://pixabay.com/api/?key=45170644-baa9552b1c978473d8d221321&q=food')
d3_images = response.json()

def home_view(request):
    global d3_images
    
    for i in d3_images['hits']:
        if not Image.objects.filter(
                pageURL=i['pageURL'],
            ).exists():
            Image.objects.create(
                pageURL=i['pageURL'],
                type=i['type'],
                tags=i['tags'],
                webformatURL=i['webformatURL'],
                views=i['views'],
                downloads=i['downloads'],
                likes=i['likes'],
                user=i['user']
            )
    images = Image.objects.all()
    return render(request, 'index.html', {"images":images}) 


def imageDetail_view(request, pk):
    try:
        image = Image.objects.filter(pk=pk).values()
        if not image:
            return JsonResponse({"error": "Image not found"}, status=404)
        image_list = list(image)
        return render(request, 'details.html',{"image": image_list[0]})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    