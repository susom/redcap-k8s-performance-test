from locus_scripts.SingleSurvey import SingleSurveyUser
from locus_scripts.MutlipleSurveys import MutlipleSurveyUser
from dotenv import load_dotenv
import os

load_dotenv() # load env variables

SingleSurveyUser.weight = int(os.getenv('single_survey_weight')) if os.getenv('single_survey_weight') else 1
MutlipleSurveyUser.weight = int(os.getenv('multiple_survey_weight')) if os.getenv('multiple_survey_weight') else 1
