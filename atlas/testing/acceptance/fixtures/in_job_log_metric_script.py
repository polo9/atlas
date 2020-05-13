
import os

import foundations
from foundations_contrib.global_state import current_foundations_context, message_router
from foundations_events.producers.jobs import RunJob

foundations.set_project_name('default')

job_id = os.environ['ACCEPTANCE_TEST_JOB_ID']
current_foundations_context().job_id = job_id

RunJob(message_router, current_foundations_context()).push_message()

foundations.log_metric('key', 'value')
print('Hello World!')