from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Quote
import random
import json


def _serialize(q):
    return {"id": q.id, "text": q.text, "author": q.author}


# ============ TEMPLATE VIEWS (return HTML) ============

def home(request):
    quotes = list(Quote.objects.all())
    quote = random.choice(quotes) if quotes else None
    return render(request, "quotes/home.html", {"quote": quote})


def all_quotes(request):
    quotes = Quote.objects.all()
    return render(request, "quotes/all_quotes.html", {"quotes": quotes})


# ============ API VIEWS (return JSON) ============

def random_quote_api(request):
    quotes = list(Quote.objects.all())
    if not quotes:
        return JsonResponse({"error": "No quotes available"}, status=404)
    return JsonResponse(_serialize(random.choice(quotes)))


@csrf_exempt
def quotes_api(request):
    if request.method == "GET":
        data = [_serialize(q) for q in Quote.objects.all()]
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body or b"{}")
        quote = Quote.objects.create(
            text=body.get("text", ""),
            author=body.get("author", ""),
        )
        return JsonResponse(_serialize(quote), status=201)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def quote_detail_api(request, id):
    try:
        quote = Quote.objects.get(id=id)
    except Quote.DoesNotExist:
        return JsonResponse({"error": "Quote not found"}, status=404)

    if request.method == "GET":
        return JsonResponse(_serialize(quote))

    if request.method == "PUT":
        body = json.loads(request.body or b"{}")
        if "text" in body:
            quote.text = body["text"]
        if "author" in body:
            quote.author = body["author"]
        quote.save()
        return JsonResponse(_serialize(quote))

    if request.method == "DELETE":
        quote.delete()
        return JsonResponse({"message": f"Quote {id} deleted"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
