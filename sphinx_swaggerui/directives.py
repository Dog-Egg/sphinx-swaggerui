import json
import posixpath
import uuid
from urllib.parse import quote
from sphinx.util.docutils import SphinxDirective
import yaml
import docutils.nodes

class SwaggerUI(SphinxDirective):
    has_content = True

    def run(self):
        content = yaml.safe_load('\n'.join(self.content))

        if self.config.process_swaggerui_config is not None:
            swaggerui_config = self.config.process_swaggerui_config(self.env.app, content)
        else:
            swaggerui_config = content  # pragma: no cover

        iframe_id = "id_" + uuid.uuid4().hex
        iframe = f"""
        <div style="border: 1px solid #eeebee;">
            <iframe src="{posixpath.join(self.config.html_baseurl or "/", "swagger-ui.html?config=" + quote(json.dumps(swaggerui_config)))}" id={iframe_id} loading="lazy" frameborder="0" style="min-width: 100%; display: block;"></iframe>
            <script>
                window.onload = function() {{
                    iFrameResize({{checkOrigin: false}}, '#{iframe_id}')
                }}
            </script>
        </div>
        """
        return [docutils.nodes.raw(text=iframe, format="html")]