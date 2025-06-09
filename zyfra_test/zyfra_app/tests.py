from django.test import TestCase
from .models import Samosval, Warehouse, Ruda, SamosvalDescription
from .reset import reset_and_initialize_data


class RudaTestCase(TestCase):
    def setUp(self):
        reset_and_initialize_data()

    def test_samosval_count(self):
        self.assertEqual(Samosval.objects.count(), 3)

    def test_overload_percent(self):
        samosval = Samosval.objects.get(number="102")
        self.assertAlmostEqual(samosval.peregruz_percent(), 4.16666666666, places=2)

    def test_point_inside_polygon(self):
        warehouse = Warehouse.objects.first()
        self.assertTrue(warehouse.is_point_inside(30, 10))
        self.assertFalse(warehouse.is_point_inside(100, 100))

    def test_update_ruda(self):
        warehouse = Warehouse.objects.first()
        samosval = Samosval.objects.get(number="101")
        warehouse.update_ruda(samosval)
        self.assertEqual(warehouse.current_quantity, 1000)
