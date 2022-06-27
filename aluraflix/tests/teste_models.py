from django.test import TestCase
from aluraflix.models import Programa

class ProgaramaModelTestCase(TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguem',
            data_lancamento = '2003-07-04'
        )
        
    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de um programa com valores default
        """
        self.assertEqual(self.programa.titulo, 'Procurando ninguem')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2003-07-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
        
            