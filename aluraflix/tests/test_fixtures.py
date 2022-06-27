from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']
    
    
    def tes_loading_fixtures(self):
        porgrama_bizarro = Programa.objects.get(pk = 1)
        todos_os_programas = Programa.objects.all()
        self.assertEqual(porgrama_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(todos_os_programas), 9)
        