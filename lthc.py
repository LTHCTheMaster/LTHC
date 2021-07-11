#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789.'

#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, error_name, details, file_, line):
        self.error_name = error_name
        self.details = details
        self.file = file_
        self.line = line
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.file}, line {self.line}'
        return result

class IllegalCharacterError(Error):
    def __init__(self, details, file_, line):
        super().__init__('Illegal Character', details, file_, line)

class InvalidSyntaxError(Error):
    def __init__(self, details, file_, line):
        super().__init__('Invalid Syntax', details, file_, line)

class RuntimeError(Error):
    def __init__(self, details, file_, line):
        super().__init__('Runtime Error', details, file_, line)

#######################################
# TOKENS
#######################################

T_NUM      = 'NUM'

T_PLUS     = 'PLUS'
T_MINUS    = 'MINUS'
T_MUL      = 'MUL'
T_DIV      = 'DIV'
T_QEDIV    = 'QEDIV'
T_MOD      = 'MOD'
T_POW      = 'POW'

T_LPAREN   = 'LPAREN'
T_RPAREN   = 'RPAREN'

T_EOF      = 'EOF'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, text, file_, line):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
        self.file = file_
        self.line = line
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    def tokenize(self):
        tokens = []

        while self.current_char != None and self.pos < len(self.text):
            if self.current_char in ' \t':
                self.advance()
            
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())

            elif self.current_char == '+':
                tokens.append(Token(T_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(T_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(self.make_mul())
            elif self.current_char == '/':
                tokens.append(self.make_div())
            elif self.current_char == '%':
                tokens.append(Token(T_MOD))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(T_POW))
                self.advance()
            
            elif self.current_char == '(':
                tokens.append(Token(T_LPAREN))
                self.advance()
            
            elif self.current_char == ')':
                tokens.append(Token(T_RPAREN))
                self.advance()
            
            else:
                char = self.current_char
                return [], IllegalCharacterError("'" + char + "'", self.file, self.line)

        tokens.append(Token(T_EOF))
        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS:
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(T_NUM, int(num_str))
        else:
            return Token(T_NUM, float(num_str))
    
    def make_div(self):
        tokentype = T_DIV
        self.advance()
        if self.current_char == '/':
            tokentype = T_QEDIV
            self.advance()
        return Token(tokentype)
    
    def make_mul(self):
        tokentype = T_MUL
        self.advance()
        if self.current_char == '*':
            tokentype = T_POW
            self.advance()
        return Token(tokentype)

#######################################
# NODES
#######################################

class NumberNode:
	def __init__(self, tok):
		self.tok = tok

	def __repr__(self):
		return f'{self.tok}'

class BinOpNode:
	def __init__(self, left_node, op_tok, right_node):
		self.left_node = left_node
		self.op_tok = op_tok
		self.right_node = right_node

	def __repr__(self):
		return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
	def __init__(self, op_tok, node):
		self.op_tok = op_tok
		self.node = node

	def __repr__(self):
		return f'({self.op_tok}, {self.node})'

#######################################
# PARSE RESULT
#######################################

class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None

	def register(self, res):
		if isinstance(res, ParseResult):
			if res.error: self.error = res.error
			return res.node

		return res

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
		self.error = error
		return self

#######################################
# PARSER
#######################################

class Parser:
    def __init__(self, tokens, file_, line):
        self.tokens = tokens
        self.token_index = -1
        self.current_token = None
        self.advance()
        self.file = file_
        self.line = line
    
    def advance(self, ):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        return self.current_token
    
    def parse(self):
        res = self.expr()
        if not res.error and self.current_token.type != T_EOF:
            return res.failure(InvalidSyntaxError(
                "Expected '+', '-', '*' or '/'", self.file, self.line
            ))
        return res
    
    ###################################
    
    def atom(self):
        res = ParseResult()
        tok = self.current_token

        if tok.type == T_NUM:
            res.register(self.advance())
            return res.success(NumberNode(tok))

        elif tok.type == T_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_token.type == T_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    "Expected ')'", self.file, self.line
                ))

        return res.failure(InvalidSyntaxError(
            "Expected int, float, '+', '-' or '('", self.file, self.line
        ))

    def power(self):
        return self.bin_op(self.atom, (T_POW, ), self.factor)

    def factor(self):
        res = ParseResult()
        tok = self.current_token

        if tok.type in (T_PLUS, T_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        return self.power()
    
    def term(self):
        return self.bin_op(self.factor, (T_MUL, T_DIV, T_QEDIV, T_MOD))

    def expr(self):
        return self.bin_op(self.term, (T_PLUS, T_MINUS))
    
    ###################################

    def bin_op(self, func_a, ops, func_b=None):
        if func_b == None:
            func_b = func_a

        res = ParseResult()
        left = res.register(func_a())
        if res.error: return res

        while self.current_token.type in ops:
            op_tok = self.current_token
            res.register(self.advance())
            right = res.register(func_b())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)

#######################################
# RUNTIME RESULT
#######################################

class RuntimeResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error: self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self

#######################################
# VALUES
#######################################

class Number:
    def __init__(self, value, context):
        self.value = value
        self.n()
        self.set_context(context)

    def n(self):
        return self

    def set_context(self, context=None):
        self.context = context
        self.file = self.context.file
        self.line = self.context.line
        return self

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value, self.context).set_context(self.context), None

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value, self.context).set_context(self.context), None

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value, self.context).set_context(self.context), None

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RuntimeError(
                    'Division by zero', self.file, self.line
                )

            return Number(self.value / other.value, self.context).set_context(self.context), None
    
    def qedived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RuntimeError(
                    'Division by zero', self.file, self.line
                )

            return Number(self.value // other.value, self.context).set_context(self.context), None
    
    def moded_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RuntimeError(
                    'Division by zero', self.file, self.line
                )

            return Number(self.value % other.value, self.context).set_context(self.context), None

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value, self.context).set_context(self.context), None

    def __repr__(self):
        return str(self.value)

#######################################
# CONTEXT
#######################################

class Context:
    def __init__(self, display_name, file_, line, parent=None):
        self.display_name = display_name
        self.parent = parent
        self.file = file_
        self.line = line

#######################################
# INTERPRETER
#######################################

class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    ###################################

    def visit_NumberNode(self, node, context):
        return RuntimeResult().success(
            Number(node.tok.value, context).set_context(context).n()
        )

    def visit_BinOpNode(self, node, context):
        res = RuntimeResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error: return res
        right = res.register(self.visit(node.right_node, context))
        if res.error: return res

        if node.op_tok.type == T_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.type == T_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.type == T_MUL:
            result, error = left.multed_by(right)
        elif node.op_tok.type == T_DIV:
            result, error = left.dived_by(right)
        elif node.op_tok.type == T_QEDIV:
            result, error = left.qedived_by(right)
        elif node.op_tok.type == T_MOD:
            result, error = left.moded_by(right)
        elif node.op_tok.type == T_POW:
            result, error = left.powed_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.n())

    def visit_UnaryOpNode(self, node, context):
        res = RuntimeResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res

        error = None

        if node.op_tok.type == T_MINUS:
            number, error = number.multed_by(Number(-1, context))

        if error:
            return res.failure(error)
        else:
            return res.success(number.n())

#######################################
# RUN
#######################################

def run(text, file_, line):
    lexer = Lexer(text, file_, line)
    tokens, error = lexer.tokenize()
    if error: return None, error

    parser = Parser(tokens, file_, line)
    ast = parser.parse()
    if ast.error: return None, ast.error

    interpreter = Interpreter()
    context = Context('<program>', file_, line)
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
