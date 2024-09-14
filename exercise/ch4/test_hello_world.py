from hello_world import hello


def test_hello_without_fixture():
    hello()
    with open("hello.txt", "r") as f:
        content = f.read()
    assert content == "Hello World!\n"


def test_hello_with_fixture(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(tmp_path)
    hello()
    with open("hello.txt", "r") as f:
        content = f.read()
    with capsys.disabled():
        print(str(tmp_path))
    assert content == "Hello World!\n"
