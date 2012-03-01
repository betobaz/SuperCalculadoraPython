import unittest
import mox
import supercalculadora
import expr_aritmetica
import validador_expr_aritmetica as validador

class TestsSupercaculadora(unittest.TestCase):
	
	def setUp(self):
		self.sc = supercalculadora.Supercalculadora(expr_aritmetica.ExprAritmetica(), validador.ValidadorExprAritmetica())
	
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
	
	def test_expr_compleja_todas_operaciones_sin_parntesis(self):
		self.failUnlessEqual("11", self.sc.calcular("4 - -3 * 2 / 3 + 5"))
	
	def test_validador_expresion_invalida_stub(self):
		validador_stub = validador.ValidadorExprAritmetica()
		validar_mock = mox.Mox()
		validar_mock.StubOutWithMock(validador_stub, 'validar')
		validador_stub.validar("2 ^ 3").AndReturn(False)
		validar_mock.ReplayAll()
		sc = supercalculadora.Supercalculadora(expr_aritmetica.ExprAritmetica(), validador_stub)
		self.failUnlessRaises(SyntaxError, sc.calcular, "2 ^ 3")
		validar_mock.UnsetStubs()
		validar_mock.VerifyAll()

