Sphinx-SwaggerUI
================

This extension is used to embed `SwaggerUI <https://github.com/swagger-api/swagger-ui>`_ into Sphinx documentations in the form of an iframe.

Installation
------------

.. code-block::

    pip install git+https://github.com/Dog-Egg/sphinx-swaggerui.git

Usage
-----

.. code-block::
    :caption: conf.py

    extensions = [
        ...
        "sphinx_swaggerui"
    ]

Directives
----------

.. _directives.swaggerui:

``.. swaggerui::``
~~~~~~~~~~~~~~~~~~

The directive requires YAML-formatted content to provide configuration for SwaggerUI.

.. note::

    You can find the configuration options for SwaggerUI `here <https://github.com/swagger-api/swagger-ui/blob/HEAD/docs/usage/configuration.md>`_.

For example:

.. code-block::
    :caption: index.rst

    .. swaggerui::
        
        url: https://petstore.swagger.io/v2/swagger.json

This directive will generate the following content.

.. swaggerui::

    url: https://petstore.swagger.io/v2/swagger.json

Configurations
--------------

You can modify the configuration content of the :ref:`swaggerui <directives.swaggerui>` directive by configuring the ``process_swaggerui_config`` method.

.. code-block::
    :caption: conf.py

    def process_swaggerui_config(app, config):
        return {
            **config,
            "docExpansion": "full"
        }