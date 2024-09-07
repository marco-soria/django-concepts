
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def my_view(request):
    car_list = [
        {'title': 'Toyota Camry'},
        {'title': 'Honda Accord'},
        {'title': 'Tesla Model S'},
    ]
    context = {
        'car_list': car_list
    }
    return render(request, 'car_list.html', context)

class CarListView(TemplateView):
    template_name = 'car_list.html'
    
    def get_context_data(self):
        car_list = [
            {'title': 'Toyota Camry'},
            {'title': 'Honda Accord'},
            {'title': 'Tesla Model S'},
        ]
        return {
            "car_list": car_list
            }

def my_test_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("")