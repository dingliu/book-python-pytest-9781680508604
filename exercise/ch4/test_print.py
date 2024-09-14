def test_normal():
    print("\nnormal print.")


def test_fail():
    print("\nnormal print.")
    assert False


def test_capsys_disabled(capsys):
    with capsys.disabled():
        print("\nprint with capsys.disabled()")
