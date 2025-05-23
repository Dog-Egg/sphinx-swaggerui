Sphinx-SwaggerUI
================

Usage
-----

.. code-block::
    :caption: conf.py

    extensions = [
        ...
        "sphinx_swaggerui"
    ]

.. code-block::
    :caption: index.rst

    .. swaggerui::
        
        url: https://petstore.swagger.io/v2/swagger.json

.. swaggerui::

    url: https://petstore.swagger.io/v2/swagger.json


You can modify the configuration content of the ``swaggerui`` directive by configuring the ``process_swaggerui_config`` method.

.. code-block::
    :caption: conf.py

    def process_swaggerui_config(app, config):
        return {
            **config,
            "docExpansion": "full"
        }