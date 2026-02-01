from project import fix_space, calc_complexity, clean_tag_list


def test_fix_space():
    assert fix_space(None) == ""
    assert fix_space("") == ""
    assert fix_space("  ") == ""
    assert fix_space(" a b c ") == "a b c"
    assert fix_space("a  b  c") == "a b c"
    assert fix_space("ab .") == "ab."
    assert fix_space("ab.cd") == "ab. cd"
    assert fix_space(" ab     ,cd! ") == "ab, cd!"
    assert fix_space("ab .ab ,12 :12 ;a1 ?1a !ab") == "ab. ab, 12: 12; a1? 1a! ab"
    assert fix_space("ab !!cd") == "ab!! cd"
    assert fix_space("'ab' 'cd'") == "'ab' 'cd'"
    assert fix_space('"ab" "cd"') == '"ab" "cd"'


def test_calc_complexity():
    assert calc_complexity(None) == 0
    assert calc_complexity("") == 0
    assert calc_complexity("  ") == 0
    assert calc_complexity("12 1a 1a2 a1 ! !12") == 0
    assert calc_complexity("a 1a a") == 2
    assert calc_complexity(" a 1a a ") == 2
    assert calc_complexity(" abc 1a ab ") == 5
    assert calc_complexity("ab ab ab") == 6
    assert calc_complexity("ab! a'b' ab") == 6
    assert calc_complexity('ab! ab. a\'b "ab"') == 8


def test_clean_tag_list():
    assert clean_tag_list(None) == ""
    assert clean_tag_list(["  ", None]) == ""
    assert clean_tag_list([" AA ", "bB ", " cc"]) == "aa-bb-cc"
    assert clean_tag_list([" aa ", "bb ", " cc"]) == "aa-bb-cc"
    assert clean_tag_list([" aa ", " ", " cc"]) == "aa-cc"
    assert clean_tag_list([" aa ", "BB", "aA", " bB"]) == "aa-bb"
    assert clean_tag_list([" aa ", "zz ", " aa", "BB", "aA", " bB"]) == "aa-bb-zz"
