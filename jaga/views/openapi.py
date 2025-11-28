import yaml


# View to expose OpenAPI spec document
def openapi(app, api):
    spec = api.spec.to_dict()
    return app.response_class(
        yaml.dump(spec, default_flow_style=False), mimetype="application/x-yaml"
    )


def register_views(app, api):
    app.add_url_rule("/openapi.yaml", view_func=lambda: openapi(app, api))
