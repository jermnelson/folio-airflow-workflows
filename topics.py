__author__ = "Jeremy Nelson"

import js

from jinja2 import Template
from pyodide import create_proxy


intro_airflow_template = Template("""<div><h2>What is Airflow?</h2>
<p>
  <a href="https://airflow.apache.org/">Apache Airflow</a> is an open-source workflow 
  authoring, orchestration and management tool that ... 
</p>
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

discovery_integration_template = Template("""<div><h2>Stanford's Searchworks</h2>
<p>
 A critical and high-profile discovery service of Stanford University Libraries, 
 <a href="https://searchworks.stanford.edu/">SearchWorks</a> is a Blacklight-based 
 discovery system. 
</p>
</div>""")

def discovery_integration(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Discovery Integration"
 
    main.innerHTML = discovery_integration_template.render()
