from locust import HttpUser, task, events, between
from dotenv import load_dotenv
import os

load_dotenv() # load env variables

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

class SingleSurveyUser(HttpUser):
    sw = int(os.getenv('single_survey_submit_weight')) if os.getenv('single_survey_submit_weight') else 1
    rw = int(os.getenv('single_survey_render_weight')) if os.getenv('single_survey_render_weight') else 1

    @task(sw)
    def submit_public_survey(self):
        print("submitting single survey ... ")
        params = {
            'random_int': 5,
            'random_string': 'abcdef',
            'random_name': 'Jeff',
            'submit-action': 'submit-btn-saverecord'
        }
        
        with self.client.post(os.getenv('single_public_survey_url'), params, catch_response=True, name='Single survey submission') as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure()


    @task(rw) # render 3 times as often
    def render_public_survey(self):
        print("rendering single survey ... ")
        
        self.client.get(os.getenv('single_public_survey_url'), name='Single survey render')
            

    wait_time = between(1, 3)