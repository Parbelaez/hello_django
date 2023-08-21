from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # create a form with a name field set to an empty string
        form = ItemForm({'name': ''})
        # check if the form is invalid
        self.assertFalse(form.is_valid())
        # check if the name field has the error message we expect
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    
    def test_done_field_is_not_required(self):
        # create a form with a name field set to any string
        form = ItemForm({'name': 'Test Todo Item'})
        # check if the form is valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # create a form instance
        form = ItemForm()
        # check if the form fields match the expected fields
        self.assertEqual(form.Meta.fields, ['name', 'done'])