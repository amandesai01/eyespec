from lib.tokens import Token, Token0, SpecialTokenDivision


def group_by_division(parse_tree: list[Token]) -> list[SpecialTokenDivision]:
    print("Grouping by divisions...")
    current_division = None
    divisions: list[SpecialTokenDivision] = []
    for token in parse_tree:
        if token.get_token_type() == 0:
            token: Token0 = token
            if current_division is None or current_division.sr_no != token.d1:
                current_division = SpecialTokenDivision(sr_no=token.d1)
                divisions.append(current_division)
            current_division.children.append(token)
    return divisions
