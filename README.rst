Sigils-FastAPI
==============

Sigils is a Python library for interpolating strings with data.
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.

This package provides several example servers using FastAPI and Sigils together.


Installation
------------

Install and update from PyPI:

.. code-block:: text

    pip install -U sigils-fastapi


Redirect Server
---------------

Start the server in redirect mode:
(uvicorn must be installed already)

.. code-block:: text

    uvicorn sigils_fastapi.redirect:app --reload

