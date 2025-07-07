from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from .models import Consultation

@csrf_exempt
def save_consultation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Consultation.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                subject=data.get('subject'),
                message=data.get('message')
            )
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return HttpResponse("This endpoint only accepts POST requests to store data.")
