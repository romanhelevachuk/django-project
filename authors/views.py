from django.http import JsonResponse
from .models import Author

def author_list(request):
    authors = Author.objects.all().values()
    return JsonResponse(list(authors), safe=False)

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return JsonResponse({"name": author.name, "birthdate": author.birthdate})
