from actionform import ActionForm
from wtforms import form, fields

from nose.tools import assert_equal

class TestAction(ActionForm):
    class form_class(form.Form):
        test = fields.StringField()

    def _run(self, test):
        return test.upper()


def test_action():
    result = TestAction(test="test").run()
    assert_equal(result, "TEST")
