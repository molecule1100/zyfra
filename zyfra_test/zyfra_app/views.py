from django.shortcuts import render
from .models import Samosval, Warehouse


def index(request):
    samosvals = Samosval.objects.all()
    warehouse = Warehouse.objects.first()

    if request.method == 'POST':
        for samosval in samosvals:
            coords = request.POST.get(f'coords_{samosvals.id}', '')
            if coords:
                try:
                    x, y = map(float, coords.split())
                    if warehouse.is_point_inside(x, y):
                        warehouse.update_ore(samosval)
                except ValueError:
                    pass

    context = {
        'samosvals': samosvals,
        'warehouse': warehouse,
    }
    return render(request, 'index.html', context)
