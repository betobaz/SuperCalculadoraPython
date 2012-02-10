import unittest
import expr_aritmetica

class TestsExprAritmetica(unittest.TestCase):

	def setUp(self):
		self.expresion = expr_aritmetica.ExprAritmetica()
	
	def tearDown(self):
		pass

	def test_extraer_operandos_y_operadores_en_2_mas_2(self):
		self.failUnlessEqual({'Operandos':[2, 2], 'Operadores':['+']}, self.expresion.parse("2 + 2"))

	def test_extraer_operandos_y_operadores_en_10_entre_menos_5(self):
		self.failUnlessEqual({'Operandos': [10, -5], 'Operadores': ['/']}, self.expresion.parse("10 / -5"))

	def test_extraer_operandos_y_operadores_expr_sin_ptesis(self):
		self.failUnlessEqual({'Operandos': [5, 4, 2, 2], 'Operadores': ['+', '*', '/']}, self.expresion.parse("5 + 4 * 2 / 2"))

