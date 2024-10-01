# Setting up a monorepo with bazel

- there is a command to compile `pyproject.toml` https://rules-python.readthedocs.io/en/latest/api/rules_python/python/pip.html#compile_pip_requirements.visibility


## How a build process works

The build command is responsible to write the output files to a specific directory. For a given file this directory can
be passed as `$(execpath <out-file>)`.

```bazel
run_binary(
    name="package",
    tool="main",
    args=["$(execpath foo_project-0.1.0.tar.gz)"],
    srcs = glob(["src/**/*.py"]) + [":pyproject.toml"],
    outs = [
        "foo_project-0.1.0-py3-none-any.whl",
        "foo_project-0.1.0.tar.gz"
    ],
)
```
