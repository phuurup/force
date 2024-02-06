import os
import json
from slash_slack import SlashSlack, String, Flag, Enum
from simple_salesforce import Salesforce
from collections import OrderedDict


#environment variables need to be set in your .zshrc or .bashrc file.
sf = Salesforce(username=os.environ["SF_UNAME"],
                password=os.environ["SF_PW"],
               security_token=os.environ["SF_SECURITY_TOKEN"])



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

# /client 23487 tax --update
def client(benchId: str = String(help="The Bench Id to search"), team: str = Enum(values={"tax", "bpa", "onboarding"}), update: str = Flag(), create: str = Flag()):
    if team == "tax":
        if update:
            return updateTax
        if create:
            return createTax
    else: 
        return queryTax
    if team == "bpa":
        if update:
            return updateBpa
        if create:
            return createBpa
    else:
        return queryBpa
    if team == "onboarding":
        if update:
            return updateOnboarding
        if create:
            return createOnboarding
    else:
        return queryOnboarding
    if team != "defult":
        try:
            data = getGeneralAccountInfo(benchId)
            return data, None
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Below are all the classes we'll need to complete.
def getGeneralAccountInfo(benchId: str):
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

def updateTax(benchId: str):
    return null

def createTax(benchId: str):
    return null

def queryTax(benchId: str):
    return null

def updateBpa(benchId: str):
    return null

def createBpa(benchId: str):
    return null

def queryBpa(benchId: str):
    return null

def updateOnboarding(benchId: str):
    return null

def createOnboarding(benchId: str):
    return null

def queryOnboarding(benchId: str):
    return null