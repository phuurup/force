import os
import json
from slash_slack import SlashSlack, String
from simple_salesforce import Salesforce
from collections import OrderedDict

sf = Salesforce(username='philip.pol@bench.co',
                password='',
                security_token='')

slash = SlashSlack(
    dev=True
    #signing_secret=os.environ["SLACK_SIGNING_SECRET"],
    #description="An example Slack slash command server.",
)
app = slash.get_fast_api()

@slash.command(
    "client",
    summary="get client info based on Bench Id",
    help="grabs salesforce client id based on the Bench Id you enter",
)
def client(benchId: str = String(help="The Bench Id to search")):
    try:
        data = getAccountInfo(benchId)
        return data, None
    except Exception as e:
        return f"An error occurred: {str(e)}"

def getAccountInfo(benchId: str):
    try:
        data = sf.query("select benchid__c, id, filing_type__c, tq_Corporate_Structure__c from Account where benchid__c = '" + benchId + "'")
        records = data.get('records', [{}])[0]  # Get the first record
        # Extract the values
        bench_id = records.get('BenchId__c')
        id_ = records.get('Id')
        filing_type = records.get('Filing_Type__c')
        corporate_structure = records.get('tq_Corporate_Structure__c')
        # Format the result
        result = f"BenchId__c: {bench_id}, Id: {id_}, Filing_Type__c: {filing_type}, tq_Corporate_Structure__c: {corporate_structure}"
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
    
  