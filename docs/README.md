# TestProject Documentation

The source for TestProject documentation is in this directory under `sources/`.
Our documentation uses extended Markdown, as implemented by [MkDocs](http://mkdocs.org).

## Building the documentation

- install MkDocs: `pip install mkdocs` 
- `pip install -e .` to make sure that Python will import your modified version of TestProject.
- `cd` to the `docs/` folder and run:
    - `python autogen.py`
    - `mkdocs build`    # Builds a static site in "site" directory
    - `mkdocs serve`    # Starts a local webserver:  [localhost:8000](http://127.0.0.1:8000)
    

Documentation produced based on [Keras project.](https://github.com/keras-team/keras/blob/master/keras) 

For creating docstrings is useful to read the [following documentation.](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)