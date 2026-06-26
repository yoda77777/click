import click


def test_clickexception_show_includes_notes(capsys):
    """ClickException.show() displays exception notes (PEP 678).

    Regression for https://github.com/pallets/click/issues/2740
    """
    exc = click.ClickException("foo")
    exc.add_note("bar")
    exc.add_note("baz")
    exc.show()
    err = capsys.readouterr().err
    assert "Error: foo" in err
    assert "bar" in err
    assert "baz" in err


def test_clickexception_show_without_notes(capsys):
    exc = click.ClickException("only message")
    exc.show()
    err = capsys.readouterr().err
    assert err.strip() == "Error: only message"
