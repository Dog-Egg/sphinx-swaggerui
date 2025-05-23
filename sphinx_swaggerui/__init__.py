import os
from pathlib import Path
import shutil

from sphinx.application import Sphinx

from .directives import SwaggerUI

__version__ = "0.1"


def setup(app: Sphinx):
    app.add_directive("swaggerui", SwaggerUI)
    app.add_config_value('process_swaggerui_config', None, rebuild=True)

    static_path = Path(__file__).parent / "static"
    app.config.html_static_path.append(static_path.as_posix())
    app.add_js_file("iframeResizer.min.js")

    def on_build_finished(app, exception):
        shutil.copy(
            os.path.join(os.path.dirname(__file__), "swagger-ui.html"),
            os.path.join(app.outdir, "swagger-ui.html"),
        )

    app.connect('build-finished', on_build_finished)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }