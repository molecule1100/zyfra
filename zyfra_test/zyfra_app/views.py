from django.shortcuts import render
from .models import Samosval, Warehouse


def index(request):
    samosvals = Samosval.objects.all()
    warehouse = Warehouse.objects.first()
    initial_quantity = warehouse.current_quantity

    if request.method == 'POST':
        for samosval in samosvals:
            coords = request.POST.get(f'coords_{samosval.id}', '')
            if coords:
                try:
                    x, y = map(float, coords.split())
                    if warehouse.is_point_inside(x, y):
                        warehouse.update_ruda(samosval)
                except ValueError:
                    pass

    context = {
        'samosvals': samosvals,
        'warehouse': warehouse,
        'initial_quantity': initial_quantity,
    }


    return render(request, 'index.html', context)
