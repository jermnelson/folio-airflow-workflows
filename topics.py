__author__ = "Jeremy Nelson"

import js

from jinja2 import Template
from pyodide import create_proxy


intro_airflow_template = Template("""<div><h2>What is Airflow?</h2>
<h3>Used widely in Data Science and Machine Learning Applications</h3>
<p>
  
</p>
<p>
  <a href="https://airflow.apache.org/">Apache Airflow</a> is an open-source workflow 
  authoring, orchestration and management tool that allows for the construction of 
  complex workflows, called DAGs (short for directed acyclic graphs), that are made up 
  of one or more code-defined tasks. Airflow has a rich ecosystem of plugins for integrating
  these tasks with a large number of technologies, both commercial cloud providers like
  Amazon and Google, along with popular open-source projects like Postgres, .., and ...
</p>
<
<pre>


</pre>
</div>""")

def intro2airflow(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Introduction to Airflow"
  
    main.innerHTML = intro_airflow_template.render()
    


sinopia_stack_template = Template("""<div><h2>Sinopia Linked-Data Editor</h2>
<p>
  Sinopia, a project of the Linked-Data for Production (LD4), a Mellon funded grant.
</p>
</div>""")

def sinopia_stack(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Sinopia Editor Stack"
 
    main.innerHTML = sinopia_stack_template.render()


marc_migration_template = Template("""<div><h2>MARC BIB Records Migration</h2>

</div>""")

def marc_migration(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- MARC BIB Record Migration"
 
    main.innerHTML = marc_migration_template.render()

future_workflows_template = Template("""<div><h2>Future Workflows</h2>
<p>

</p>
</div>""")

def future_workflows(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Future Workflows"
 
    main.innerHTML = future_workflows_template.render()
