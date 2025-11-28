from .basic import register_views as register_views_basic
from .openapi import register_views as register_views_openapi
from .task import register_views as register_views_task


def register_views(app, api):
    register_views_basic(app)
    register_views_openapi(app, api)
    register_views_task(api)
