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

def _render_template(subtitle, template):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = subtitle
    main.innerHTML = template.render()


def intro2airflow(event):
    _render_template("-- Introduction to Airflow", intro_airflow_template)

def sinopia_stack(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Sinopia Editor Stack"
 
    main.innerHTML = sinopia_stack_template.render()

def marc_migration(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- MARC BIB Record Migration"
 
    main.innerHTML = marc_migration_template.render()


def future_workflows(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Future Workflows"
 
    main.innerHTML = future_workflows_template.render()
