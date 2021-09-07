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
    rw = int(os.getenv('multiple_survey_render_weight')) if os.getenv('multiple_survey_render_weight') else 1
    sw1 = int(os.getenv('mutiple_survey1_submit_weight')) if os.getenv('mutiple_survey1_submit_weight') else 1
    sw2 = int(os.getenv('mutiple_survey2_submit_weight')) if os.getenv('mutiple_survey2_submit_weight') else 1
    sw3 = int(os.getenv('mutiple_survey3_submit_weight')) if os.getenv('mutiple_survey3_submit_weight') else 1
    sw4 = int(os.getenv('mutiple_survey4_submit_weight')) if os.getenv('mutiple_survey4_submit_weight') else 1
    
    params = {
        'random_int': 5,
        'random_string': 'abcdef',
        'random_name': 'Jeff',
        'submit-action': 'submit-btn-saverecord'
    }

    def submit(self, uri, name):
        with self.client.post(uri, self.params, catch_response=True, name=name) as response: 
            if response.status_code == 200:
                response.success()
            else:
                response.failure()

    @task(sw1)
    def submit_public_survey1(self):
        print("submitting multiple survey ... ")
        self.submit(os.getenv('multiple_public_survey_url1'), 'Multiple Survey 1 submission')
    
    @task(sw2)
    def submit_public_survey2(self):
        print("submitting multiple survey 2 ... ")
        self.submit(os.getenv('multiple_public_survey_url2'), 'Multiple Survey 2 submission')

    
    @task(sw3)
    def submit_public_survey3(self):
        print("submitting multiple survey 3 ... ")
        self.submit(os.getenv('multiple_public_survey_url3'), 'Multiple Survey 3 submission')


    @task(sw4)
    def submit_public_survey4(self):
        print("submitting multiple survey 4 ... ")
        self.submit(os.getenv('multiple_public_survey_url4'), 'Multiple Survey 4 submission')

    @task(rw) # render 5 times as often
    def render_public_survey(self):
        choices = [
            os.getenv('multiple_public_survey_url1'),
            os.getenv('multiple_public_survey_url2'),
            os.getenv('multiple_public_survey_url3'),
            os.getenv('multiple_public_survey_url4')
        ]
        
        choice = random.randint(0,3)
        
        print(f"rendering multiple survey ... {choice + 1}")
        
        self.client.get(choices[choice], name='Multiple survey render')

    wait_time = between(1, 3)