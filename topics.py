__author__ = "Jeremy Nelson"

import js

from jinja2 import Template
from pyodide import create_proxy


intro_airflow_template = Template("""<div><h2>What is Airflow?</h2>
<img src="assets/airflow.png" alt="Airflow Logo" />
<p>
  <a href="https://airflow.apache.org/">Apache Airflow</a> is an open-source workflow 
  authoring, orchestration and management tool that allows for the construction of 
  complex workflows, called DAGs (short for directed acyclic graphs), that are made up 
  of one or more code-defined tasks.
</p>
<h3>Used widely in Data Science and Machine Learning Applications</h3>
<p>
  Companies and organizations in a wide range of industries use Apache Airflow
  for the following reasons:   
</p>
<ul>
  <li><strong>Ease of use</strong></li>
  <li><strong>Open Source</strong> with a strong developer and user communities.</li>
  <li><strong>Integrations</strong>
   Airflow has a rich ecosystem of plugins for integrating
   these tasks with a large number of technologies, both commercial cloud providers like
   Amazon and Google, along with popular open-source projects like Postgres, .., and ...
   <br>
   <img src="assets/aws.png" style="height: 75px" alt="AWS Logo"> 
  </li>
  <li><strong>Graphical/Web-based User Interface</strong></li>
  <li><strong>REST API</strong></li>
</ul>
<h3>Example DAG with Tasks</h3>
<pre>



</pre>
</div>""")

def intro2airflow(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Introduction to Airflow"
  
    main.innerHTML = intro_airflow_template.render()
    


sinopia_stack_template = Template("""<div>
<h2>Sinopia Linked-Data Editor</h2>
<p>
  <a href="https://sinopia.io/">Sinopia</a>, a project of the <a href="http://www.ld4p.org/">Linked-Data for Production (LD4)</a>, 
  was initially funded by multiple Andrew W. Mellon Foundation grants. 
</p>

<h3>Sinopia's ILS Middleware</h3>
<p>

</p>
</div>""")

def sinopia_stack(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Sinopia Editor Stack"
 
    main.innerHTML = sinopia_stack_template.render()


marc_migration_template = Template("""<div><h2>MARC Records Migration to FOLIO</h2>
<p>
  Stanford's migration of bibliographic data from our legacy ILS to FOLIO Library Services Platform,
  is built with multiple open-source technologies. Our workflow DAGs and plugins are also licensed under
  the Apache2 license and are available from <a href="https://github.com/sul-dlss/libsys-airflow/">LibSys Airflow</a>
  repository.
</p>
<h3>FOLIO-FSE Migration Tools</h3>
<p>
  Stanford's DAGs use the open-source tools  <a href="https://github.com/FOLIO-FSE/folio_migration_tools/">FOLIO Migration Tools</a> 
  and <a href="https://github.com/FOLIO-FSE/FolioClient">FolioClient</a> developed by Ebsco's FOLIO-FSE team for the majority of 
  the core migration from MARC21 binary and tab-separated files (TSV) to FOLIO Instances, Holdings, and Items records. 
</p>
<h2>Directed Acyclic Graph Workflows</h2>
<h3><em>symphony_marc_import</em> DAG</h3>
<p>
  The primary 
</p>
<h3><em>ingest_marc_to_srs</em> DAG</h3>
<h3><em>fix_failed_record_loads</em>DAG</h3>
<h2>Recent Functionality</h2>

<h3>Boundwidths, Proceeding/Succeeding Titles</h3>

<h3>MHLD</h3>


</div>""")

def marc_migration(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- MARC BIB Record Migration"
 
    main.innerHTML = marc_migration_template.render()

future_workflows_template = Template("""<div><h2>Future Workflows</h2>
<h3>Circulation Migration: Loans and Requests</h3> 
<p>

</p>
<h3>Migrating Bills</h3>
<h3>Ongoing MARC Record and User Loads</h3>
<h3>Authority Records</h3>
<h3>Further Sinopia Integration</h3>
</div>""")

def future_workflows(event):
    main = js.document.getElementById('content')
    subtitle = js.document.getElementById('subtitle')
    subtitle.innerHTML = "-- Future Workflows"
 
    main.innerHTML = future_workflows_template.render()
