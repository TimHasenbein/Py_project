import project as p
import pytest


def main():
    test_check_sequence()
    test_characterize()
    test_complement()
    test_translation()
    test_motif_search()


def test_check_sequence():
    assert p.check_sequence("ACTG") == "ACTG"
    with pytest.raises(SystemExit):
        p.check_sequence("ACTF")


def test_characterize():
    length, GC_content, molecular_weight = p.characterize('ACTG')
    assert length == 4
    assert GC_content == 0.5
    assert molecular_weight == 523.47


def test_complement():
    assert p.complement("ACTG") == "TGAC"
    assert p.complement("ATGC") == "TACG"
    assert p.complement("AATC") == "TTAG"


def test_translation():
    assert p.translation("ATGAATATGTCGAAA") == "MNMSK"
    assert p.translation("GGGATGAATATGTCGAAA") == "MNMSK"
    assert p.translation("AATATCTCGAAA") == ''


def test_motif_search():
    assert p.motif_search("ATGAATATGTCGAAA","ATG") == [0,6]
    assert p.motif_search("ATGAATATGTCGAAA","ATGATT") == []


if __name__ == "__main__":
    main()


