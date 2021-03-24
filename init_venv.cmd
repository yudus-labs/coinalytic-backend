set PY_DIR=C:\python39

"%PY_DIR%/python" -m venv venv
"venv/Scripts/pip" install -e .[dev]
