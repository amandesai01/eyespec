from lib.tokens import Token, Token0, Token6
from lib.lex import get_total_index_levels, identify_level

TOTAL_INDEX_LEVELS = get_total_index_levels()


def create_parse_tree(tokens: list[Token]) -> list[Token]:
    final_parse_tree: list[Token] = []
    hierarchy_adjust_register: list = [None for _ in range(TOTAL_INDEX_LEVELS)]
    for token in tokens:
        __parse_treeify(token, final_parse_tree, hierarchy_adjust_register)
    __post_process_tree(final_parse_tree)
    return final_parse_tree


def __parse_treeify(token: Token, current_parse_tree: list[Token], hierarchy_adjust_register: list[Token]) -> None:
    current_token_level = identify_level(token)
    for i in range(current_token_level + 1, TOTAL_INDEX_LEVELS):
        hierarchy_adjust_register[i] = None
    hierarchy_adjust_register[current_token_level] = token
    for i in range(current_token_level - 1, -1, -1):
        if hierarchy_adjust_register[i]:
            hierarchy_adjust_register[i].children.append(token)
            return
    current_parse_tree.append(token)


def __post_process_tree(parse_tree: list[Token]) -> None:
    for token in parse_tree:
        if token.get_token_type() == 0:
            token: Token0 = token
            if not token.title:
                if len(token.children) > 0:
                    first_child = token.children[0]
                    if first_child.get_token_type() == 6:
                        first_child: Token6 = first_child
                        token.title = first_child.data
