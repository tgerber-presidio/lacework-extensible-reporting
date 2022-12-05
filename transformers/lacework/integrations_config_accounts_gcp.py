import pandas as pd
import datapane as dp
import numpy as np

def integrations_config_accounts_gcp(integrations, types=["'GCP_CFG'"]):
    df = pd.json_normalize(integrations)
    df = df[(df['TYPE'] == "GCP_CFG") & (df['ENABLED'] == 1) & (df['STATE.ok'] == 1)]

    if len(df) != 0 :
         return df['DATA.ID'].unique().tolist()
    else :
        return False