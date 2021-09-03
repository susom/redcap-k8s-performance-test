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
    @task(1)
    def submit_public_survey(self):
        print("submitting public survey ... ")
        params = {
            'random_int': 5,
            'random_string': 'abcdef',
            'random_name': 'Jeff',
            'submit-action': 'submit-btn-saverecord'
        }
        with self.client.post(os.getenv('single_public_survey_url'), params, catch_response=True) as response:
            if response.is_redirect:
                print('is redirect')
        

    @task(3) # render 3 times as often
    def render_public_survey(self):
        print("rendering survey ... ")
        self.client.get(os.getenv('single_public_survey_url'))

    wait_time = between(1, 3)