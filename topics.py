__author__ = "Jeremy Nelson"

import js

from jinja2 import Template
from pyodide import create_proxy

with open("intro-airflow.html") as fo:
    intro_airflow_template = Template(fo.read())

with open("marc-migration.html") as fo:
    marc_migration_template = Template(fo.read())

with open("sinopia-stack.html") as fo:
    sinopia_stack_template = Template(fo.read())

with open("future-workflows.html") as fo:
    future_workflows_template = Template(fo.read())

def _render_template(subtitle_text, template):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = subtitle_text
    main.innerHTML = template.render()


def intro2airflow(event):
    _render_template("-- Introduction to Airflow", intro_airflow_template)

def sinopia_stack(event):
    _render_template("-- Sinopia Editor Stack", sinopia_stack_template)

def marc_migration(event):
    _render_template("-- MARC BIB Record Migration", marc_migration_template)


def future_workflows(event):
    _render_template("-- Future Workflows", future_workflows_template)
