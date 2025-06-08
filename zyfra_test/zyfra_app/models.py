from django.db import models
from shapely.geometry import Point, Polygon


class SamosvalDescription(models.Model):
    name = models.CharField(max_length=50, unique=True)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Ruda(models.Model):
    sio2 = models.FloatField()
    fe = models.FloatField()

    def __str__(self):
        return f"SiO2: {self.sio2:.2f}%, Fe: {self.fe:.2f}%"

class Samosval(models.Model):
    number = models.CharField(max_length=10, unique=True)
    model = models.ForeignKey(SamosvalDescription, on_delete=models.CASCADE)
    current_load = models.IntegerField()
    ruda = models.ForeignKey(Ruda, on_delete=models.CASCADE)

    def peregruz_percent(self):
        if self.model.max_capacity <= 0:
            return 0
        peregruz = self.current_load - self.model.max_capacity
        if peregruz <= 0:
            return 0
        return (peregruz / self.model.max_capacity) * 100

    def __str__(self):
        return self.number


class Warehouse(models.Model):
    name = models.CharField(max_length=50, default="Склад")
    current_quantity = models.IntegerField(default=0)
    ruda = models.ForeignKey(Ruda, on_delete=models.CASCADE)
    polygon_wkt = models.TextField()

    def is_point_inside(self, x, y):
        polygon = Polygon([(30, 10), (40, 40), (20, 40), (10, 20), (30, 10)])
        point = Point(x, y)
        return polygon.contains(point) or polygon.boundary.contains(point)

    def update_ruda(self, samosval):
        total_mass = self.current_quantity + samosval.current_load
        if total_mass > 0:
            sio2 = ((self.ruda.sio2 * self.current_quantity + samosval.ruda.sio2 * samosval.current_load) / total_mass)
            fe = ((self.ruda.fe * self.current_quantity + samosval.ruda.fe * samosval.current_load) / total_mass)
            self.ruda.sio2 = sio2
            self.ruda.fe = fe
            self.current_quantity = total_mass
            self.ruda.save()
            self.save()

    def __str__(self):
        return self.name
