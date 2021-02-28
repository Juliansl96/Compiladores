# coding: utf-8
'''
Lenguaje BASIC Dartmouth
------------------------

Palabras Reservadas (keywords)

DEF — define funciones de una sola línea
DIM — define el tamaño de los arreglos
END — define el final del programa
STOP — detiene un programa antes del final
FOR/TO/STEP — define los bucles
NEXT — marca el final de los bucles
GOSUB — transfiere control a subrutinas simples
RETURN — retorna el control desde subrutinas simples
GOTO — transfiere el control a otra sentencia
IF/THEN — toma de decisiones
LET/= — asigna los resultados de las fórmulas a una variable
PRINT — salida de resultados
DATA — almacena datos estáticos dentro del programa
READ — entrada de datos almacenados en sentencias DATA
REM — comentario

También implementó variables numéricas y aritmética de punto flotante.
Los nombres de variables fueron limitados de A a Z, A0 a A9, B0 a B9, ... , Z0 a Z9,
dando un máximo de 286 distintas variables posibles.
Los nombres de matrices estaban restringidos a solamente de A a Z. Las matrices
no necesitaban ser definidas, pero en ausencia de una declaración DIM tenían por
defecto 10 elementos, a los que se accedía con un índice desde 1 a 10.

Lista de operadores

Operadores aritméticos	       Operadores relacionales/lógicos
-	Negación (op. unario)	    =	Igual a
+	Adición	                    <>	No igual a
-	Sustracción (op. binario)	<	Menor que
*	Multiplicación	            <=	Menor o igual a
/	División	                >	Mayor que
^	Exponenciación	            >=	Mayor o igual a

Operadores de agrupamiento
( )	Agrupamiento

Lista de funciones
ABS -- Valor absoluto
INT -- Parte entera de un número
RND -- número real al azar entre 0 y 1
SIN -- Seno (argumento en radianes)
COS -- Coseno (argumento en radianes)
TAN -- Tangente (argumento en radianes)
ATN -- Arco tangente (resultado en radianes)
EXP -- Exponencial (e^x)
LOG -- Logaritmo natural
SQR -- raíz cuadrada
'''


import sly
from errors import error

class Lexer(sly.Lexer):
	tokens = {
		# keywords
		LET, READ, DATA, PRINT, GOTO, IF,
		THEN, FOR, NEXT, TO, STEP, END,
		STOP, DEF, GOSUB, DIM, REM, RETURN,
		RUN, LIST, NEW,

		# operadores de relacion
		LT, LE, GT, GE, NE,

		# identificador
		ID,

		# constantes
		LINENO, NUMBER, STRING,
	}
	literals = '+-*/^()=:,;'

	# ignorar
	ignore = r' \t\r'

	# expresiones regulares
	REM    = r'REM .*'

	ID = r'[A-Z][A-Z0-9]*'
	ID['LET']    = LET
	ID['READ']   = READ
	ID['DATA']   = DATA
	ID['PRINT']  = PRINT
	ID['GOTO']   = GOTO
	ID['IF']     = IF
	ID['THEN']   = THEN
	ID['FOR']    = FOR
	ID['NEXT']   = NEXT
	ID['TO']     = TO
	ID['STEP']   = STEP
	ID['END']    = END
	ID['STOP']   = STOP
	ID['DEF']    = DEF
	ID['GOSUB']  = GOSUB
	ID['DIM']    = DIM
	ID['RETURN'] = RETURN
	ID['RUN']    = RUN
	ID['LIST']   = LIST
	ID['NEW']    = NEW

	LE = r'<='
	LT = r'<'
	GE = r'>='
	GT = r'>'
	NE = r'<>'
	LINENO = r'^\d+'
	NUMBER = r'(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)'
	STRING = r'"[^"]*"?'

	@_(r'\n')
	def NEWLINE(self, t):
		self.lineno += 1

	def error(self, t):
		error('caracter ilegal %s' % t.value[0], t.lineno)
		self.index += 1


if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		print('uso: baslex.py filename')
		sys.exit(1)

	data = open(sys.argv[1]).read()

	lex = Lexer()
	for tok in lex.tokenize(data):
		print(tok)
