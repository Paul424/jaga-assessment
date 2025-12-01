from .authlib import register_auth as register_auth_authlib


def register_auth(app):
    register_auth_authlib(app)
