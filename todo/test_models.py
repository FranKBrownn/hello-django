from django.test import TestCase
from .models import item


class TestModels(TestCase):

    def test_done_defults_to_fales(self):
        Item = item.objects.create(name='Test todo item')
        self.assertFalse(Item.done)

    def test_item_string_method_returns_name(self):
        Item = item.objects.create(name='Test todo item')
        self.assertEqual(str(Item), 'Test todo item')