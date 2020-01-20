from hello_ci import HelloCI


def test_helloci():
    assert len(HelloCI().name) > 0
    assert not HelloCI().greet()
