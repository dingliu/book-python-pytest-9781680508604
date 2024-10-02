from sums import main


def test_sums_main(capsys):
    main()
    output = capsys.readouterr().out
    assert output.strip() == "200.00"
