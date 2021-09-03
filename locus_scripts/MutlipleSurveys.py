from locust import HttpUser, task, events, between
from dotenv import load_dotenv
import os, random

load_dotenv() # load env variables

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

class MutlipleSurveyUser(HttpUser):
    params = {
        'random_int': 5,
        'random_string': 'abcdef',
        'random_name': 'Jeff',
        'submit-action': 'submit-btn-saverecord'
    }

    @task(1)
    def submit_public_survey1(self):
        print("submitting public survey ... ")
        self.client.post(os.getenv('multiple_public_survey_url1'), self.params, catch_response=True)
    
    @task(1)
    def submit_public_survey2(self):
        print("submitting public survey 2 ... ")
        self.client.post(os.getenv('multiple_public_survey_url2'), self.params, catch_response=True)            
    
    @task(1)
    def submit_public_survey3(self):
        print("submitting public survey 3 ... ")
        self.client.post(os.getenv('multiple_public_survey_url3'), self.params, catch_response=True)

    @task(1)
    def submit_public_survey4(self):
        print("submitting public survey 4 ... ")
        self.client.post(os.getenv('multiple_public_survey_url4'), self.params, catch_response=True)

    @task(5) # render 3 times as often
    def render_public_survey(self):
        choices = [
            os.getenv('multiple_public_survey_url1'),
            os.getenv('multiple_public_survey_url2'),
            os.getenv('multiple_public_survey_url3'),
            os.getenv('multiple_public_survey_url4')
        ]
        
        choice = random.choices(choices)
        
        print(f"rendering survey ... ${choice}")
        
        self.client.get(random.choice(choices))

    wait_time = between(1, 3)