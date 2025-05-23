from io import StringIO
import os
from sphinx.application import Sphinx
from sphinx.testing.path import path

def test_extension(make_app):
    app: Sphinx = make_app(
        srcdir=path(os.path.join(os.path.dirname(__file__), 'docs')),
                           )
    app.warningiserror = True
    app.build(force_all=True)
