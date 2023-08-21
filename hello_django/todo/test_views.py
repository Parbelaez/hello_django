from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        # create a response variable that will store the response from the client
        response = self.client.get('/')
        # check if the response status code is 200... basically, check if the page exists
        self.assertEqual(response.status_code, 200)
        # check if the right template was used
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # create a response variable that will store the response from the client
        response = self.client.get('/add')
        # check if the response status code is 200
        self.assertEqual(response.status_code, 200)
        # check if the right template was used
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # create an item
        item = Item.objects.create(name='Test Todo Item')
        # create a response variable that will store the response from the client
        response = self.client.get(f'/edit/{item.id}')
        # check if the response status code is 200
        self.assertEqual(response.status_code, 200)
        # check if the right template was used
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # create a response variable that will store the response from the client
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # redirect to the todo list
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # create an item
        item = Item.objects.create(name='Test Todo Item')
        # create a response variable that will store the response from the client
        response = self.client.get(f'/delete/{item.id}')
        # check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # redirect to the todo list
        self.assertRedirects(response, '/')
        # check if the item was deleted
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # create an item
        item = Item.objects.create(name='Test Todo Item', done=True)
        # create a response variable that will store the response from the client
        response = self.client.get(f'/toggle/{item.id}')
        # check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # redirect to the todo list
        self.assertRedirects(response, '/')
        # get the item again
        updated_item = Item.objects.get(id=item.id)
        # check if the item.done value is False
        self.assertFalse(updated_item.done)
