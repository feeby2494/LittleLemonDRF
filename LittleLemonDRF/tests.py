from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.test import Client
from django.forms.models import model_to_dict
from .models import Category, MenuItem
from .views import CategoriesView, MenuItemsView
import unittest

# Want to test frist baby steps to lanauge API


class TestLittleLemonDRF(unittest.TestCase):

    def setUp(self):
        self.client = Client()

        # setup models
        self.test_pass_category = Category.objects.create(slug='passCat', title='passTitle')
        self.test_pass_menu_item = MenuItem.objects.create(title='passItem', price='5', inventory=7.0, category=self.test_pass_category)
        self.test_cat_id = model_to_dict(self.test_pass_category)['id']
        self.test_item_id = model_to_dict(self.test_pass_menu_item)['id']

        self.factory = APIRequestFactory()


        # self.factory = APIRequestFactory()     

    def test_models(self):
        self.assertEqual(model_to_dict(self.test_pass_category), {'id' : self.test_cat_id, 'slug' : 'passCat', 'title' : 'passTitle'})
        self.assertEqual(model_to_dict(self.test_pass_menu_item), {'id' : self.test_item_id, 'title' : 'passItem', 'price' : '5', 'inventory' : 7.0, 'category' : self.test_cat_id})

    def test_endpoints(self):
        request_pass_cat = self.factory.get('/api/category')
        response_pass_cat = CategoriesView.as_view()(request_pass_cat)
        self.assertEqual(response_pass_cat.status_code, 200)

        request_pass_item = self.factory.get('/api/menu-items')
        response_pass_item = MenuItemsView.as_view()(request_pass_cat)
        self.assertEqual(response_pass_item.status_code, 200)

        # test response data
        self.assertEqual(response_pass_cat.data, [{'id' : self.test_cat_id, 'slug' : 'passCat', 'title' : 'passTitle'}])
        self.assertEqual(response_pass_item.data, [{'id' : self.test_item_id, 'title' : 'passItem', 'price' : '5', 'inventory' : 7.0, 'category' : self.test_cat_id}])

    # def test_search(self):
    #     req = self.factory.get('/api/menu-items?search=passTitle')
    #     res = MenuItemsView.as_view()(req)
    #     self.assertEqual(res.data, [{'id' : self.test_cat_id, 'title' : 'passItem', 'price' : '5', 'inventory' : 7.0, 'category' : self.test_cat_id}])

    def tearDownCat(self):
        cat = Category.objects.get(pk=self.test_cat_id)
        cat.delete()
        cat.save()

        all_cat = Category.objects.all()
        all_cat.delete()
        all_cat.save()

        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.all().delete()

    def tearDownItem(self):
        item = MenuItem.objects.get(pk=self.test_item_id)
        item.delete()
        item.save()

        all_item = MenuItem.objects.all()
        all_item.delete()
        all_item.save()
        
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()
        MenuItem.objects.all().delete()



# I give up with this shit. 
# Whoever came up with Test Driven Development is a Fucking idiot
# I spend more time writing shit tests that don't work


