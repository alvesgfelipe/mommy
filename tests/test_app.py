from flask import Flask


def test_app_foi_criado_corretamente(app: Flask):
    assert app.name == "mommy.app"


def test_app_debug_esta_false(config):
    assert config["DEBUG"] is False


def test_app_testing_esta_true(config):
    assert config["TESTING"] is True
