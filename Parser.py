from colorama import Fore, Style, init

init(autoreset=True)


def banner():
    logo = f"""{Fore.RED}
    ████████████████████████████████████████████████████████
    
        ██████   █████  ██████  ███████ ███████ ██████  
        ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ 
        ██████  ███████ ██████  ███████ █████   ██████  
        ██      ██   ██ ██   ██      ██ ██      ██   ██ 
        ██      ██   ██ ██   ██ ███████ ███████ ██   ██ 

    ████████████████████████████████████████████████████████
    """

    info = f"""
    {Fore.CYAN}Creator{Style.DIM}: ALI Raza
    {Fore.CYAN}Github{Style.DIM}: https://github.com/0xAli-Raza/AdvancedParser
    {Fore.CYAN}Status{Style.DIM}: Stable
    {Fore.CYAN}Version{Style.DIM}: 3.0
    """

    print(logo + info)
# =============================================================
#                          AST Nodes
# =============================================================
class ASTNode:
    def __init__(self, line=None, col=None):
        self.line = line
        self.col = col


class Program(ASTNode):
    def __init__(self, statements):  
        super().__init__()
        self.statements = statements  

    def __repr__(self):
        return f"Program({len(self.statements)} statements)"


class Number(ASTNode):
    def __init__(self, value, line=None, col=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Identifier(ASTNode):
    def __init__(self, name, line=None, col=None):
        super().__init__(line, col)
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"


class StringLiteral(ASTNode):
    def __init__(self, value, line=None, col=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self):
        return f"String({self.value})"


class BinaryOp(ASTNode):
    def __init__(self, operator, left, right, line=None, col=None):
        super().__init__(line, col)
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOp('{self.operator}', {self.left}, {self.right})"


class VarDeclaration(ASTNode):
    def __init__(self, var_type, identifier, value=None, line=None, col=None):
        super().__init__(line, col)
        self.var_type = var_type
        self.identifier = identifier  # String name
        self.value = value  # Optional initializer

    def __repr__(self):
        return f"VarDeclaration(type='{self.var_type}', id='{self.identifier}', value={self.value})"


class Assignment(ASTNode):
    def __init__(self, identifier, value, line=None, col=None):
        super().__init__(line, col)
        self.identifier = identifier  # String name
        self.value = value

    def __repr__(self):
        return f"Assignment('{self.identifier}' = {self.value})"


class CompoundAssignment(ASTNode):
    def __init__(self, identifier, operator, value, line=None, col=None):
        super().__init__(line, col)
        self.identifier = identifier
        self.operator = operator
        self.value = value

    def __repr__(self):
        return f"CompoundAssignment('{self.identifier}' {self.operator} {self.value})"


class ComparisonOp(ASTNode):
    def __init__(self, operator, left, right, line=None, col=None):
        super().__init__(line, col)
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"ComparisonOp('{self.operator}', {self.left}, {self.right})"


class LogicalOp(ASTNode):
    def __init__(self, operator, left, right=None, line=None, col=None):
        super().__init__(line, col)
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        if self.right:
            return f"LogicalOp('{self.operator}', {self.left}, {self.right})"
        return f"LogicalOp('{self.operator}', {self.left})"


class Block(ASTNode):
    def __init__(self, statements, line=None, col=None):
        super().__init__(line, col)
        self.statements = statements

    def __repr__(self):
        return f"Block({len(self.statements)} statements)"


class IfStatement(ASTNode):
    def __init__(self, condition, then_block, else_block=None, line=None, col=None):
        super().__init__(line, col)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __repr__(self):
        return f"IfStatement(condition={self.condition})"


class WhileStatement(ASTNode):
    def __init__(self, condition, body, line=None, col=None):
        super().__init__(line, col)
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileStatement(condition={self.condition})"


class ForStatement(ASTNode):
    def __init__(self, init, condition, update, body, line=None, col=None):
        super().__init__(line, col)
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

    def __repr__(self):
        return f"ForStatement()"


class BreakStatement(ASTNode):
    def __repr__(self):
        return "BreakStatement()"


class ContinueStatement(ASTNode):
    def __repr__(self):
        return "ContinueStatement()"


class Parameter(ASTNode):
    def __init__(self, param_type, name, line=None, col=None):
        super().__init__(line, col)
        self.param_type = param_type
        self.name = name

    def __repr__(self):
        return f"Parameter({self.param_type} {self.name})"


class FunctionDeclaration(ASTNode):
    def __init__(self, return_type, name, parameters, body, line=None, col=None):
        super().__init__(line, col)
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return f"FunctionDeclaration({self.return_type} {self.name})"


class FunctionCall(ASTNode):
    def __init__(self, name, arguments, line=None, col=None):
        super().__init__(line, col)
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"FunctionCall({self.name})"


class ReturnStatement(ASTNode):
    def __init__(self, value=None, line=None, col=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self):
        return f"ReturnStatement({self.value})"


# =============================================================
#                       AST Printer
# =============================================================
def print_ast(node, indent=0, prefix=""):
    indent_str = "  " * indent

    if node is None:
        print(f"{indent_str}{prefix}None")
        return

    if isinstance(node, Program):
        print(f"{indent_str}{prefix}Program")
        for i, stmt in enumerate(node.statements):
            print_ast(stmt, indent + 1, f"[{i}]: ")

    elif isinstance(node, FunctionDeclaration):
        print(f"{indent_str}{prefix}FunctionDeclaration({node.return_type} {node.name})")
        print(f"{indent_str}  params: {node.parameters}")
        print_ast(node.body, indent + 1, "body: ")

    elif isinstance(node, Block):
        print(f"{indent_str}{prefix}Block")
        for i, stmt in enumerate(node.statements):
            print_ast(stmt, indent + 1, f"[{i}]: ")

    elif isinstance(node, VarDeclaration):
        print(f"{indent_str}{prefix}VarDeclaration({node.var_type} {node.identifier})")
        if node.value:
            print_ast(node.value, indent + 1, "value: ")

    elif isinstance(node, Assignment):
        print(f"{indent_str}{prefix}Assignment({node.identifier})")
        print_ast(node.value, indent + 1, "value: ")

    elif isinstance(node, CompoundAssignment):
        print(f"{indent_str}{prefix}CompoundAssignment({node.identifier} {node.operator})")
        print_ast(node.value, indent + 1, "value: ")

    elif isinstance(node, IfStatement):
        print(f"{indent_str}{prefix}IfStatement")
        print_ast(node.condition, indent + 1, "condition: ")
        print_ast(node.then_block, indent + 1, "then: ")
        if node.else_block:
            print_ast(node.else_block, indent + 1, "else: ")

    elif isinstance(node, WhileStatement):
        print(f"{indent_str}{prefix}WhileStatement")
        print_ast(node.condition, indent + 1, "condition: ")
        print_ast(node.body, indent + 1, "body: ")

    elif isinstance(node, ForStatement):
        print(f"{indent_str}{prefix}ForStatement")
        print_ast(node.init, indent + 1, "init: ")
        print_ast(node.condition, indent + 1, "condition: ")
        print_ast(node.update, indent + 1, "update: ")
        print_ast(node.body, indent + 1, "body: ")

    elif isinstance(node, FunctionCall):
        print(f"{indent_str}{prefix}FunctionCall({node.name})")
        for i, arg in enumerate(node.arguments):
            print_ast(arg, indent + 1, f"arg[{i}]: ")

    elif isinstance(node, ReturnStatement):
        print(f"{indent_str}{prefix}ReturnStatement")
        if node.value:
            print_ast(node.value, indent + 1, "value: ")

    elif isinstance(node, BinaryOp):
        print(f"{indent_str}{prefix}BinaryOp({node.operator})")
        print_ast(node.left, indent + 1, "left: ")
        print_ast(node.right, indent + 1, "right: ")

    elif isinstance(node, ComparisonOp):
        print(f"{indent_str}{prefix}ComparisonOp({node.operator})")
        print_ast(node.left, indent + 1, "left: ")
        print_ast(node.right, indent + 1, "right: ")

    elif isinstance(node, LogicalOp):
        print(f"{indent_str}{prefix}LogicalOp({node.operator})")
        print_ast(node.left, indent + 1, "left: ")
        if node.right:
            print_ast(node.right, indent + 1, "right: ")

    elif isinstance(node, (Number, StringLiteral)):
        print(f"{indent_str}{prefix}{node.__class__.__name__}({node.value})")

    elif isinstance(node, Identifier):
        print(f"{indent_str}{prefix}Identifier({node.name})")

    elif isinstance(node, (BreakStatement, ContinueStatement)):
        print(f"{indent_str}{prefix}{node.__class__.__name__}")

    else:
        print(f"{indent_str}{prefix}{node}")


# =============================================================
#                     Symbol Table (Parser)
# =============================================================
class Symbol:
    def __init__(self, name, var_type, is_function=False, params=None, value=None):
        self.name = name
        self.var_type = var_type
        self.is_function = is_function
        self.params = params if params is not None else []
        self.value = value
        self.is_variadic = False

    def __repr__(self):
        if self.is_function:
            return f"Symbol({self.name}, function, {self.var_type})"
        return f"Symbol({self.name}, {self.var_type})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self._add_stdlib()

    def _add_stdlib(self):
        stdlib = [
            ('printf', 'int', True),
            ('scanf', 'int', True),
            ('malloc', 'void*', False),
            ('free', 'void', False),
        ]
        for name, ret_type, variadic in stdlib:
            sym = Symbol(name, ret_type, is_function=True)
            sym.is_variadic = variadic
            self.symbols[name] = sym

    def declare(self, name, var_type, value=None, is_function=False, params=None):
        """Declare a symbol in the symbol table."""
        sym = Symbol(name, var_type, is_function=is_function, params=params, value=value)
        self.symbols[name] = sym
        return sym

    def lookup(self, name):
        return self.symbols.get(name)

    def exists(self, name):
        return name in self.symbols


# =============================================================
#                        Token Class
# =============================================================
class Token:
    def __init__(self, token_type, lexeme, line, col):
        self.type = token_type
        self.lexeme = lexeme
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.type}, '{self.lexeme}')"


# =============================================================
#                          Parser
# =============================================================
class Parser:
    def __init__(self, tokens):
        self.tokens = [Token(*t) if len(t) == 4 else Token(t[0], t[1], t[2], 0)
                       for t in tokens]
        self.pos = 0
        self.current_token = self.tokens[0] if self.tokens else None
        self.symbol_table = SymbolTable()
        self.errors = []
        self.loop_depth = 0
        self.function_depth = 0

    # Token Management
    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def peek(self, offset=1):
        pos = self.pos + offset
        return self.tokens[pos] if pos < len(self.tokens) else None

    def check(self, token_type, lexeme=None):
        if not self.current_token:
            return False
        if self.current_token.type != token_type:
            return False
        if lexeme and self.current_token.lexeme != lexeme:
            return False
        return True

    def match(self, token_type, lexeme=None):
        if self.check(token_type, lexeme):
            token = self.current_token
            self.advance()
            return token
        return None

    def expect(self, token_type, lexeme=None):
        token = self.match(token_type, lexeme)
        if token:
            return token
        expected = f"{token_type}" + (f":'{lexeme}'" if lexeme else "")
        actual = f"{self.current_token.type}:'{self.current_token.lexeme}'" if self.current_token else "EOF"
        self.report_error(f"Expected {expected}, got {actual}")
        return None

    def report_error(self, message):
        if self.current_token:
            error = f"Syntax Error at {self.current_token.line}:{self.current_token.col} - {message}"
        else:
            error = f"Syntax Error at EOF - {message}"
        self.errors.append(error)
        print(f" {error}")

    def synchronize(self):
        sync_tokens = {'SEMICOLON', 'EOF', 'RBRACE'}
        sync_keywords = {'int', 'float', 'char', 'void', 'if', 'while', 'for', 'return'}
        
        while self.current_token:
            if self.current_token.type in sync_tokens:
                if self.current_token.type == 'SEMICOLON':
                    self.advance()
                return
            if self.current_token.type == 'KEYWORD' and self.current_token.lexeme in sync_keywords:
                return
            self.advance()

    # Main Parse Entry
    def parse(self):
        print(" Starting parsing...")
        ast = self.program()
        if not self.errors:
            print(" Parsing completed successfully!")
        return ast

    def program(self):
        statements = []
        while self.current_token and self.current_token.type != 'EOF':
            stmt = self.declaration_or_statement()
            if stmt:
                statements.append(stmt)
            if self.errors and self.current_token and self.current_token.type != 'EOF':
                self.synchronize()
        return Program(statements)

    def declaration_or_statement(self):
        if self.check('KEYWORD'):
            keyword = self.current_token.lexeme
            if keyword in ['int', 'float', 'char', 'void']:
                next_tok = self.peek()
                next_next = self.peek(2)
                if next_tok and next_tok.type == 'IDENTIFIER' and next_next and next_next.type == 'LPAREN':
                    return self.function_declaration()
        return self.statement()

    def function_declaration(self):
        type_token = self.expect('KEYWORD')
        if not type_token:
            return None
        return_type = type_token.lexeme
        line, col = type_token.line, type_token.col

        name_token = self.expect('IDENTIFIER')
        if not name_token:
            return None
        func_name = name_token.lexeme

        if not self.expect('LPAREN'):
            return None
        parameters = self.parameter_list()
        if not self.expect('RPAREN'):
            return None

        self.symbol_table.declare(func_name, return_type, is_function=True, params=parameters)

        self.function_depth += 1
        body = self.block()
        self.function_depth -= 1

        return FunctionDeclaration(return_type, func_name, parameters, body, line, col)

    def parameter_list(self):
        params = []
        if self.check('RPAREN'):
            return params
        
        param = self.parameter()
        if param:
            params.append(param)
        
        while self.match('COMMA'):
            param = self.parameter()
            if param:
                params.append(param)
        return params

    def parameter(self):
        type_token = self.expect('KEYWORD')
        if not type_token:
            return None
        name_token = self.expect('IDENTIFIER')
        if not name_token:
            return None
        return Parameter(type_token.lexeme, name_token.lexeme, type_token.line, type_token.col)

    def statement(self):
        if self.check('KEYWORD'):
            kw = self.current_token.lexeme
            if kw in ['int', 'float', 'char']:
                return self.declaration()
            elif kw == 'if':
                return self.if_statement()
            elif kw == 'while':
                return self.while_statement()
            elif kw == 'for':
                return self.for_statement()
            elif kw == 'break':
                return self.break_statement()
            elif kw == 'continue':
                return self.continue_statement()
            elif kw == 'return':
                return self.return_statement()

        if self.check('LBRACE'):
            return self.block()

        if self.check('IDENTIFIER'):
            next_tok = self.peek()
            if next_tok and next_tok.type == 'OPERATOR':
                if next_tok.lexeme in ['+=', '-=', '*=', '/=']:
                    return self.compound_assignment()
                elif next_tok.lexeme == '=':
                    return self.assignment()

        return self.expression_statement()

    def declaration(self):
        type_token = self.expect('KEYWORD')
        if not type_token:
            return None
        var_type = type_token.lexeme
        line, col = type_token.line, type_token.col

        id_token = self.expect('IDENTIFIER')
        if not id_token:
            return None
        identifier = id_token.lexeme

        value = None
        if self.match('OPERATOR', '='):
            value = self.expression()

        self.expect('SEMICOLON')
        self.symbol_table.declare(identifier, var_type, value)

        return VarDeclaration(var_type, identifier, value, line, col)

    def assignment(self):
        id_token = self.expect('IDENTIFIER')
        if not id_token:
            return None
        identifier = id_token.lexeme
        line, col = id_token.line, id_token.col

        if not self.expect('OPERATOR', '='):
            return None
        
        value = self.expression()
        
        if not self.expect('SEMICOLON'):  # Catches missing semicolon
            return None

        return Assignment(identifier, value, line, col)
    def compound_assignment(self):
        id_token = self.expect('IDENTIFIER')
        if not id_token:
            return None
        identifier = id_token.lexeme
        line, col = id_token.line, id_token.col

        op_token = self.expect('OPERATOR')
        if not op_token:
            return None
        operator = op_token.lexeme

        value = self.expression()
        
        if not self.expect('SEMICOLON'):  # Catches missing semicolon
            return None

        return CompoundAssignment(identifier, operator, value, line, col)

    def if_statement(self):
        if_token = self.expect('KEYWORD', 'if')
        line, col = if_token.line, if_token.col

        if not self.expect('LPAREN'):  # Catches missing '('
            return None
        
        condition = self.logical_or_expression()
        
        if not self.expect('RPAREN'):  # Catches missing ')'
            return None

        then_block = self.statement()

        else_block = None
        if self.match('KEYWORD', 'else'):
            else_block = self.statement()

        return IfStatement(condition, then_block, else_block, line, col)
    def while_statement(self):
        while_token = self.expect('KEYWORD', 'while')
        line, col = while_token.line, while_token.col

        if not self.expect('LPAREN'):  # Catches missing '('
            return None
        
        condition = self.logical_or_expression()
        
        if not self.expect('RPAREN'):  # Catches missing ')'
            return None

        self.loop_depth += 1
        body = self.statement()
        self.loop_depth -= 1

        return WhileStatement(condition, body, line, col)

    def for_statement(self):
        for_token = self.expect('KEYWORD', 'for')
        line, col = for_token.line, for_token.col

        if not self.expect('LPAREN'):  # Catches missing '('
            return None

        init = None
        if not self.check('SEMICOLON'):
            if self.check('KEYWORD'):
                init = self.declaration()
            else:
                init = self.assignment()
        else:
            self.advance()

        condition = None
        if not self.check('SEMICOLON'):
            condition = self.logical_or_expression()
        
        if not self.expect('SEMICOLON'):  # Catches missing ';'
            return None

        update = None
        if not self.check('RPAREN'):
            id_token = self.current_token
            self.advance()
            if self.check('OPERATOR') and self.current_token.lexeme in ['+=', '-=', '*=', '/=']:
                op = self.current_token.lexeme
                self.advance()
                value = self.expression()
                update = CompoundAssignment(id_token.lexeme, op, value, id_token.line, id_token.col)
            elif self.check('OPERATOR') and self.current_token.lexeme == '=':
                self.advance()
                value = self.expression()
                update = Assignment(id_token.lexeme, value, id_token.line, id_token.col)

        if not self.expect('RPAREN'):  # Catches missing ')'
            return None

        self.loop_depth += 1
        body = self.statement()
        self.loop_depth -= 1

        return ForStatement(init, condition, update, body, line, col)
    def break_statement(self):
        token = self.expect('KEYWORD', 'break')
        if self.loop_depth == 0:
            self.report_error("'break' not inside loop")
        self.expect('SEMICOLON')
        return BreakStatement(token.line, token.col)

    def continue_statement(self):
        token = self.expect('KEYWORD', 'continue')
        if self.loop_depth == 0:
            self.report_error("'continue' not inside loop")
        self.expect('SEMICOLON')
        return ContinueStatement(token.line, token.col)

    def return_statement(self):
        token = self.expect('KEYWORD', 'return')
        if self.function_depth == 0:
            self.report_error("'return' not inside function")
        
        value = None
        if not self.check('SEMICOLON'):
            value = self.expression()
        
        if not self.expect('SEMICOLON'):  # Catches missing semicolon
            return None
        
        return ReturnStatement(value, token.line, token.col)

    def block(self):
        if not self.expect('LBRACE'):
            return None  
        
        line = self.current_token.line if self.current_token else 0
        col = self.current_token.col if self.current_token else 0

        statements = []
        while self.current_token and not self.check('RBRACE') and self.current_token.type != 'EOF':
            stmt = self.statement()
            if stmt:
                statements.append(stmt)

        if not self.expect('RBRACE'):  
            return None
        
        return Block(statements, line, col)


    def expression_statement(self):
        expr = self.expression()
        
        if not self.expect('SEMICOLON'):  # Catches missing semicolon
            return None
        
        return expr

    # Expression parsing with precedence
    def logical_or_expression(self):
        left = self.logical_and_expression()
        while self.check('OPERATOR') and self.current_token.lexeme == '||':
            op = self.current_token
            self.advance()
            right = self.logical_and_expression()
            left = LogicalOp('||', left, right, op.line, op.col)
        return left

    def logical_and_expression(self):
        left = self.equality_expression()
        while self.check('OPERATOR') and self.current_token.lexeme == '&&':
            op = self.current_token
            self.advance()
            right = self.equality_expression()
            left = LogicalOp('&&', left, right, op.line, op.col)
        return left

    def equality_expression(self):
        left = self.relational_expression()
        while self.check('OPERATOR') and self.current_token.lexeme in ['==', '!=']:
            op = self.current_token
            self.advance()
            right = self.relational_expression()
            left = ComparisonOp(op.lexeme, left, right, op.line, op.col)
        return left

    def relational_expression(self):
        left = self.expression()
        while self.check('OPERATOR') and self.current_token.lexeme in ['<', '>', '<=', '>=']:
            op = self.current_token
            self.advance()
            right = self.expression()
            left = ComparisonOp(op.lexeme, left, right, op.line, op.col)
        return left

    def expression(self):
        left = self.term()
        while self.check('OPERATOR') and self.current_token.lexeme in ['+', '-']:
            op = self.current_token
            self.advance()
            right = self.term()
            left = BinaryOp(op.lexeme, left, right, op.line, op.col)
        return left

    def term(self):
        left = self.factor()
        while self.check('OPERATOR') and self.current_token.lexeme in ['*', '/', '%']:
            op = self.current_token
            self.advance()
            right = self.factor()
            left = BinaryOp(op.lexeme, left, right, op.line, op.col)
        return left

    def factor(self):
        if self.check('OPERATOR', '!'):
            op = self.current_token
            self.advance()
            expr = self.factor()
            return LogicalOp('!', expr, None, op.line, op.col)

        if self.check('INTEGER_LITERAL') or self.check('FLOAT_LITERAL'):
            token = self.current_token
            self.advance()
            return Number(token.lexeme, token.line, token.col)

        if self.check('STRING_LITERAL'):
            token = self.current_token
            self.advance()
            return StringLiteral(token.lexeme, token.line, token.col)

        if self.check('IDENTIFIER'):
            if self.peek() and self.peek().type == 'LPAREN':
                return self.function_call()
            token = self.current_token
            self.advance()
            return Identifier(token.lexeme, token.line, token.col)

        if self.check('LPAREN'):
            self.advance()
            expr = self.logical_or_expression()
            if not self.expect('RPAREN'):  # Catches missing ')'
                return None
            return expr

        # Better error message for unexpected tokens
        self.report_error(f"Unexpected token in expression: {self.current_token}")
        self.advance()
        return None
    def function_call(self):
        name_token = self.expect('IDENTIFIER')
        func_name = name_token.lexeme
        line, col = name_token.line, name_token.col

        if not self.expect('LPAREN'):  # Catches missing '('
            return None
        
        arguments = self.argument_list()
        
        if not self.expect('RPAREN'):  # Catches missing ')'
            return None

        return FunctionCall(func_name, arguments, line, col)

    def argument_list(self):
        args = []
        if self.check('RPAREN'):
            return args
        
        arg = self.expression()
        if arg:
            args.append(arg)
        
        while self.match('COMMA'):
            arg = self.expression()
            if arg:
                args.append(arg)
        return args





def run_parser_tests():
    
    
    test_cases = [
       
        {
            "name": "Simple Main Function",
            "code": """int main() {
                int x = 10;
                return 0;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '10', 2, 12),
                ('SEMICOLON', ';', 2, 14),
                ('KEYWORD', 'return', 3, 4),
                ('INTEGER_LITERAL', '0', 3, 11),
                ('SEMICOLON', ';', 3, 12),
                ('RBRACE', '}', 4, 0),
                ('EOF', '', 4, 1)
            ]
        },
        
        
        {
            "name": "Main with Multiple Variables",
            "code": """int main() {
                int a = 5;
                float b = 3.14;
                char c = 'x';
                return 0;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'a', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '5', 2, 12),
                ('SEMICOLON', ';', 2, 13),
                ('KEYWORD', 'float', 3, 4),
                ('IDENTIFIER', 'b', 3, 10),
                ('OPERATOR', '=', 3, 12),
                ('FLOAT_LITERAL', '3.14', 3, 14),
                ('SEMICOLON', ';', 3, 18),
                ('KEYWORD', 'char', 4, 4),
                ('IDENTIFIER', 'c', 4, 9),
                ('OPERATOR', '=', 4, 11),
                ('STRING_LITERAL', "'x'", 4, 13),
                ('SEMICOLON', ';', 4, 16),
                ('KEYWORD', 'return', 5, 4),
                ('INTEGER_LITERAL', '0', 5, 11),
                ('SEMICOLON', ';', 5, 12),
                ('RBRACE', '}', 6, 0),
                ('EOF', '', 6, 1)
            ]
        },
        
      
        {
            "name": "Arithmetic Operations in Main",
            "code": """int main() {
                int result = 10 + 20 * 3 - 5 / 2;
                return result;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'result', 2, 8),
                ('OPERATOR', '=', 2, 15),
                ('INTEGER_LITERAL', '10', 2, 17),
                ('OPERATOR', '+', 2, 20),
                ('INTEGER_LITERAL', '20', 2, 22),
                ('OPERATOR', '*', 2, 25),
                ('INTEGER_LITERAL', '3', 2, 27),
                ('OPERATOR', '-', 2, 29),
                ('INTEGER_LITERAL', '5', 2, 31),
                ('OPERATOR', '/', 2, 33),
                ('INTEGER_LITERAL', '2', 2, 35),
                ('SEMICOLON', ';', 2, 36),
                ('KEYWORD', 'return', 3, 4),
                ('IDENTIFIER', 'result', 3, 11),
                ('SEMICOLON', ';', 3, 17),
                ('RBRACE', '}', 4, 0),
                ('EOF', '', 4, 1)
            ]
        },
        
       
        {
            "name": "Assignment in Main",
            "code": """int main() {
                int x = 10;
                x = 20;
                return x;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '10', 2, 12),
                ('SEMICOLON', ';', 2, 14),
                ('IDENTIFIER', 'x', 3, 4),
                ('OPERATOR', '=', 3, 6),
                ('INTEGER_LITERAL', '20', 3, 8),
                ('SEMICOLON', ';', 3, 10),
                ('KEYWORD', 'return', 4, 4),
                ('IDENTIFIER', 'x', 4, 11),
                ('SEMICOLON', ';', 4, 12),
                ('RBRACE', '}', 5, 0),
                ('EOF', '', 5, 1)
            ]
        },
        
        
        {
            "name": "Compound Assignment in Main",
            "code": """int main() {
                int x = 10;
                x += 5;
                x -= 3;
                x *= 2;
                x /= 4;
                return x;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '10', 2, 12),
                ('SEMICOLON', ';', 2, 14),
                ('IDENTIFIER', 'x', 3, 4),
                ('OPERATOR', '+=', 3, 6),
                ('INTEGER_LITERAL', '5', 3, 9),
                ('SEMICOLON', ';', 3, 10),
                ('IDENTIFIER', 'x', 4, 4),
                ('OPERATOR', '-=', 4, 6),
                ('INTEGER_LITERAL', '3', 4, 9),
                ('SEMICOLON', ';', 4, 10),
                ('IDENTIFIER', 'x', 5, 4),
                ('OPERATOR', '*=', 5, 6),
                ('INTEGER_LITERAL', '2', 5, 9),
                ('SEMICOLON', ';', 5, 10),
                ('IDENTIFIER', 'x', 6, 4),
                ('OPERATOR', '/=', 6, 6),
                ('INTEGER_LITERAL', '4', 6, 9),
                ('SEMICOLON', ';', 6, 10),
                ('KEYWORD', 'return', 7, 4),
                ('IDENTIFIER', 'x', 7, 11),
                ('SEMICOLON', ';', 7, 12),
                ('RBRACE', '}', 8, 0),
                ('EOF', '', 8, 1)
            ]
        },
        
        
        {
            "name": "If Statement in Main",
            "code": """int main() {
                int x = 15;
                if (x > 10) {
                    x = 20;
                }
                return x;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '15', 2, 12),
                ('SEMICOLON', ';', 2, 14),
                ('KEYWORD', 'if', 3, 4),
                ('LPAREN', '(', 3, 7),
                ('IDENTIFIER', 'x', 3, 8),
                ('OPERATOR', '>', 3, 10),
                ('INTEGER_LITERAL', '10', 3, 12),
                ('RPAREN', ')', 3, 14),
                ('LBRACE', '{', 3, 16),
                ('IDENTIFIER', 'x', 4, 8),
                ('OPERATOR', '=', 4, 10),
                ('INTEGER_LITERAL', '20', 4, 12),
                ('SEMICOLON', ';', 4, 14),
                ('RBRACE', '}', 5, 4),
                ('KEYWORD', 'return', 6, 4),
                ('IDENTIFIER', 'x', 6, 11),
                ('SEMICOLON', ';', 6, 12),
                ('RBRACE', '}', 7, 0),
                ('EOF', '', 7, 1)
            ]
        },
        
       
        {
            "name": "If-Else Statement in Main",
            "code": """int main() {
                int x = 5;
                int y = 0;
                if (x > 10) {
                    y = 20;
                } else {
                    y = 5;
                }
                return y;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '5', 2, 12),
                ('SEMICOLON', ';', 2, 13),
                ('KEYWORD', 'int', 3, 4),
                ('IDENTIFIER', 'y', 3, 8),
                ('OPERATOR', '=', 3, 10),
                ('INTEGER_LITERAL', '0', 3, 12),
                ('SEMICOLON', ';', 3, 13),
                ('KEYWORD', 'if', 4, 4),
                ('LPAREN', '(', 4, 7),
                ('IDENTIFIER', 'x', 4, 8),
                ('OPERATOR', '>', 4, 10),
                ('INTEGER_LITERAL', '10', 4, 12),
                ('RPAREN', ')', 4, 14),
                ('LBRACE', '{', 4, 16),
                ('IDENTIFIER', 'y', 5, 8),
                ('OPERATOR', '=', 5, 10),
                ('INTEGER_LITERAL', '20', 5, 12),
                ('SEMICOLON', ';', 5, 14),
                ('RBRACE', '}', 6, 4),
                ('KEYWORD', 'else', 6, 6),
                ('LBRACE', '{', 6, 11),
                ('IDENTIFIER', 'y', 7, 8),
                ('OPERATOR', '=', 7, 10),
                ('INTEGER_LITERAL', '5', 7, 12),
                ('SEMICOLON', ';', 7, 13),
                ('RBRACE', '}', 8, 4),
                ('KEYWORD', 'return', 9, 4),
                ('IDENTIFIER', 'y', 9, 11),
                ('SEMICOLON', ';', 9, 12),
                ('RBRACE', '}', 10, 0),
                ('EOF', '', 10, 1)
            ]
        },
        

        {
            "name": "While Loop in Main",
            "code": """int main() {
                int i = 0;
                int sum = 0;
                while (i < 10) {
                    sum += i;
                    i += 1;
                }
                return sum;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'i', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '0', 2, 12),
                ('SEMICOLON', ';', 2, 13),
                ('KEYWORD', 'int', 3, 4),
                ('IDENTIFIER', 'sum', 3, 8),
                ('OPERATOR', '=', 3, 12),
                ('INTEGER_LITERAL', '0', 3, 14),
                ('SEMICOLON', ';', 3, 15),
                ('KEYWORD', 'while', 4, 4),
                ('LPAREN', '(', 4, 10),
                ('IDENTIFIER', 'i', 4, 11),
                ('OPERATOR', '<', 4, 13),
                ('INTEGER_LITERAL', '10', 4, 15),
                ('RPAREN', ')', 4, 17),
                ('LBRACE', '{', 4, 19),
                ('IDENTIFIER', 'sum', 5, 8),
                ('OPERATOR', '+=', 5, 12),
                ('IDENTIFIER', 'i', 5, 15),
                ('SEMICOLON', ';', 5, 16),
                ('IDENTIFIER', 'i', 6, 8),
                ('OPERATOR', '+=', 6, 10),
                ('INTEGER_LITERAL', '1', 6, 13),
                ('SEMICOLON', ';', 6, 14),
                ('RBRACE', '}', 7, 4),
                ('KEYWORD', 'return', 8, 4),
                ('IDENTIFIER', 'sum', 8, 11),
                ('SEMICOLON', ';', 8, 14),
                ('RBRACE', '}', 9, 0),
                ('EOF', '', 9, 1)
            ]
        },
        
       
        {
            "name": "For Loop in Main",
            "code": """int main() {
                int sum = 0;
                for (int i = 0; i < 10; i += 1) {
                    sum += i;
                }
                return sum;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'sum', 2, 8),
                ('OPERATOR', '=', 2, 12),
                ('INTEGER_LITERAL', '0', 2, 14),
                ('SEMICOLON', ';', 2, 15),
                ('KEYWORD', 'for', 3, 4),
                ('LPAREN', '(', 3, 8),
                ('KEYWORD', 'int', 3, 9),
                ('IDENTIFIER', 'i', 3, 13),
                ('OPERATOR', '=', 3, 15),
                ('INTEGER_LITERAL', '0', 3, 17),
                ('SEMICOLON', ';', 3, 18),
                ('IDENTIFIER', 'i', 3, 20),
                ('OPERATOR', '<', 3, 22),
                ('INTEGER_LITERAL', '10', 3, 24),
                ('SEMICOLON', ';', 3, 26),
                ('IDENTIFIER', 'i', 3, 28),
                ('OPERATOR', '+=', 3, 30),
                ('INTEGER_LITERAL', '1', 3, 33),
                ('RPAREN', ')', 3, 34),
                ('LBRACE', '{', 3, 36),
                ('IDENTIFIER', 'sum', 4, 8),
                ('OPERATOR', '+=', 4, 12),
                ('IDENTIFIER', 'i', 4, 15),
                ('SEMICOLON', ';', 4, 16),
                ('RBRACE', '}', 5, 4),
                ('KEYWORD', 'return', 6, 4),
                ('IDENTIFIER', 'sum', 6, 11),
                ('SEMICOLON', ';', 6, 14),
                ('RBRACE', '}', 7, 0),
                ('EOF', '', 7, 1)
            ]
        },
        
        
        {
            "name": "Break Statement in Main",
            "code": """int main() {
                int i = 0;
                while (i < 100) {
                    if (i > 5) {
                        break;
                    }
                    i += 1;
                }
                return i;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'i', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '0', 2, 12),
                ('SEMICOLON', ';', 2, 13),
                ('KEYWORD', 'while', 3, 4),
                ('LPAREN', '(', 3, 10),
                ('IDENTIFIER', 'i', 3, 11),
                ('OPERATOR', '<', 3, 13),
                ('INTEGER_LITERAL', '100', 3, 15),
                ('RPAREN', ')', 3, 18),
                ('LBRACE', '{', 3, 20),
                ('KEYWORD', 'if', 4, 8),
                ('LPAREN', '(', 4, 11),
                ('IDENTIFIER', 'i', 4, 12),
                ('OPERATOR', '>', 4, 14),
                ('INTEGER_LITERAL', '5', 4, 16),
                ('RPAREN', ')', 4, 17),
                ('LBRACE', '{', 4, 19),
                ('KEYWORD', 'break', 5, 12),
                ('SEMICOLON', ';', 5, 17),
                ('RBRACE', '}', 6, 8),
                ('IDENTIFIER', 'i', 7, 8),
                ('OPERATOR', '+=', 7, 10),
                ('INTEGER_LITERAL', '1', 7, 13),
                ('SEMICOLON', ';', 7, 14),
                ('RBRACE', '}', 8, 4),
                ('KEYWORD', 'return', 9, 4),
                ('IDENTIFIER', 'i', 9, 11),
                ('SEMICOLON', ';', 9, 12),
                ('RBRACE', '}', 10, 0),
                ('EOF', '', 10, 1)
            ]
        },
        
       
        {
            "name": "Continue Statement in Main",
            "code": """int main() {
                int sum = 0;
                for (int i = 0; i < 10; i += 1) {
                    if (i == 5) {
                        continue;
                    }
                    sum += i;
                }
                return sum;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'sum', 2, 8),
                ('OPERATOR', '=', 2, 12),
                ('INTEGER_LITERAL', '0', 2, 14),
                ('SEMICOLON', ';', 2, 15),
                ('KEYWORD', 'for', 3, 4),
                ('LPAREN', '(', 3, 8),
                ('KEYWORD', 'int', 3, 9),
                ('IDENTIFIER', 'i', 3, 13),
                ('OPERATOR', '=', 3, 15),
                ('INTEGER_LITERAL', '0', 3, 17),
                ('SEMICOLON', ';', 3, 18),
                ('IDENTIFIER', 'i', 3, 20),
                ('OPERATOR', '<', 3, 22),
                ('INTEGER_LITERAL', '10', 3, 24),
                ('SEMICOLON', ';', 3, 26),
                ('IDENTIFIER', 'i', 3, 28),
                ('OPERATOR', '+=', 3, 30),
                ('INTEGER_LITERAL', '1', 3, 33),
                ('RPAREN', ')', 3, 34),
                ('LBRACE', '{', 3, 36),
                ('KEYWORD', 'if', 4, 8),
                ('LPAREN', '(', 4, 11),
                ('IDENTIFIER', 'i', 4, 12),
                ('OPERATOR', '==', 4, 14),
                ('INTEGER_LITERAL', '5', 4, 17),
                ('RPAREN', ')', 4, 18),
                ('LBRACE', '{', 4, 20),
                ('KEYWORD', 'continue', 5, 12),
                ('SEMICOLON', ';', 5, 20),
                ('RBRACE', '}', 6, 8),
                ('IDENTIFIER', 'sum', 7, 8),
                ('OPERATOR', '+=', 7, 12),
                ('IDENTIFIER', 'i', 7, 15),
                ('SEMICOLON', ';', 7, 16),
                ('RBRACE', '}', 8, 4),
                ('KEYWORD', 'return', 9, 4),
                ('IDENTIFIER', 'sum', 9, 11),
                ('SEMICOLON', ';', 9, 14),
                ('RBRACE', '}', 10, 0),
                ('EOF', '', 10, 1)
            ]
        },
        
        
        {
            "name": "Helper Function with Main",
            "code": """int add(int a, int b) {
                return a + b;
            }

            int main() {
                int result = add(10, 20);
                return result;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'add', 1, 4),
                ('LPAREN', '(', 1, 7),
                ('KEYWORD', 'int', 1, 8),
                ('IDENTIFIER', 'a', 1, 12),
                ('COMMA', ',', 1, 13),
                ('KEYWORD', 'int', 1, 15),
                ('IDENTIFIER', 'b', 1, 19),
                ('RPAREN', ')', 1, 20),
                ('LBRACE', '{', 1, 22),
                ('KEYWORD', 'return', 2, 4),
                ('IDENTIFIER', 'a', 2, 11),
                ('OPERATOR', '+', 2, 13),
                ('IDENTIFIER', 'b', 2, 15),
                ('SEMICOLON', ';', 2, 16),
                ('RBRACE', '}', 3, 0),
                ('KEYWORD', 'int', 5, 0),
                ('IDENTIFIER', 'main', 5, 4),
                ('LPAREN', '(', 5, 8),
                ('RPAREN', ')', 5, 9),
                ('LBRACE', '{', 5, 11),
                ('KEYWORD', 'int', 6, 4),
                ('IDENTIFIER', 'result', 6, 8),
                ('OPERATOR', '=', 6, 15),
                ('IDENTIFIER', 'add', 6, 17),
                ('LPAREN', '(', 6, 20),
                ('INTEGER_LITERAL', '10', 6, 21),
                ('COMMA', ',', 6, 23),
                ('INTEGER_LITERAL', '20', 6, 25),
                ('RPAREN', ')', 6, 27),
                ('SEMICOLON', ';', 6, 28),
                ('KEYWORD', 'return', 7, 4),
                ('IDENTIFIER', 'result', 7, 11),
                ('SEMICOLON', ';', 7, 17),
                ('RBRACE', '}', 8, 0),
                ('EOF', '', 8, 1)
            ]
        },
        
        
        {
            "name": "Function Call in Main",
            "code": """int main() {
                int result = printf("Hello");
                return 0;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'result', 2, 8),
                ('OPERATOR', '=', 2, 15),
                ('IDENTIFIER', 'printf', 2, 17),
                ('LPAREN', '(', 2, 23),
                ('STRING_LITERAL', '"Hello"', 2, 24),
                ('RPAREN', ')', 2, 31),
                ('SEMICOLON', ';', 2, 32),
                ('KEYWORD', 'return', 3, 4),
                ('INTEGER_LITERAL', '0', 3, 11),
                ('SEMICOLON', ';', 3, 12),
                ('RBRACE', '}', 4, 0),
                ('EOF', '', 4, 1)
            ]
        },
        
       
        {
            "name": "Logical Operators in Main",
            "code": """int main() {
                int x = 1;
                if (a > 5 && b < 10 || c == 0) {
                    x = 1;
                }
                return x;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '1', 2, 12),
                ('SEMICOLON', ';', 2, 13),
                ('KEYWORD', 'if', 3, 4),
                ('LPAREN', '(', 3, 7),
                ('IDENTIFIER', 'a', 3, 8),
                ('OPERATOR', '>', 3, 10),
                ('INTEGER_LITERAL', '5', 3, 12),
                ('OPERATOR', '&&', 3, 14),
                ('IDENTIFIER', 'b', 3, 17),
                ('OPERATOR', '<', 3, 19),
                ('INTEGER_LITERAL', '10', 3, 21),
                ('OPERATOR', '||', 3, 24),
                ('IDENTIFIER', 'c', 3, 27),
                ('OPERATOR', '==', 3, 29),
                ('INTEGER_LITERAL', '0', 3, 32),
                ('RPAREN', ')', 3, 33),
                ('LBRACE', '{', 3, 35),
                ('IDENTIFIER', 'x', 4, 8),
                ('OPERATOR', '=', 4, 10),
                ('INTEGER_LITERAL', '1', 4, 12),
                ('SEMICOLON', ';', 4, 13),
                ('RBRACE', '}', 5, 4),
                ('KEYWORD', 'return', 6, 4),
                ('IDENTIFIER', 'x', 6, 11),
                ('SEMICOLON', ';', 6, 12),
                ('RBRACE', '}', 7, 0),
                ('EOF', '', 7, 1)
            ]
        },
        
        
        {
            "name": "Comparison Operators in Main",
            "code": """int main() {
                int x = 5;
                if (x == 5) { }
                if (x != 5) { }
                if (x < 5) { }
                if (x > 5) { }
                if (x <= 5) { }
                if (x >= 5) { }
                return 0;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'x', 2, 8),
                ('OPERATOR', '=', 2, 10),
                ('INTEGER_LITERAL', '5', 2, 12),
                ('SEMICOLON', ';', 2, 13),
                ('KEYWORD', 'if', 3, 4),
                ('LPAREN', '(', 3, 7),
                ('IDENTIFIER', 'x', 3, 8),
                ('OPERATOR', '==', 3, 10),
                ('INTEGER_LITERAL', '5', 3, 13),
                ('RPAREN', ')', 3, 14),
                ('LBRACE', '{', 3, 16),
                ('RBRACE', '}', 3, 18),
                ('KEYWORD', 'if', 4, 4),
                ('LPAREN', '(', 4, 7),
                ('IDENTIFIER', 'x', 4, 8),
                ('OPERATOR', '!=', 4, 10),
                ('INTEGER_LITERAL', '5', 4, 13),
                ('RPAREN', ')', 4, 14),
                ('LBRACE', '{', 4, 16),
                ('RBRACE', '}', 4, 18),
                ('KEYWORD', 'if', 5, 4),
                ('LPAREN', '(', 5, 7),
                ('IDENTIFIER', 'x', 5, 8),
                ('OPERATOR', '<', 5, 10),
                ('INTEGER_LITERAL', '5', 5, 12),
                ('RPAREN', ')', 5, 13),
                ('LBRACE', '{', 5, 15),
                ('RBRACE', '}', 5, 17),
                ('KEYWORD', 'if', 6, 4),
                ('LPAREN', '(', 6, 7),
                ('IDENTIFIER', 'x', 6, 8),
                ('OPERATOR', '>', 6, 10),
                ('INTEGER_LITERAL', '5', 6, 12),
                ('RPAREN', ')', 6, 13),
                ('LBRACE', '{', 6, 15),
                ('RBRACE', '}', 6, 17),
                ('KEYWORD', 'if', 7, 4),
                ('LPAREN', '(', 7, 7),
                ('IDENTIFIER', 'x', 7, 8),
                ('OPERATOR', '<=', 7, 10),
                ('INTEGER_LITERAL', '5', 7, 13),
                ('RPAREN', ')', 7, 14),
                ('LBRACE', '{', 7, 16),
                ('RBRACE', '}', 7, 18),
                ('KEYWORD', 'if', 8, 4),
                ('LPAREN', '(', 8, 7),
                ('IDENTIFIER', 'x', 8, 8),
                ('OPERATOR', '>=', 8, 10),
                ('INTEGER_LITERAL', '5', 8, 13),
                ('RPAREN', ')', 8, 14),
                ('LBRACE', '{', 8, 16),
                ('RBRACE', '}', 8, 18),
                ('KEYWORD', 'return', 9, 4),
                ('INTEGER_LITERAL', '0', 9, 11),
                ('SEMICOLON', ';', 9, 12),
                ('RBRACE', '}', 10, 0),
                ('EOF', '', 10, 1)
            ]
        },
        
        
        {
            "name": "Nested Loops in Main",
            "code": """int main() {
                int count = 0;
                for (int i = 0; i < 3; i += 1) {
                    for (int j = 0; j < 4; j += 1) {
                        count += 1;
                    }
                }
                return count;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'count', 2, 8),
                ('OPERATOR', '=', 2, 14),
                ('INTEGER_LITERAL', '0', 2, 16),
                ('SEMICOLON', ';', 2, 17),
                ('KEYWORD', 'for', 3, 4),
                ('LPAREN', '(', 3, 8),
                ('KEYWORD', 'int', 3, 9),
                ('IDENTIFIER', 'i', 3, 13),
                ('OPERATOR', '=', 3, 15),
                ('INTEGER_LITERAL', '0', 3, 17),
                ('SEMICOLON', ';', 3, 18),
                ('IDENTIFIER', 'i', 3, 20),
                ('OPERATOR', '<', 3, 22),
                ('INTEGER_LITERAL', '3', 3, 24),
                ('SEMICOLON', ';', 3, 25),
                ('IDENTIFIER', 'i', 3, 27),
                ('OPERATOR', '+=', 3, 29),
                ('INTEGER_LITERAL', '1', 3, 32),
                ('RPAREN', ')', 3, 33),
                ('LBRACE', '{', 3, 35),
                ('KEYWORD', 'for', 4, 8),
                ('LPAREN', '(', 4, 12),
                ('KEYWORD', 'int', 4, 13),
                ('IDENTIFIER', 'j', 4, 17),
                ('OPERATOR', '=', 4, 19),
                ('INTEGER_LITERAL', '0', 4, 21),
                ('SEMICOLON', ';', 4, 22),
                ('IDENTIFIER', 'j', 4, 24),
                ('OPERATOR', '<', 4, 26),
                ('INTEGER_LITERAL', '4', 4, 28),
                ('SEMICOLON', ';', 4, 29),
                ('IDENTIFIER', 'j', 4, 31),
                ('OPERATOR', '+=', 4, 33),
                ('INTEGER_LITERAL', '1', 4, 36),
                ('RPAREN', ')', 4, 37),
                ('LBRACE', '{', 4, 39),
                ('IDENTIFIER', 'count', 5, 12),
                ('OPERATOR', '+=', 5, 18),
                ('INTEGER_LITERAL', '1', 5, 21),
                ('SEMICOLON', ';', 5, 22),
                ('RBRACE', '}', 6, 8),
                ('RBRACE', '}', 7, 4),
                ('KEYWORD', 'return', 8, 4),
                ('IDENTIFIER', 'count', 8, 11),
                ('SEMICOLON', ';', 8, 16),
                ('RBRACE', '}', 9, 0),
                ('EOF', '', 9, 1)
            ]
        },
        
        
        {
            "name": "Complex Expression with Precedence in Main",
            "code": """int main() {
                int result = 2 + 3 * 4 - 10 / 2;
                return result;
            }""",
            "tokens": [
                ('KEYWORD', 'int', 1, 0),
                ('IDENTIFIER', 'main', 1, 4),
                ('LPAREN', '(', 1, 8),
                ('RPAREN', ')', 1, 9),
                ('LBRACE', '{', 1, 11),
                ('KEYWORD', 'int', 2, 4),
                ('IDENTIFIER', 'result', 2, 8),
                ('OPERATOR', '=', 2, 15),
                ('INTEGER_LITERAL', '2', 2, 17),
                ('OPERATOR', '+', 2, 19),
                ('INTEGER_LITERAL', '3', 2, 21),
                ('OPERATOR', '*', 2, 23),
                ('INTEGER_LITERAL', '4', 2, 25),
                ('OPERATOR', '-', 2, 27),
                ('INTEGER_LITERAL', '10', 2, 29),
                ('OPERATOR', '/', 2, 32),
                ('INTEGER_LITERAL', '2', 2, 34),
                ('SEMICOLON', ';', 2, 35),
                ('KEYWORD', 'return', 3, 4),
                ('IDENTIFIER', 'result', 3, 11),
                ('SEMICOLON', ';', 3, 17),
                ('RBRACE', '}', 4, 0),
                ('EOF', '', 4, 1)
            ]
        }
    ]
    
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{Fore.YELLOW}{'─'*70}")
        print(f"{Fore.YELLOW}TEST {i}: {test['name']}")
        print(f"{Fore.YELLOW}{'─'*70}")
        
        # Print Input Code
        print(f"\n{Fore.GREEN} INPUT CODE:")
        print(f"{Fore.WHITE}{Style.DIM}{'─'*70}")
        for line in test['code'].split('\n'):
            print(f"{Fore.WHITE}{line}")
        print(f"{Fore.WHITE}{Style.DIM}{'─'*70}")
        
        # Print Tokens
        print(f"\n{Fore.CYAN} TOKENS:")
        print(f"{Fore.WHITE}{Style.DIM}{'─'*70}")
        for token in test['tokens']:
            if len(token) == 4:
                token_type, lexeme, line, col = token
                print(f"{Fore.CYAN}  {token_type:20s} {Fore.WHITE}'{lexeme}'{Style.DIM}  @ {line}:{col}")
            else:
                print(f"{Fore.RED}  Invalid token format: {token}")
        print(f"{Fore.WHITE}{Style.DIM}{'─'*70}")
        
        # Parse and Print AST
        print(f"\n{Fore.MAGENTA} PARSE TREE:")
        print(f"{Fore.WHITE}{Style.DIM}{'─'*70}")
        
        try:
            parser = Parser(test['tokens'])
            ast = parser.parse()
            
            if parser.errors:
                print(f"{Fore.RED} PARSING FAILED!")
                for error in parser.errors:
                    print(f"{Fore.RED}   {error}")
                failed += 1
            else:
                print_ast(ast)
                print(f"\n{Fore.GREEN} PARSING SUCCESSFUL!")
                passed += 1
                
        except Exception as e:
            print(f"{Fore.RED} EXCEPTION: {str(e)}")
            import traceback
            traceback.print_exc()
            failed += 1
        
        print(f"{Fore.WHITE}{Style.DIM}{'─'*70}")
    
    # Final Summary
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}                        TEST SUMMARY")
    print(f"{Fore.CYAN}{'='*70}")
    print(f"{Fore.GREEN} Passed: {passed}/{len(test_cases)}")
    print(f"{Fore.RED} Failed: {failed}/{len(test_cases)}")
    
    if failed == 0:
        print(f"{Fore.GREEN}\n ALL TESTS PASSED! ")
    else:
        print(f"{Fore.RED}\n  SOME TESTS FAILED")
    
    print(f"{Fore.CYAN}{'='*70}\n")


if __name__ == '__main__':
    banner()
    print("\n")
    run_parser_tests()