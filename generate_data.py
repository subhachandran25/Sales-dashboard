import pandas as pd
import random

regions = ['North', 'South', 'East', 'West']
data = []

for region in regions:
    auh = f"AUH_{region}"
    for sm_idx in range(1, 4):
        senior_mgr = f"SM_{region}_{sm_idx}"
        for mgr_idx in range(1, 6):
            sales_mgr = f"Mgr_{region}_{sm_idx}_{mgr_idx}"
            for rep_idx in range(1, 11):
                sales_rep = f"Rep_{region}_{sm_idx}_{mgr_idx}_{rep_idx}"
                
                # Random performance metrics
                new_leads = random.randint(50, 100)
                disqualified = random.randint(5, 20)
                no_answer = random.randint(10, 30)
                qualified = new_leads - disqualified - no_answer
                converted = random.randint(0, qualified)
                deals_closed = random.randint(0, converted)
                
                data.append([
                    region, auh, senior_mgr, sales_mgr, sales_rep,
                    random.randint(200, 500), # Calls Dialed
                    random.randint(300, 1200), # Call Time Mins
                    new_leads, disqualified, no_answer, qualified,
                    converted, deals_closed, random.randint(5, 20) # Followup
                ])

columns = ['Region', 'AUH', 'Senior_Manager', 'Sales_Manager', 'Sales_Rep', 
           'Calls_Dialed', 'Call_Time_Mins', 'New_Leads', 'Disqualified', 
           'No_Answer', 'Qualified', 'Converted', 'Deals_Closed', 'Followup_Leads']

df = pd.DataFrame(data, columns=columns)
df.to_csv('data.csv', index=False)
print("data.csv has been generated successfully!")
