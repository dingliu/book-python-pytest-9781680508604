from subprocess import run


def test_sums_sub_process():
    result = run(["python", "sums.py"], capture_output=True, text=True)
    output = result.stdout.strip()
    assert output == "200.00"
