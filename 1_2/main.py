class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token <{self.value}, {self.type}>"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    keywords = {'if', 'else', 'print', 'while', 'elif', 'for'}

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def collect_number(self):
        num_str = ''
        is_negative = False

        if self.current_char == '-':
            is_negative = True
            num_str += self.current_char
            self.advance()

        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()

        token_type = 'negative number' if is_negative else 'number'
        return Token(token_type, int(num_str))

    def collect_identifier_or_keyword(self):
        id_str = ''
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char == '_'):
            id_str += self.current_char
            self.advance()

        if id_str in self.keywords:
            return Token('keyword', id_str)
        else:
            return Token('identifier', id_str)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue


            if self.current_char.isdigit():
                return self.collect_number()

            if self.current_char == '-' and (
                self.pos == 0 or
                self.text[self.pos - 1] in ' (' or
                self.text[self.pos - 1] == '='
            ):

                return self.collect_number()

            if self.current_char.isalpha() or self.current_char == '_':
                return self.collect_identifier_or_keyword()


            if self.current_char == '+':
                self.advance()
                return Token('sum', '+')

            if self.current_char == '-':
                self.advance()
                return Token('subtract', '-')

            if self.current_char == '*':
                self.advance()
                return Token('multiply', '*')

            if self.current_char == '/':
                self.advance()
                return Token('divide', '/')

            if self.current_char == '=':
                self.advance()
                return Token('equal', '=')

            if self.current_char == '(':
                self.advance()
                return Token('open', '(')

            if self.current_char == ')':
                self.advance()
                return Token('close', ')')


            print(f"Warning: Unknown character '{self.current_char}' skipped.")
            self.advance()

        return Token('final', None)



sentences = [
    "x=-5+3*(y-2)/4",
    "if x=0 print(x)",
    "y=10+(x/2)",
    "while(t=-9)",
    "if (a=8) b=r-6 else color=red"
]


for text in sentences:
    lexer = Lexer(text)
    tokens = []
    while True:
        token = lexer.get_next_token()
        tokens.append(token)
        if token.type == 'final':
            break


    print("\nInput:")
    print(text)

    print("\nTokens:")
    print("[")
    for token in tokens[:-1]:
        print(token, ",")
    print(tokens[-1], "]\n*********")