from colorama import Fore, Style, init

init(autoreset=True)


def banner():
    logo = f"""{Fore.RED}
    ██████   █████  ██████  ███████ ███████ ██████  
    ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ 
    ██████  ███████ ██████  ███████ █████   ██████  
    ██      ██   ██ ██   ██      ██ ██      ██   ██ 
    ██      ██   ██ ██   ██ ███████ ███████ ██   ██ 
    """

    info = f"""
    {Fore.CYAN}Creator{Style.DIM}: ALI Raza
    {Fore.CYAN}Github{Style.DIM}: https://github.com/PatchedDragon/AdvancedParser
    {Fore.CYAN}Status{Style.DIM}: Advance Parser
    {Fore.CYAN}Version{Style.DIM}: 2.0
    """

    print(logo + info)


# =============================================================
#                          AST Nodes
# =============================================================
# Base/Parent class for all nodes
class ASTNode:
    def __init__(self, line=None, col=None):
        self.line = line
        self.col = col


# root node representing the entire program
class Program(ASTNode):
    def __init__(self, statement):
        super().__init__()
        self.statement = statement

    def __repr__(self):
        return f"program(statement={self.statement})"


# to represent numeric literal
class Number(ASTNode):
    def __init__(self, value, line=None, col=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


# representing identifier in AST
class Identifier(ASTNode):
    def __init__(self, name, line=None, col=None):
        super().__init__(line, col)
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"


# respresnts binary operations( +, -, /, * )
class BinaryOp(ASTNode):
    def __init__(self, operator, left, right, line=None, col=None):
        super().__init__(line, col)
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOp('{self.operator}', {self.left}, {self.right})"


# representing variable declaration e.g int x = 5;
class VarDeclaration(ASTNode):
    def __init__(self, var_type, identifier, value, line=None, col=None):
        super().__init__(line, col)
        self.var_type = var_type
        self.identifier = identifier
        self.value = value

    def __repr__(self):
        return f"VarDeclaration(type='{self.var_type}', id='{self.identifier}', value={self.value})"


# represent assignment e.g x=5;
class Assignment(ASTNode):
    def __init__(self, identifier, value, line=None, col=None):
        super().__init__(line, col)
        self.identifier = identifier
        self.value = value

    def __repr__(self):
        return f"Assignment(identifier='{self.identifier}', value={self.value})"


# Represents comparison operations (==, !=, <, >, <=, >=)
class ComparisonOp(ASTNode):
    def __init__(self, operator, left, right, line=None, col=None):
        super().__init__(line, col)
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"ComparisonOp('{self.operator}', {self.left}, {self.right})"


# Represents logical operations (&&, ||, !)
class LogicalOp(ASTNode):
    def __init__(self, operator, left, right=None, line=None, col=None):
        super().__init__(line, col)
        self.operator = operator
        self.left = left
        self.right = right  # None for unary ! operator

    def __repr__(self):
        if self.right:
            return f"LogicalOp('{self.operator}', {self.left}, {self.right})"
        return f"LogicalOp('{self.operator}', {self.left})"


# Represents a block of statements { ... }
class Block(ASTNode):
    def __init__(self, statements, line=None, col=None):
        super().__init__(line, col)
        self.statements = statements

    def __repr__(self):
        return f"Block({len(self.statements)} statements)"


# Represents if-else statement
class IfStatement(ASTNode):
    def __init__(self, condition, then_block, else_block=None, line=None, col=None):
        super().__init__(line, col)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __repr__(self):
        if self.else_block:
            return f"IfStatement(condition={self.condition}, then={self.then_block}, else={self.else_block})"
        return f"IfStatement(condition={self.condition}, then={self.then_block})"


# Represents while loop
class WhileStatement(ASTNode):
    def __init__(self, condition, body, line=None, col=None):
        super().__init__(line, col)
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileStatement(condition={self.condition}, body={self.body})"


# Represents for loop
class ForStatement(ASTNode):
    def __init__(self, init, condition, update, body, line=None, col=None):
        super().__init__(line, col)
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

    def __repr__(self):
        return f"ForStatement(init={self.init}, condition={self.condition}, update={self.update}, body={self.body})"


# Represents break statement
class BreakStatement(ASTNode):
    def __init__(self, line=None, col=None):
        super().__init__(line, col)

    def __repr__(self):
        return "BreakStatement()"


# Represents continue statement
class ContinueStatement(ASTNode):
    def __init__(self, line=None, col=None):
        super().__init__(line, col)

    def __repr__(self):
        return "ContinueStatement()"


# Represents a function parameter
class Parameter(ASTNode):
    def __init__(self, param_type, name, line=None, col=None):
        super().__init__(line, col)
        self.param_type = param_type
        self.name = name

    def __repr__(self):
        return f"Parameter(type='{self.param_type}', name='{self.name}')"


# Represents a function declaration
class FunctionDeclaration(ASTNode):
    def __init__(self, return_type, name, parameters, body, line=None, col=None):
        super().__init__(line, col)
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        params_str = ', '.join([str(p) for p in self.parameters])
        return f"FunctionDeclaration(return_type='{self.return_type}', name='{self.name}', params=[{params_str}], body={self.body})"


# Represents a function call
class FunctionCall(ASTNode):
    def __init__(self, name, arguments, line=None, col=None):
        super().__init__(line, col)
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        args_str = ', '.join([str(a) for a in self.arguments])
        return f"FunctionCall(name='{self.name}', args=[{args_str}])"


# Represents a return statement
class ReturnStatement(ASTNode):
    def __init__(self, value=None, line=None, col=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self):
        if self.value:
            return f"ReturnStatement(value={self.value})"
        return "ReturnStatement()"

class CompoundAssignment(ASTNode):
    """Handles +=, -=, *=, /="""
    def __init__(self, identifier, operator, value, line=None, col=None):
        super().__init__(line, col)
        self.identifier = identifier
        self.operator = operator  # '+=', '-=', '*=', '/='
        self.value = value

    def __repr__(self):
        return f"CompoundAssignment('{self.identifier}' {self.operator} {self.value})"


class StringLiteral(ASTNode):
    """Handles string literals like "Hello World" """
    def __init__(self, value, line=None, col=None):
        super().__init__(line, col)
        self.value = value

    def __repr__(self):
        return f"String({self.value})"



#==============================================================
def print_ast(node, indent=0, prefix=""):
    """
    Recursively print the complete AST tree structure
    """
    indent_str = "  " * indent

    if node is None:
        print(f"{indent_str}{prefix}None")
        return

    # Program node
    if isinstance(node, Program):
        print(f"{indent_str}{prefix}Program")
        for i, stmt in enumerate(node.statement):
            print_ast(stmt, indent + 1, f"Statement[{i}]: ")

    # Function Declaration
    elif isinstance(node, FunctionDeclaration):
        print(f"{indent_str}{prefix}FunctionDeclaration")
        print(f"{indent_str}  return_type: {node.return_type}")
        print(f"{indent_str}  name: {node.name}")
        print(f"{indent_str}  parameters: [")
        for param in node.parameters:
            print_ast(param, indent + 2, "")
        print(f"{indent_str}  ]")
        print(f"{indent_str}  body:")
        print_ast(node.body, indent + 2, "")

    # Parameter
    elif isinstance(node, Parameter):
        print(f"{indent_str}{prefix}Parameter(type={node.param_type}, name={node.name})")

    # Block
    elif isinstance(node, Block):
        print(f"{indent_str}{prefix}Block ({len(node.statements)} statements)")
        for i, stmt in enumerate(node.statements):
            print_ast(stmt, indent + 1, f"[{i}]: ")

    # Variable Declaration
    elif isinstance(node, VarDeclaration):
        print(f"{indent_str}{prefix}VarDeclaration")
        print(f"{indent_str}  type: {node.var_type}")
        print(f"{indent_str}  identifier: {node.identifier}")
        print(f"{indent_str}  value:")
        print_ast(node.value, indent + 2, "")

    # Assignment
    elif isinstance(node, Assignment):
        print(f"{indent_str}{prefix}Assignment")
        print(f"{indent_str}  identifier: {node.identifier}")
        print(f"{indent_str}  value:")
        print_ast(node.value, indent + 2, "")

    # Compound Assignment
    elif isinstance(node, CompoundAssignment):
        print(f"{indent_str}{prefix}CompoundAssignment")
        print(f"{indent_str}  identifier: {node.identifier}")
        print(f"{indent_str}  operator: {node.operator}")
        print(f"{indent_str}  value:")
        print_ast(node.value, indent + 2, "")

    # If Statement
    elif isinstance(node, IfStatement):
        print(f"{indent_str}{prefix}IfStatement")
        print(f"{indent_str}  condition:")
        print_ast(node.condition, indent + 2, "")
        print(f"{indent_str}  then:")
        print_ast(node.then_block, indent + 2, "")
        if node.else_block:
            print(f"{indent_str}  else:")
            print_ast(node.else_block, indent + 2, "")

    # While Statement
    elif isinstance(node, WhileStatement):
        print(f"{indent_str}{prefix}WhileStatement")
        print(f"{indent_str}  condition:")
        print_ast(node.condition, indent + 2, "")
        print(f"{indent_str}  body:")
        print_ast(node.body, indent + 2, "")

    # For Statement
    elif isinstance(node, ForStatement):
        print(f"{indent_str}{prefix}ForStatement")
        print(f"{indent_str}  init:")
        print_ast(node.init, indent + 2, "")
        print(f"{indent_str}  condition:")
        print_ast(node.condition, indent + 2, "")
        print(f"{indent_str}  update:")
        print_ast(node.update, indent + 2, "")
        print(f"{indent_str}  body:")
        print_ast(node.body, indent + 2, "")

    # Function Call
    elif isinstance(node, FunctionCall):
        print(f"{indent_str}{prefix}FunctionCall")
        print(f"{indent_str}  name: {node.name}")
        print(f"{indent_str}  arguments: [")
        for i, arg in enumerate(node.arguments):
            print_ast(arg, indent + 2, f"arg[{i}]: ")
        print(f"{indent_str}  ]")

    # Return Statement
    elif isinstance(node, ReturnStatement):
        print(f"{indent_str}{prefix}ReturnStatement")
        if node.value:
            print(f"{indent_str}  value:")
            print_ast(node.value, indent + 2, "")

    # Break/Continue
    elif isinstance(node, BreakStatement):
        print(f"{indent_str}{prefix}BreakStatement")
    elif isinstance(node, ContinueStatement):
        print(f"{indent_str}{prefix}ContinueStatement")

    # Binary Operation
    elif isinstance(node, BinaryOp):
        print(f"{indent_str}{prefix}BinaryOp(operator='{node.operator}')")
        print(f"{indent_str}  left:")
        print_ast(node.left, indent + 2, "")
        print(f"{indent_str}  right:")
        print_ast(node.right, indent + 2, "")

    # Comparison Operation
    elif isinstance(node, ComparisonOp):
        print(f"{indent_str}{prefix}ComparisonOp(operator='{node.operator}')")
        print(f"{indent_str}  left:")
        print_ast(node.left, indent + 2, "")
        print(f"{indent_str}  right:")
        print_ast(node.right, indent + 2, "")

    # Logical Operation
    elif isinstance(node, LogicalOp):
        print(f"{indent_str}{prefix}LogicalOp(operator='{node.operator}')")
        print(f"{indent_str}  left:")
        print_ast(node.left, indent + 2, "")
        if node.right:
            print(f"{indent_str}  right:")
            print_ast(node.right, indent + 2, "")

    # Leaf nodes
    elif isinstance(node, Number):
        print(f"{indent_str}{prefix}Number({node.value})")
    elif isinstance(node, StringLiteral):
        print(f"{indent_str}{prefix}StringLiteral({node.value})")
    elif isinstance(node, Identifier):
        print(f"{indent_str}{prefix}Identifier({node.name})")

    else:
        print(f"{indent_str}{prefix}{node.__class__.__name__}: {node}")


# =============================================================
#                          Symbol Table
# =============================================================
class Symbol:
    def __init__(self, name, symbol_type, value=None, is_function=False, params=None):
        self.name = name
        self.type = symbol_type
        self.value = value
        self.is_function = is_function
        self.params = params or []

    def __repr__(self):
        if self.is_function:
            param_types = ', '.join([p.param_type for p in self.params])
            return f"Symbol(name='{self.name}', type={self.type}, function=True, params=[{param_types}])"
        return f"Symbol(name='{self.name}', type={self.type})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self._add_stdlib_functions()

    def declare(self, name, symbol_type, value=None, is_function=False, params=None):
        """adding symbol in symbol table if not exist"""
        if name in self.symbols:
            return False
        self.symbols[name] = Symbol(name, symbol_type, value, is_function, params)
        return True

    def lookup(self, name):
        """To look-up a symbol in table"""
        return self.symbols.get(name)

    def exists(self, name):
        return name in self.symbols

    def __repr__(self):
        return f"SymbolTable({self.symbols})"

    def _add_stdlib_functions(self):
        """Add common C standard library functions"""
        stdlib_funcs = [
            ('printf', 'int', True),  # True = variadic (skip param check)
            ('scanf', 'int', True),
            ('malloc', 'void*', False),
            ('free', 'void', False),
            ('strlen', 'int', False),
            ('strcpy', 'char*', False),
            ('strcmp', 'int', False),
        ]
        for name, return_type, is_variadic in stdlib_funcs:
            symbol = Symbol(name, return_type, is_function=True, params=[])
            symbol.is_variadic = is_variadic
            self.symbols[name] = symbol


# =============================================================
#                          Token Class
# =============================================================
class Token:
    def __init__(self, token_type, lexeme, line, col):
        self.type = token_type
        self.lexeme = lexeme
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.type}, {self.lexeme}, {self.line}, {self.col})"


# =======================
# Parser Implementation
# =======================

class Parser:

    def __init__(self, tokens):
        # Convert raw tokens to Token objects for easier handling
        self.tokens = [Token(*t) if len(t) == 4 else Token(t[0], t[1], t[2], 0)
                       for t in tokens]
        self.pos = 0  # Current position in token stream
        self.current_token = self.tokens[0] if self.tokens else None
        self.symbol_table = SymbolTable()
        self.errors = []  # Store syntax errors
        self.loop_depth = 0  # Track if we're inside a loop (for break/continue)
        self.function_depth = 0  # Track if we're inside a function (for return)

    # =======================
    # Token Management
    # =======================

    def advance(self):
        """Move to the next token in the stream"""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def peek(self, offset=1):
        """Look ahead at future tokens without consuming them"""
        peek_pos = self.pos + offset
        if peek_pos < len(self.tokens):
            return self.tokens[peek_pos]
        return None

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

        # Error detected - report it
        expected = f"{token_type}"
        if lexeme:
            expected += f":'{lexeme}'"
        actual = f"{self.current_token.type}:'{self.current_token.lexeme}'" if self.current_token else "EOF"
        self.report_error(f"Expected {expected}, got {actual}")
        return None

    # =======================
    # Error Handling
    # =======================

    def report_error(self, message):
        """Record a syntax error with position information"""
        if self.current_token:
            line = self.current_token.line
            col = self.current_token.col
            error_msg = f"Syntax Error at {line}:{col} - {message}"
        else:
            error_msg = f"Syntax Error at EOF - {message}"

        self.errors.append(error_msg)
        print(f"❌ {error_msg}")

    def synchronize(self):
        sync_tokens = {'SEMICOLON', 'EOF', 'RBRACE'}
        sync_keywords = {'int', 'float', 'char', 'void', 'if', 'while', 'for', 'return', 'break', 'continue'}

        while self.current_token:
            # Stop at semicolon, right brace, or EOF
            if self.current_token.type in sync_tokens:
                if self.current_token.type == 'SEMICOLON':
                    self.advance()  # Consume the semicolon
                return

            # Stop at statement-starting keywords
            if (self.current_token.type == 'KEYWORD' and
                    self.current_token.lexeme in sync_keywords):
                return

            self.advance()

    # =======================
    # Grammar Rules (Recursive Descent)
    # =======================

    def parse(self):
        print("🔍 Starting parsing process...")
        print(f"📝 Total tokens received from lexer: {len(self.tokens)}")
        print()

        try:
            ast = self.program()

            if self.errors:
                print(f"\n⚠️  Parsing completed with {len(self.errors)} error(s)")
            else:
                print(f"\n✅ Parsing completed successfully!")

            # Print the COMPLETE AST tree
            print("\n" + "=" * 70)
            print("COMPLETE AST TREE:")
            print("=" * 70)
            print_ast(ast)
            print("=" * 70)

            return ast
        except Exception as e:
            self.report_error(f"Fatal parsing error: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    def program(self):
        statements = []

        # Parse statements until EOF
        while self.current_token and self.current_token.type != 'EOF':
            stmt = self.declaration_or_statement()
            if stmt:
                statements.append(stmt)

            # If error occurred, try to recover
            if self.errors and self.current_token and self.current_token.type != 'EOF':
                self.synchronize()

        return Program(statements)

    def declaration_or_statement(self):
        """Parse either a function declaration or a regular statement"""
        # Check if this is a function declaration
        # Pattern: type identifier (
        if self.check('KEYWORD'):
            keyword = self.current_token.lexeme
            if keyword in ['int', 'float', 'double', 'char', 'bool', 'string', 'void']:
                # Look ahead to see if it's a function
                next_token = self.peek()
                next_next_token = self.peek(2)
                if (next_token and next_token.type == 'IDENTIFIER' and
                        next_next_token and next_next_token.type == 'LPAREN'):
                    return self.function_declaration()

        return self.statement()

    def function_declaration(self):
        """Parse function declaration: type identifier(params) { body }"""
        # Get return type
        type_token = self.expect('KEYWORD')
        if not type_token:
            return None

        return_type = type_token.lexeme
        line, col = type_token.line, type_token.col

        # Get function name
        name_token = self.expect('IDENTIFIER')
        if not name_token:
            return None

        func_name = name_token.lexeme

        # Parse parameter list
        if not self.expect('LPAREN'):
            return None

        parameters = self.parameter_list()

        if not self.expect('RPAREN'):
            return None

        # Add function to symbol table
        if not self.symbol_table.declare(func_name, return_type, is_function=True, params=parameters):
            self.report_error(f"Function '{func_name}' already declared")

        # Parse function body
        self.function_depth += 1
        body = self.block()
        self.function_depth -= 1

        return FunctionDeclaration(return_type, func_name, parameters, body, line, col)

    def parameter_list(self):
        """Parse function parameters: type id, type id, ..."""
        parameters = []

        # Empty parameter list
        if self.check('RPAREN'):
            return parameters

        # Parse first parameter
        param = self.parameter()
        if param:
            parameters.append(param)

        # Parse additional parameters
        while self.match('COMMA'):
            param = self.parameter()
            if param:
                parameters.append(param)

        return parameters

    def parameter(self):
        """Parse single parameter: type identifier"""
        # Get parameter type
        type_token = self.expect('KEYWORD')
        if not type_token:
            return None

        param_type = type_token.lexeme
        line, col = type_token.line, type_token.col

        # Get parameter name
        name_token = self.expect('IDENTIFIER')
        if not name_token:
            return None

        param_name = name_token.lexeme

        # un-commit it when i have parameter already declared error
        #if not self.symbol_table.declare(param_name, param_type):
        #self.report_error(f"Parameter '{param_name}' already declared")

        return Parameter(param_type, param_name, line, col)

    def statement(self):
        """Parse any type of statement"""
        if self.check('KEYWORD'):
            keyword = self.current_token.lexeme

            if keyword in ['int', 'float', 'double', 'char', 'bool', 'string']:
                return self.declaration()
            elif keyword == 'if':
                return self.if_statement()
            elif keyword == 'while':
                return self.while_statement()
            elif keyword == 'for':
                return self.for_statement()
            elif keyword == 'break':
                return self.break_statement()
            elif keyword == 'continue':
                return self.continue_statement()
            elif keyword == 'return':
                return self.return_statement()

        if self.check('LBRACE'):
            return self.block()

        if self.check('IDENTIFIER'):
            next_token = self.peek()
            if next_token and next_token.type == 'OPERATOR' and next_token.lexeme in ['+=', '-=', '*=', '/=']:
                return self.compound_assignment()
            elif next_token and next_token.type == 'OPERATOR' and next_token.lexeme == '=':
                return self.assignment()
            elif next_token and next_token.type == 'LPAREN':
                return self.expression_statement()

        return self.expression_statement()

    def compound_assignment(self):
        """Handle +=, -=, *=, /="""
        id_token = self.expect('IDENTIFIER')
        if not id_token:
            return None

        identifier = id_token.lexeme
        line, col = id_token.line, id_token.col

        if not self.symbol_table.exists(identifier):
            self.report_error(f"Variable '{identifier}' used before declaration")

        # Get the compound operator
        op_token = self.expect('OPERATOR')
        if not op_token:
            return None

        operator = op_token.lexeme  # '+=', '-=', '*=', '/='

        # Parse the right-hand side
        value = self.expression()

        self.expect('SEMICOLON')

        return CompoundAssignment(identifier, operator, value, line, col)

    def return_statement(self):
        """Parse return statement: return expression;"""
        return_token = self.expect('KEYWORD', 'return')
        if not return_token:
            return None

        line, col = return_token.line, return_token.col

        # Check if we're inside a function
        if self.function_depth == 0:
            self.report_error("'return' statement not inside a function")

        # Check for return value
        value = None
        if not self.check('SEMICOLON'):
            value = self.expression()

        self.expect('SEMICOLON')

        return ReturnStatement(value, line, col)

    def block(self):
        """Parse a block of statements: { statement* }"""
        if not self.expect('LBRACE'):
            return None

        line = self.current_token.line if self.current_token else None
        col = self.current_token.col if self.current_token else None

        statements = []

        while self.current_token and not self.check('RBRACE') and self.current_token.type != 'EOF':
            stmt = self.statement()
            if stmt:
                statements.append(stmt)

            # Error recovery
            if self.errors and self.current_token and not self.check('RBRACE'):
                self.synchronize()

        self.expect('RBRACE')

        return Block(statements, line, col)

    def if_statement(self):
        """Parse if-else statement: if (condition) { ... } else { ... }"""
        if_token = self.expect('KEYWORD', 'if')
        if not if_token:
            return None

        line, col = if_token.line, if_token.col

        # Expect opening parenthesis
        if not self.expect('LPAREN'):
            return None

        # Parse condition
        condition = self.logical_or_expression()

        # Expect closing parenthesis
        if not self.expect('RPAREN'):
            return None

        # Parse then block
        then_block = self.statement()

        # Check for else clause
        else_block = None
        if self.match('KEYWORD', 'else'):
            else_block = self.statement()

        return IfStatement(condition, then_block, else_block, line, col)

    def while_statement(self):
        """Parse while loop: while (condition) { ... }"""
        while_token = self.expect('KEYWORD', 'while')
        if not while_token:
            return None

        line, col = while_token.line, while_token.col

        # Expect opening parenthesis
        if not self.expect('LPAREN'):
            return None

        # Parse condition
        condition = self.logical_or_expression()

        # Expect closing parenthesis
        if not self.expect('RPAREN'):
            return None

        # Increment loop depth
        self.loop_depth += 1

        # Parse body
        body = self.statement()

        # Decrement loop depth
        self.loop_depth -= 1

        return WhileStatement(condition, body, line, col)

    def for_statement(self):
        """Parse for loop: for (init; condition; update) { ... }"""
        for_token = self.expect('KEYWORD', 'for')
        if not for_token:
            return None

        line, col = for_token.line, for_token.col

        if not self.expect('LPAREN'):
            return None

        # Parse initialization
        init = None
        if not self.check('SEMICOLON'):
            if self.check('KEYWORD'):
                init = self.declaration()
            else:
                # CHECK for compound assignment in init
                next_token = self.peek()
                if next_token and next_token.type == 'OPERATOR' and next_token.lexeme in ['+=', '-=', '*=', '/=']:
                    init = self.compound_assignment()
                else:
                    init = self.assignment()
        else:
            self.advance()

        # Parse condition
        condition = None
        if not self.check('SEMICOLON'):
            condition = self.logical_or_expression()
        self.expect('SEMICOLON')

        # Parse update
        update = None
        if not self.check('RPAREN'):
            if self.check('IDENTIFIER'):
                id_token = self.current_token
                identifier = id_token.lexeme
                self.advance()

                # CHECK for compound assignment
                if self.check('OPERATOR') and self.current_token.lexeme in ['+=', '-=', '*=', '/=']:
                    op = self.current_token.lexeme
                    self.advance()
                    value = self.expression()
                    update = CompoundAssignment(identifier, op, value, id_token.line, id_token.col)
                elif self.match('OPERATOR', '='):
                    value = self.expression()
                    update = Assignment(identifier, value, id_token.line, id_token.col)

        if not self.expect('RPAREN'):
            return None

        self.loop_depth += 1
        body = self.statement()
        self.loop_depth -= 1

        return ForStatement(init, condition, update, body, line, col)

    def break_statement(self):
        """Parse break statement: break;"""
        break_token = self.expect('KEYWORD', 'break')
        if not break_token:
            return None

        line, col = break_token.line, break_token.col

        # Check if we're inside a loop
        if self.loop_depth == 0:
            self.report_error("'break' statement not inside a loop")

        self.expect('SEMICOLON')

        return BreakStatement(line, col)

    def continue_statement(self):
        """Parse continue statement: continue;"""
        continue_token = self.expect('KEYWORD', 'continue')
        if not continue_token:
            return None

        line, col = continue_token.line, continue_token.col

        # Check if we're inside a loop
        if self.loop_depth == 0:
            self.report_error("'continue' statement not inside a loop")

        self.expect('SEMICOLON')

        return ContinueStatement(line, col)

    def declaration(self):
        """Parse variable declaration: type identifier = expression;"""
        # Get type keyword
        type_token = self.expect('KEYWORD')
        if not type_token:
            return None

        var_type = type_token.lexeme
        line, col = type_token.line, type_token.col

        # Get identifier
        id_token = self.expect('IDENTIFIER')
        if not id_token:
            return None

        identifier = id_token.lexeme

        # Check if there's an initialization
        value = None
        if self.match('OPERATOR', '='):
            value = self.expression()

        # Expect semicolon
        self.expect('SEMICOLON')

        # Add to symbol table
        if not self.symbol_table.declare(identifier, var_type, value):
            self.report_error(f"Variable '{identifier}' already declared")

        return VarDeclaration(var_type, identifier, value, line, col)

    def assignment(self):
        """Parse assignment: identifier = expression;"""
        id_token = self.expect('IDENTIFIER')
        if not id_token:
            return None

        identifier = id_token.lexeme
        line, col = id_token.line, id_token.col

        # Remove this check or make it a warning instead of error
        # This allows parameters to be assigned without declaring them first
        # if not self.symbol_table.exists(identifier):
        #     self.report_error(f"Variable '{identifier}' used before declaration")

        if not self.expect('OPERATOR', '='):
            return None

        value = self.expression()

        self.expect('SEMICOLON')

        return Assignment(identifier, value, line, col)

    def expression_statement(self):
        """Parse expression as a statement"""
        expr = self.expression()
        self.expect('SEMICOLON')
        return expr

    # =======================
    # Expression Parsing with Precedence
    # =======================

    def logical_or_expression(self):
        """Parse logical OR: expression || expression"""
        left = self.logical_and_expression()

        while self.check('OPERATOR') and self.current_token.lexeme == '||':
            op_token = self.current_token
            self.advance()
            right = self.logical_and_expression()
            left = LogicalOp('||', left, right, op_token.line, op_token.col)

        return left

    def logical_and_expression(self):
        """Parse logical AND: expression && expression"""
        left = self.equality_expression()

        while self.check('OPERATOR') and self.current_token.lexeme == '&&':
            op_token = self.current_token
            self.advance()
            right = self.equality_expression()
            left = LogicalOp('&&', left, right, op_token.line, op_token.col)

        return left

    def equality_expression(self):
        """Parse equality: expression == expression, expression != expression"""
        left = self.relational_expression()

        while self.check('OPERATOR') and self.current_token.lexeme in ['==', '!=']:
            op_token = self.current_token
            operator = op_token.lexeme
            self.advance()
            right = self.relational_expression()
            left = ComparisonOp(operator, left, right, op_token.line, op_token.col)

        return left

    def relational_expression(self):
        """Parse relational: expression < expression, etc."""
        left = self.expression()

        while self.check('OPERATOR') and self.current_token.lexeme in ['<', '>', '<=', '>=']:
            op_token = self.current_token
            operator = op_token.lexeme
            self.advance()
            right = self.expression()
            left = ComparisonOp(operator, left, right, op_token.line, op_token.col)

        return left

    def expression(self):
        """Parse addition/subtraction"""
        left = self.term()

        # Handle left-associative operators
        while self.check('OPERATOR') and self.current_token.lexeme in ['+', '-']:
            op_token = self.current_token
            operator = op_token.lexeme
            line, col = op_token.line, op_token.col
            self.advance()

            right = self.term()
            left = BinaryOp(operator, left, right, line, col)

        return left

    def term(self):
        """Parse multiplication/division"""
        left = self.factor()

        # Handle left-associative operators
        while self.check('OPERATOR') and self.current_token.lexeme in ['*', '/', '%']:
            op_token = self.current_token
            operator = op_token.lexeme
            line, col = op_token.line, op_token.col
            self.advance()

            right = self.factor()
            left = BinaryOp(operator, left, right, line, col)

        return left

    def factor(self):
        """Parse primary expressions"""
        # Logical NOT
        if self.check('OPERATOR', '!'):
            op_token = self.current_token
            self.advance()
            expr = self.factor()
            return LogicalOp('!', expr, None, op_token.line, op_token.col)

        # Changed from 'NUMBER' to 'INTEGER_LITERAL'
        if self.check('INTEGER_LITERAL'):
            token = self.current_token
            self.advance()
            return Number(token.lexeme, token.line, token.col)

        # Added FLOAT_LITERAL support
        if self.check('FLOAT_LITERAL'):
            token = self.current_token
            self.advance()
            return Number(token.lexeme, token.line, token.col)

        # Added STRING_LITERAL support
        if self.check('STRING_LITERAL'):
            token = self.current_token
            self.advance()
            return StringLiteral(token.lexeme, token.line, token.col)

        # Identifier (variable reference or function call)
        elif self.check('IDENTIFIER'):
            token = self.current_token
            identifier = token.lexeme

            if self.peek() and self.peek().type == 'LPAREN':
                return self.function_call()

            # REMOVED the check that causes "Undefined variable" for valid vars
            # Variables will be checked during semantic analysis
            # Just allow them during parsing

            self.advance()
            return Identifier(identifier, token.line, token.col)

        # Parenthesized expression
        elif self.check('LPAREN'):
            self.advance()
            expr = self.logical_or_expression()
            self.expect('RPAREN')
            return expr

        else:
            self.report_error(f"Unexpected token: {self.current_token.type}:'{self.current_token.lexeme}'")
            self.advance()
            return None

    def function_call(self):
        """Parse function call: identifier(arguments)"""
        name_token = self.expect('IDENTIFIER')
        if not name_token:
            return None

        func_name = name_token.lexeme
        line, col = name_token.line, name_token.col

        symbol = self.symbol_table.lookup(func_name)
        if not symbol:
            self.report_error(f"Undefined function '{func_name}'")
        elif not symbol.is_function:
            self.report_error(f"'{func_name}' is not a function")

        if not self.expect('LPAREN'):
            return None

        arguments = self.argument_list()

        if not self.expect('RPAREN'):
            return None

        # Check argument count (skip for variadic functions like printf)
        if symbol and symbol.is_function:
            # Check if function is variadic
            is_variadic = getattr(symbol, 'is_variadic', False)
            if not is_variadic:
                expected_params = len(symbol.params)
                actual_args = len(arguments)
                if expected_params != actual_args:
                    self.report_error(f"Function '{func_name}' expects {expected_params} arguments, got {actual_args}")

        return FunctionCall(func_name, arguments, line, col)

    def argument_list(self):
        """Parse function arguments: expression, expression, ..."""
        arguments = []

        # Empty argument list
        if self.check('RPAREN'):
            return arguments

        # Parse first argument
        arg = self.expression()
        if arg:
            arguments.append(arg)

        # Parse additional arguments
        while self.match('COMMA'):
            arg = self.expression()
            if arg:
                arguments.append(arg)

        return arguments


# =======================
# Complete Test Cases Suite
# =======================

def run_test_case_1():
    """Test Case 1: Variable Declaration with Initialization"""
    print("=" * 70)
    print("TEST CASE 1: Variable Declaration with Initialization")
    print("Input: int x = 5;")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'x', 1, 4),
        ('OPERATOR', '=', 1, 6),
        ('INTEGER_LITERAL', '5', 1, 8),
        ('SEMICOLON', ';', 1, 9),
        ('EOF', '', 1, 10)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n📚 Symbol Table:")
    print(f"   {parser.symbol_table}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_2():
    """Test Case 2: Complex Expression with Operator Precedence"""
    print("=" * 70)
    print("TEST CASE 2: Complex Expression with Operator Precedence")
    print("Input: int result = 10 + 20 * 2;")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'result', 1, 4),
        ('OPERATOR', '=', 1, 11),
        ('INTEGER_LITERAL', '10', 1, 13),
        ('OPERATOR', '+', 1, 16),
        ('INTEGER_LITERAL', '20', 1, 18),
        ('OPERATOR', '*', 1, 21),
        ('INTEGER_LITERAL', '2', 1, 23),
        ('SEMICOLON', ';', 1, 24),
        ('EOF', '', 2, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n📚 Symbol Table:")
    print(f"   {parser.symbol_table}")

    print("\n💡 Note: Multiplication has higher precedence, so:")
    print("   Expression parsed as: 10 + (20 * 2), not (10 + 20) * 2")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_simple_function():
    """Test Case: Simple Function Declaration"""
    print("=" * 70)
    print("TEST CASE: Simple Function Declaration")
    print("Input:")
    print("   void hello() {")
    print("       int x = 5;")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'void', 1, 0),
        ('IDENTIFIER', 'hello', 1, 5),
        ('LPAREN', '(', 1, 10),
        ('RPAREN', ')', 1, 11),
        ('LBRACE', '{', 1, 13),
        ('KEYWORD', 'int', 2, 4),
        ('IDENTIFIER', 'x', 2, 8),
        ('OPERATOR', '=', 2, 10),
        ('INTEGER_LITERAL', '5', 2, 12),
        ('SEMICOLON', ';', 2, 13),
        ('RBRACE', '}', 3, 0),
        ('EOF', '', 4, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n📚 Symbol Table:")
    for name, symbol in parser.symbol_table.symbols.items():
        print(f"   {symbol}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_function_with_params():
    """Test Case: Function with Parameters"""
    print("=" * 70)
    print("TEST CASE: Function with Parameters")
    print("Input:")
    print("   int add(int a, int b) {")
    print("       return a + b;")
    print("   }")
    print("=" * 70)

    tokens = [
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
        ('EOF', '', 4, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n📚 Symbol Table:")
    for name, symbol in parser.symbol_table.symbols.items():
        print(f"   {symbol}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_function_call():
    """Test Case: Function Call"""
    print("=" * 70)
    print("TEST CASE: Function Call")
    print("Input:")
    print("   int add(int a, int b) {")
    print("       return a + b;")
    print("   }")
    print("   int main() {")
    print("       int result = add(5, 10);")
    print("       return 0;")
    print("   }")
    print("=" * 70)

    tokens = [
        # Function declaration: int add(int a, int b)
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
        # Function declaration: int main()
        ('KEYWORD', 'int', 4, 0),
        ('IDENTIFIER', 'main', 4, 4),
        ('LPAREN', '(', 4, 8),
        ('RPAREN', ')', 4, 9),
        ('LBRACE', '{', 4, 11),
        ('KEYWORD', 'int', 5, 4),
        ('IDENTIFIER', 'result', 5, 8),
        ('OPERATOR', '=', 5, 15),
        ('IDENTIFIER', 'add', 5, 17),
        ('LPAREN', '(', 5, 20),
        ('INTEGER_LITERAL', '5', 5, 21),
        ('COMMA', ',', 5, 22),
        ('INTEGER_LITERAL', '10', 5, 24),
        ('RPAREN', ')', 5, 26),
        ('SEMICOLON', ';', 5, 27),
        ('KEYWORD', 'return', 6, 4),
        ('INTEGER_LITERAL', '0', 6, 11),
        ('SEMICOLON', ';', 6, 12),
        ('RBRACE', '}', 7, 0),
        ('EOF', '', 8, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n📚 Symbol Table:")
    for name, symbol in parser.symbol_table.symbols.items():
        print(f"   {symbol}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_recursive_function():
    """Test Case: Recursive Function (Factorial)"""
    print("=" * 70)
    print("TEST CASE: Recursive Function (Factorial)")
    print("Input:")
    print("   int factorial(int n) {")
    print("       if (n <= 1) {")
    print("           return 1;")
    print("       }")
    print("       return n * factorial(n - 1);")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'factorial', 1, 4),
        ('LPAREN', '(', 1, 13),
        ('KEYWORD', 'int', 1, 14),
        ('IDENTIFIER', 'n', 1, 18),
        ('RPAREN', ')', 1, 19),
        ('LBRACE', '{', 1, 21),
        ('KEYWORD', 'if', 2, 4),
        ('LPAREN', '(', 2, 7),
        ('IDENTIFIER', 'n', 2, 8),
        ('OPERATOR', '<=', 2, 10),
        ('INTEGER_LITERAL', '1', 2, 13),
        ('RPAREN', ')', 2, 14),
        ('LBRACE', '{', 2, 16),
        ('KEYWORD', 'return', 3, 8),
        ('INTEGER_LITERAL', '1', 3, 15),
        ('SEMICOLON', ';', 3, 16),
        ('RBRACE', '}', 4, 4),
        ('KEYWORD', 'return', 5, 4),
        ('IDENTIFIER', 'n', 5, 11),
        ('OPERATOR', '*', 5, 13),
        ('IDENTIFIER', 'factorial', 5, 15),
        ('LPAREN', '(', 5, 24),
        ('IDENTIFIER', 'n', 5, 25),
        ('OPERATOR', '-', 5, 27),
        ('INTEGER_LITERAL', '1', 5, 29),
        ('RPAREN', ')', 5, 30),
        ('SEMICOLON', ';', 5, 31),
        ('RBRACE', '}', 6, 0),
        ('EOF', '', 7, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n📚 Symbol Table:")
    for name, symbol in parser.symbol_table.symbols.items():
        print(f"   {symbol}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_if():
    """Test Case: If-Else Statement"""
    print("=" * 70)
    print("TEST CASE: If-Else Statement")
    print("Input:")
    print("   int x = 10;")
    print("   if (x > 5) {")
    print("       x = 20;")
    print("   } else {")
    print("       x = 0;")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'x', 1, 4),
        ('OPERATOR', '=', 1, 6),
        ('INTEGER_LITERAL', '10', 1, 8),
        ('SEMICOLON', ';', 1, 10),
        ('KEYWORD', 'if', 2, 0),
        ('LPAREN', '(', 2, 3),
        ('IDENTIFIER', 'x', 2, 4),
        ('OPERATOR', '>', 2, 6),
        ('INTEGER_LITERAL', '5', 2, 8),
        ('RPAREN', ')', 2, 9),
        ('LBRACE', '{', 2, 11),
        ('IDENTIFIER', 'x', 3, 4),
        ('OPERATOR', '=', 3, 6),
        ('INTEGER_LITERAL', '20', 3, 8),
        ('SEMICOLON', ';', 3, 10),
        ('RBRACE', '}', 4, 0),
        ('KEYWORD', 'else', 4, 2),
        ('LBRACE', '{', 4, 7),
        ('IDENTIFIER', 'x', 5, 4),
        ('OPERATOR', '=', 5, 6),
        ('INTEGER_LITERAL', '0', 5, 8),
        ('SEMICOLON', ';', 5, 9),
        ('RBRACE', '}', 6, 0),
        ('EOF', '', 7, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_while():
    """Test Case: While Loop"""
    print("=" * 70)
    print("TEST CASE: While Loop")
    print("Input:")
    print("   int i = 0;")
    print("   while (i < 10) {")
    print("       i = i + 1;")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'i', 1, 4),
        ('OPERATOR', '=', 1, 6),
        ('INTEGER_LITERAL', '0', 1, 8),
        ('SEMICOLON', ';', 1, 9),
        ('KEYWORD', 'while', 2, 0),
        ('LPAREN', '(', 2, 6),
        ('IDENTIFIER', 'i', 2, 7),
        ('OPERATOR', '<', 2, 9),
        ('INTEGER_LITERAL', '10', 2, 11),
        ('RPAREN', ')', 2, 13),
        ('LBRACE', '{', 2, 15),
        ('IDENTIFIER', 'i', 3, 4),
        ('OPERATOR', '=', 3, 6),
        ('IDENTIFIER', 'i', 3, 8),
        ('OPERATOR', '+', 3, 10),
        ('INTEGER_LITERAL', '1', 3, 12),
        ('SEMICOLON', ';', 3, 13),
        ('RBRACE', '}', 4, 0),
        ('EOF', '', 5, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_for():
    """Test Case: For Loop"""
    print("=" * 70)
    print("TEST CASE: For Loop")
    print("Input:")
    print("   int sum = 0;")
    print("   for (int i = 0; i < 5; i = i + 1) {")
    print("       sum = sum + i;")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'sum', 1, 4),
        ('OPERATOR', '=', 1, 8),
        ('INTEGER_LITERAL', '0', 1, 10),
        ('SEMICOLON', ';', 1, 11),
        ('KEYWORD', 'for', 2, 0),
        ('LPAREN', '(', 2, 4),
        ('KEYWORD', 'int', 2, 5),
        ('IDENTIFIER', 'i', 2, 9),
        ('OPERATOR', '=', 2, 11),
        ('INTEGER_LITERAL', '0', 2, 13),
        ('SEMICOLON', ';', 2, 14),
        ('IDENTIFIER', 'i', 2, 16),
        ('OPERATOR', '<', 2, 18),
        ('INTEGER_LITERAL', '5', 2, 20),
        ('SEMICOLON', ';', 2, 21),
        ('IDENTIFIER', 'i', 2, 23),
        ('OPERATOR', '=', 2, 25),
        ('IDENTIFIER', 'i', 2, 27),
        ('OPERATOR', '+', 2, 29),
        ('INTEGER_LITERAL', '1', 2, 31),
        ('RPAREN', ')', 2, 32),
        ('LBRACE', '{', 2, 34),
        ('IDENTIFIER', 'sum', 3, 4),
        ('OPERATOR', '=', 3, 8),
        ('IDENTIFIER', 'sum', 3, 10),
        ('OPERATOR', '+', 3, 14),
        ('IDENTIFIER', 'i', 3, 16),
        ('SEMICOLON', ';', 3, 17),
        ('RBRACE', '}', 4, 0),
        ('EOF', '', 5, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_break_continue():
    """Test Case: Break and Continue"""
    print("=" * 70)
    print("TEST CASE: Break and Continue")
    print("Input:")
    print("   int i = 0;")
    print("   while (i < 10) {")
    print("       if (i == 5) {")
    print("           break;")
    print("       }")
    print("       if (i == 3) {")
    print("           continue;")
    print("       }")
    print("       i = i + 1;")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'i', 1, 4),
        ('OPERATOR', '=', 1, 6),
        ('INTEGER_LITERAL', '0', 1, 8),
        ('SEMICOLON', ';', 1, 9),
        ('KEYWORD', 'while', 2, 0),
        ('LPAREN', '(', 2, 6),
        ('IDENTIFIER', 'i', 2, 7),
        ('OPERATOR', '<', 2, 9),
        ('INTEGER_LITERAL', '10', 2, 11),
        ('RPAREN', ')', 2, 13),
        ('LBRACE', '{', 2, 15),
        ('KEYWORD', 'if', 3, 4),
        ('LPAREN', '(', 3, 7),
        ('IDENTIFIER', 'i', 3, 8),
        ('OPERATOR', '==', 3, 10),
        ('INTEGER_LITERAL', '5', 3, 13),
        ('RPAREN', ')', 3, 14),
        ('LBRACE', '{', 3, 16),
        ('KEYWORD', 'break', 4, 8),
        ('SEMICOLON', ';', 4, 13),
        ('RBRACE', '}', 5, 4),
        ('KEYWORD', 'if', 6, 4),
        ('LPAREN', '(', 6, 7),
        ('IDENTIFIER', 'i', 6, 8),
        ('OPERATOR', '==', 6, 10),
        ('INTEGER_LITERAL', '3', 6, 13),
        ('RPAREN', ')', 6, 14),
        ('LBRACE', '{', 6, 16),
        ('KEYWORD', 'continue', 7, 8),
        ('SEMICOLON', ';', 7, 16),
        ('RBRACE', '}', 8, 4),
        ('IDENTIFIER', 'i', 9, 4),
        ('OPERATOR', '=', 9, 6),
        ('IDENTIFIER', 'i', 9, 8),
        ('OPERATOR', '+', 9, 10),
        ('INTEGER_LITERAL', '1', 9, 12),
        ('SEMICOLON', ';', 9, 13),
        ('RBRACE', '}', 10, 0),
        ('EOF', '', 11, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_nested():
    """Test Case: Nested Control Flow"""
    print("=" * 70)
    print("TEST CASE: Nested Control Flow")
    print("Input:")
    print("   for (int i = 0; i < 3; i = i + 1) {")
    print("       if (i == 1) {")
    print("           int x = 10;")
    print("       }")
    print("   }")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'for', 1, 0),
        ('LPAREN', '(', 1, 4),
        ('KEYWORD', 'int', 1, 5),
        ('IDENTIFIER', 'i', 1, 9),
        ('OPERATOR', '=', 1, 11),
        ('INTEGER_LITERAL', '0', 1, 13),
        ('SEMICOLON', ';', 1, 14),
        ('IDENTIFIER', 'i', 1, 16),
        ('OPERATOR', '<', 1, 18),
        ('INTEGER_LITERAL', '3', 1, 20),
        ('SEMICOLON', ';', 1, 21),
        ('IDENTIFIER', 'i', 1, 23),
        ('OPERATOR', '=', 1, 25),
        ('IDENTIFIER', 'i', 1, 27),
        ('OPERATOR', '+', 1, 29),
        ('INTEGER_LITERAL', '1', 1, 31),
        ('RPAREN', ')', 1, 32),
        ('LBRACE', '{', 1, 34),
        ('KEYWORD', 'if', 2, 4),
        ('LPAREN', '(', 2, 7),
        ('IDENTIFIER', 'i', 2, 8),
        ('OPERATOR', '==', 2, 10),
        ('INTEGER_LITERAL', '1', 2, 13),
        ('RPAREN', ')', 2, 14),
        ('LBRACE', '{', 2, 16),
        ('KEYWORD', 'int', 3, 8),
        ('IDENTIFIER', 'x', 3, 12),
        ('OPERATOR', '=', 3, 14),
        ('INTEGER_LITERAL', '10', 3, 16),
        ('SEMICOLON', ';', 3, 18),
        ('RBRACE', '}', 4, 4),
        ('RBRACE', '}', 5, 0),
        ('EOF', '', 6, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_compound_assignment():
    """Test Case: Compound Assignment Operators"""
    print("=" * 70)
    print("TEST CASE: Compound Assignment Operators")
    print("Input:")
    print("   int x = 10;")
    print("   x += 5;")
    print("   x -= 3;")
    print("   x *= 2;")
    print("   x /= 4;")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'int', 1, 0),
        ('IDENTIFIER', 'x', 1, 4),
        ('OPERATOR', '=', 1, 6),
        ('INTEGER_LITERAL', '10', 1, 8),
        ('SEMICOLON', ';', 1, 10),
        ('IDENTIFIER', 'x', 2, 0),
        ('OPERATOR', '+=', 2, 2),
        ('INTEGER_LITERAL', '5', 2, 5),
        ('SEMICOLON', ';', 2, 6),
        ('IDENTIFIER', 'x', 3, 0),
        ('OPERATOR', '-=', 3, 2),
        ('INTEGER_LITERAL', '3', 3, 5),
        ('SEMICOLON', ';', 3, 6),
        ('IDENTIFIER', 'x', 4, 0),
        ('OPERATOR', '*=', 4, 2),
        ('INTEGER_LITERAL', '2', 4, 5),
        ('SEMICOLON', ';', 4, 6),
        ('IDENTIFIER', 'x', 5, 0),
        ('OPERATOR', '/=', 5, 2),
        ('INTEGER_LITERAL', '4', 5, 5),
        ('SEMICOLON', ';', 5, 6),
        ('EOF', '', 6, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_string_literal():
    """Test Case: String Literals"""
    print("=" * 70)
    print("TEST CASE: String Literals")
    print("Input:")
    print('   string message = "Hello World";')
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'string', 1, 0),
        ('IDENTIFIER', 'message', 1, 7),
        ('OPERATOR', '=', 1, 15),
        ('STRING_LITERAL', '"Hello World"', 1, 17),
        ('SEMICOLON', ';', 1, 31),
        ('EOF', '', 2, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


def run_test_case_float_literal():
    """Test Case: Float Literals"""
    print("=" * 70)
    print("TEST CASE: Float Literals")
    print("Input:")
    print("   float pi = 3.14159;")
    print("   float result = pi * 2.0;")
    print("=" * 70)

    tokens = [
        ('KEYWORD', 'float', 1, 0),
        ('IDENTIFIER', 'pi', 1, 6),
        ('OPERATOR', '=', 1, 9),
        ('FLOAT_LITERAL', '3.14159', 1, 11),
        ('SEMICOLON', ';', 1, 18),
        ('KEYWORD', 'float', 2, 0),
        ('IDENTIFIER', 'result', 2, 6),
        ('OPERATOR', '=', 2, 13),
        ('IDENTIFIER', 'pi', 2, 15),
        ('OPERATOR', '*', 2, 18),
        ('FLOAT_LITERAL', '2.0', 2, 20),
        ('SEMICOLON', ';', 2, 23),
        ('EOF', '', 3, 0)
    ]

    print("\n📥 Tokens received from lexer:")
    for token in tokens[:-1]:
        print(f"   {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()

    print("\n🌳 Generated AST:")
    print(f"   {ast}")

    print("\n" + "=" * 70 + "\n")
    return ast


if __name__ == '__main__':

    banner()
    run_test_case_if()
    run_test_case_1()
    run_test_case_nested()
    run_test_case_2()
    run_test_case_while()
    run_test_case_float_literal()
    run_test_case_simple_function()
    run_test_case_break_continue()