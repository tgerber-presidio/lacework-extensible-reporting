import pandas as pd
import datapane as dp
import numpy as np

def compliance_reports_raw(compliance_reports, severities=["Critical", "High"]):

    df = pd.DataFrame(compliance_reports)
    df = df[df['STATUS'].isin(["NonCompliant"])]
    
    df['RESOURCE_COUNT'] = (df['VIOLATIONS'].str.len())

    df = df.sort_values(by=['SEVERITY', 'RESOURCE_COUNT'],ascending=[True,False])
    
    df = df.replace({'SEVERITY': {1: "Critical", 2: "High", 3: "Medium", 4: "Low", 5: "Info"}})
    df = df[df['SEVERITY'].isin(severities)]
    
    df = df.reset_index()

    df['Resources'] = df['RESOURCE_COUNT'].astype('string') + " / " + df['ASSESSED_RESOURCE_COUNT'].astype('string')
    df = df[['ACCOUNT_ID', 'CATEGORY', 'TITLE', 'SEVERITY', 'Resources']]
    df.rename(columns={'ACCOUNT_ID': 'Account ID', 'CATEGORY': 'Category', 'TITLE': 'Title', 'SEVERITY': 'Severity'}, inplace=True)

    return df

def compliance_reports_raw_azure(compliance_reports, severities=["Critical", "High"]):

    df = pd.DataFrame(compliance_reports)
    df = df[df['STATUS'].isin(["NonCompliant"])]
    
    df['RESOURCE_COUNT'] = (df['VIOLATIONS'].str.len())

    df = df.sort_values(by=['SEVERITY', 'RESOURCE_COUNT'],ascending=[True,False])
    
    df = df.replace({'SEVERITY': {1: "Critical", 2: "High", 3: "Medium", 4: "Low", 5: "Info"}})
    df = df[df['SEVERITY'].isin(severities)]
    
    df = df.reset_index()

    df['Resources'] = df['RESOURCE_COUNT'].astype('string') + " / " + df['ASSESSED_RESOURCE_COUNT'].astype('string')
    df['SUBSCRIPTION_ID'] = df['SUBSCRIPTION_ID'].astype('string') + " (" + df['SUBSCRIPTION_NAME'].astype('string') + ")"


    df = df[['SUBSCRIPTION_ID', 'CATEGORY', 'TITLE', 'SEVERITY', 'Resources']]
    df.rename(columns={'SUBSCRIPTION_ID': 'Subscription', 'CATEGORY': 'Category', 'TITLE': 'Title', 'SEVERITY': 'Severity'}, inplace=True)

    return df

def compliance_reports_raw_gcp(compliance_reports, severities=["Critical", "High"]):

    df = pd.DataFrame(compliance_reports)
    df = df[df['STATUS'].isin(["NonCompliant"])]
    
    df['RESOURCE_COUNT'] = (df['VIOLATIONS'].str.len())

    df = df.sort_values(by=['SEVERITY', 'RESOURCE_COUNT'],ascending=[True,False])
    
    df = df.replace({'SEVERITY': {1: "Critical", 2: "High", 3: "Medium", 4: "Low", 5: "Info"}})
    df = df[df['SEVERITY'].isin(severities)]
    
    df = df.reset_index()

    df['Resources'] = df['RESOURCE_COUNT'].astype('string') + " / " + df['ASSESSED_RESOURCE_COUNT'].astype('string')
    df['PROJECT_ID'] = df['PROJECT_ID'].astype('string') + " (" + df['PROJECT_NAME'].astype('string') + ")"


    df = df[['PROJECT_ID', 'CATEGORY', 'TITLE', 'SEVERITY', 'Resources']]
    df.rename(columns={'PROJECT_ID': 'Project', 'CATEGORY': 'Category', 'TITLE': 'Title', 'SEVERITY': 'Severity'}, inplace=True)

    return df