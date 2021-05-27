from django.test import TestCase

# Create your tests here.
class TempTest(TestCase):
    def setUp(self):
        self.churrasco = True
    
    def test_feliz(self):
        feliz = False
        if self.churrasco:
            feliz = True
        self.assertEqual(feliz, True)