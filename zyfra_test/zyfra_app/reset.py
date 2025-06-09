def reset_and_initialize_data():
    from .models import Samosval, Warehouse, Ruda, SamosvalDescription

    Samosval.objects.all().delete()
    Warehouse.objects.all().delete()
    Ruda.objects.all().delete()
    SamosvalDescription.objects.all().delete()

    belaz = SamosvalDescription.objects.create(name="БЕЛАЗ", max_capacity=120)
    komatsu = SamosvalDescription.objects.create(name="Komatsu", max_capacity=110)

    ruda_101 = Ruda.objects.create(sio2=32.0, fe=67.0)
    ruda_102 = Ruda.objects.create(sio2=30.0, fe=65.0)
    ruda_k103 = Ruda.objects.create(sio2=35.0, fe=62.0)

    sklad_ruda = Ruda.objects.create(sio2=34.0, fe=65.0)

    Samosval.objects.create(number="101", model=belaz, current_load=100, ruda=ruda_101)
    Samosval.objects.create(number="102", model=belaz, current_load=125, ruda=ruda_102)
    Samosval.objects.create(number="K103", model=komatsu, current_load=120, ruda=ruda_k103)

    wkt_polygon = "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))"
    Warehouse.objects.create(name="Склад", current_quantity=900, ruda=sklad_ruda, polygon_wkt=wkt_polygon)
