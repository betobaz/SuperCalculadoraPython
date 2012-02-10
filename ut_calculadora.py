import unittest
import calculadora

class TestsCalculadora(unittest.TestCase):
	
	def setUp(self):
		self.calc = calculadora.Calculadora()
	
	def tearDown(self):
		pass

	def test_sumar2_y_2(self):
		self.failUnlessEqual(4, self.calc.sumar(2, 2))

	def test_sumar_5_y_7(self):
		self.failUnlessEqual(12, self.calc.sumar(5, 7))
	
	def test_sumar_propiedad_conmutativa(self):
		self.failUnlessEqual(self.calc.sumar(5, 7), self.calc.sumar(7, 5))

	def test_restar_5_y_3(self):
		self.failUnlessEqual(2, self.calc.restar(5, 3))
	
	def test_restar_2_y_3(self):
		self.failUnlessEqual(-1, self.calc.restar(2, 3))
	
	def test_restar_no_propiedad_conmutativa(self):
		self.failIfEqual(self.calc.restar(5,3), self.calc.restar(3, 5))
	
	def test_sumar_numeros_negativos(self):
		self.failUnlessEqual(0, self.calc.sumar(2, -2))

	def test_restar_numeros_negativos(self):
		self.failUnlessEqual(-7, self.calc.restar(-5, 2))
		self.failUnlessEqual(-5, self.calc.restar(-7, -2))
	
	def test_division_exacta(self):		
		self.failUnlessEqual(-2, self.calc.dividir(10, -5))
		self.failUnlessEqual(2, self.calc.dividir(-10, -5))
	
	def test_division_no_entera_da_excepcion(self):		
		self.failUnlessRaises(ValueError, self.calc.dividir, 3, 2)
	
	def test_division_por_0(self):		
		self.failUnlessRaises(ZeroDivisionError, self.calc.dividir, 3, 0)
	
	def test_multiplicar_simple(self):
		self.failUnlessEqual(8, self.calc.multiplicar(4, 2))
	
	def test_multiplicar_negativa(self):
		self.failUnlessEqual(-8, self.calc.multiplicar(-4, 2))
		self.failUnlessEqual(-8, self.calc.multiplicar(4, -2))
		self.failUnlessEqual(8, self.calc.multiplicar(-4, -2))

	


