from datetime import datetime
import pandas as pd

class Cleaner:
    def __init__(self):
        pass
        
        
    def clean_data(self, df):

        df['Onboard_date'] = pd.to_datetime(df['Onboard_date'])

        df['Years'] = df['Onboard_date'].apply(lambda x: int(((datetime.now() - x).days)/365.25))

        df = df.drop(columns = ['Names', 'Onboard_date', 'Location', 'Company'])
        
        return df