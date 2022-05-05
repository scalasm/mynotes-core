Usage
=====

After installing the package, you can run everything standalone.

Note that this package is designed to be run into a container!

.. code:: console

   $ poetry run mynotes-core
   $ MYNOTES_DEV_MODE=true poetry run mynotes-core
   $ MYNOTES_HTTP_PORT=9080 MYNOTES_DEV_MODE=true poetry run mynotes-core
