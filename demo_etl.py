import logging

from datetime import datetime

from airflow.decorators import dag, task

logger = logging.getLogger(__name__)

class MockDatabase(object):

    def load(self, records):
        logger.info(f"Mocks loading {records} into a database")

@dag(
    schedule_interval=None,
    start_date=datetime(2022, 9, 1),
    catchup=False,
    tags=['example'],
)
def etl():

  @task
  def extract(*args, **kwargs):
      logger.info("Extract data from target")
      return [{"id": 23455, "title": "A Fine Extraction"}]

  @task
  def transform(*args, **kwargs):
      input = kwargs['records']
      output = []
      for record in input:
          record['title'] = f"{record['title']}, now transformed"
          logger.info(f"Record is {record}")
          output.append(record)
      logger.info(f"Finished transforming {len(input)}")
      return output

  @task
  def load(*args, **kwargs):
      transformed_records = kwargs['records']
      database = kwargs['db']
      database.load(transformed_records)


  records = extract()
  transformed_records = transform(records=records) 
  load(db=MockDatabase(), records=transformed_records)

test_etl = etl()
