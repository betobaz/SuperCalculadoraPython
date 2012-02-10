import string

class ExprAritmetica:

	def __es_numero__(self, cadena):
		try:
			string.atoi(cadena)
			return True
		except ValueError:
			return False

	def parse(self, exp):
		operandos = []
		operadores = []
		tokens = string.split(exp)
		for token in tokens:
			if self.__es_numero__(token):
				operandos.append(string.atoi(token))
			else:
				operadores.append(token)
		return {'Operandos':operandos, 'Operadores':operadores}
