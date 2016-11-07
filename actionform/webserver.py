from jinja2 import Template
from flask import request, Flask

DEFAULT_TEMPLATE = """
<html>
<body>
<h1>Hoi!</h1>
<form method="POST" action="/">
    {{ form.test.label }} {{ form.test(size=20) }}
    <input type="submit" value="Go">
</form>
{% if result %}
<hr/>
<pre>{{ result }}</pre>
{% endif %}
</body>
</html>"""

def run_server(action, template=DEFAULT_TEMPLATE, **kargs):

    if isinstance(template, str):
        template = Template(template)
    
    app = Flask(action.__name__)
    @app.route('/', methods=['GET'])
    def get():
        form = action.get_form_class()()
        return template.render(**locals())

    @app.route('/', methods=['POST'])
    def post():
        form = action.get_form_class()(request.form)
        result = action(form).run()
        return template.render(**locals())

    app.run(**kargs)
