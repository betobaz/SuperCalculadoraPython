import unittest
import supercalculadora
import expr_aritmetica
import ut_calculadora
import ut_expr_aritmetica

class TestsSupercaculadora(unittest.TestCase):
	
	def setUp(self):
		self.sc = supercalculadora.Supercalculadora(expr_aritmetica.ExprAritmetica())
	
	def tearDown(self):
		pass

	def test_sumar(self):
		self.failUnlessEqual("4", self.sc.calcular("2 + 2"))
	
	def test_restar(self):
		self.failUnlessEqual("0", self.sc.calcular("2 - 2"))
	
	def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
		self.failUnlessEqual("6", self.sc.calcular("5 + 4 - 3"))
	
	def test_expresion_compleja_sin_parentesis_con_precedencia(self):
		self.failUnlessEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
		self.failUnlessEqual("-1", self.sc.calcular("4 / 2 - 3"))
		self.failUnlessEqual("1", self.sc.calcular("4 / 2 - 3 + 1 + 6 / 3 - 1"))
		self.failUnlessEqual("-8", self.sc.calcular("4 / -2 + 3 + -1 + -6 / -3 - 10"))
		self.failUnlessEqual("9", self.sc.calcular("5 + 4 * 2 / 2"))

	



if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(ut_calculadora.TestsCalculadora))
	suite.addTest(unittest.makeSuite(ut_expr_aritmetica.TestsExprAritmetica))
	suite.addTest(unittest.makeSuite(TestsSupercaculadora))
	unittest.TextTestRunner(verbosity=3).run(suite)
