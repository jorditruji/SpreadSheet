from . import ExcelParser


class TokenExpression(ExcelParser):
    def __init__(self, expression):
        """
        Initializes a token expression class
        Args:
            expression (str): String expression to be handled

        """
        super().__init__()
        self.string_expression = expression
        # TODO: Mirar que fem amb el parser, Agafa ',' en ves de ';'. Hauriem de canviar codi de jsport_nonEAT
        self.parse(formula=expression)

    def get_tokens(self):
        """
        Get tokens from expression as list of dicts
        Returns:
            list: list of token dicts
        """
        items = self.tokens.items
        tokens = [item.__dict__ for item in items]
        return tokens
