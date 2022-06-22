import uuid
import random
# import datetime
import numpy as np
import pandas as pd

num_users = 100000
features = ['ID','Gender','Marital_Status', 'Dependants', 'Education','Occupation_Status','Age',\
            'State','State_Code', 'Salary','Current_Loan','Loan_Amount', 'Tenure',\
            'Previous_Loans','Defaulted','Default_Dur', 'newscore', 'Status']
df = pd.DataFrame(columns = features)

class Create_Dataset: 
    """
    This function would create the dataset
    """

    def __init__(self, df : pd.DataFrame): 
        self.df = df
        print('Creating DataFrame...!!!')
    
    def create_unique_id(self) -> pd.DataFrame: 
        self.df['ID'] = [uuid.uuid4().hex for i in range(num_users)]
        return self.df
    
    def create_gender(self) -> pd.DataFrame:
        genders = ["male", "female"]
        self.df['Gender'] =  random.choices(
            genders, weights=(60,40), k=num_users)
        return self.df
    
    def create_occupation(self) -> pd.DataFrame:
        occupation = ['Employed', 'Self Employed', 'Unemployed']
        self.df['Occupation_Status'] = random.choices(
            occupation, weights=(35, 55, 10), k=num_users)
        return self.df

    def create_age(self) -> pd.DataFrame:
        np.random.seed(42)
        def age_range(gender):
            """
            Generates a age based on gender
            """
            if gender=='male':
                return np.random.randint(19, 50)
            elif gender=='female':
                return np.random.randint(25, 40)
            return np.random.randint(19, 50)
        # Generating names for each user
        self.df['Age'] = [age_range(i) for i in self.df['Gender']]
        return self.df
    
    def create_state(self) -> pd.DataFrame:
        states = ['Abia', 'Abuja', 'Akwa Ibom', 'Bauchi', 'Bayelsa', 'Cross River', 'Delta','Edo','Ekiti',
                'Enugu', 'Imo','Kaduna','Kano','Kogi','Kwara','Lagos','Ogun','Ondo','Osun',
                'Oyo','Port Harcourt','Sokoto']

        self.df['State'] = random.choices(
            states,
            weights = (10,30,4,1,3,12,6,2,10,7,7,12,15,5,8,60,10,7,8,14,20,2),
            k = num_users
        )
        return self.df

    def create_state_code(self) -> pd.DataFrame:
        def d2d_ratio(state):
            if (state == 'Abuja') | (state == 'Lagos') | (state == 'Port Harcourt'):
                return 5
            elif (state == 'Kano') | (state == 'Kwara') | (state == 'Oyo') | (state == 'Ogun') | (state == 'Cross River') | (state == 'Imo'):
                return 4
            elif (state == 'Kaduna') | (state == 'Kogi') | (state == 'Abia') | (state ==  'Enugu') | (state == 'Osun' ) | (state == 'Edo'):
                return 3
            return 2
        
        self.df['State_Code'] = [d2d_ratio(i) for i in self.df['State']]
        return self.df
        
    def create_tenure(self) -> pd.DataFrame:
        np.random.seed(3)
        def ten(period):
            if period == True:
                return np.random.randint(1, 5)
            return 0
        self.df['Tenure'] = [ten(i) for i in self.df['Current_Loan']]
        return self.df

    def create_current_loan(self) -> pd.DataFrame: 
        choice = [True, False]
        self.df['Current_Loan'] = random.choices(
            choice, weights = (30, 70),k=num_users)
        return self.df

    def create_previous_loans(self) -> pd.DataFrame:#
        self.df['Previous_Loans'] = self.df['Current_Loan'].apply(lambda x: random.choices((1,2,3,4), weights = [50,25,15,10])[0] if x == True else random.choices((0,1,2), weights = [60,32,8])[0])
        return self.df

    def create_salary(self) -> pd.DataFrame: 
        def salary(df, sal, stats, loc, scale):
            self.df.loc[(self.df['State_Code'] == sal) & (self.df['Occupation_Status'] == stats),'Salary'] =  int(np.random.normal(loc = loc, scale = scale))
        salary(self.df, 5,'Employed',300000,150000)
        salary(self.df, 5,'Self Employed',150000,50000)
        salary(self.df, 5,'Unemployed',20000,5000)
        
        salary(self.df, 4,'Employed',200000,75000)
        salary(self.df, 4,'Self Employed',100000,30000)
        salary(self.df, 4,'Unemployed',10000,5000)

        salary(self.df, 3,'Employed',100000,50000)      
        salary(self.df, 3,'Self Employed',50000,30000)
        salary(self.df, 3,'Unemployed',10000,5000)

        salary(self.df, 2,'Employed',60000,30000)
        salary(self.df, 2,'Self Employed',20000,10000)
        salary(self.df, 2,'Unemployed',5000,3000)
        return self.df 

    def create_loan_amount(self) -> pd.DataFrame: 
        self.df['Loan_Amnt'] = self.df['Salary'].apply(lambda x : x*0.40 if (self.df['Current_Loan'] == True).all() else 0 )
        return self.df

    def create_defaulted(self) -> pd.DataFrame: 
        self.df['Defaulted'] = self.df['Previous_Loans'].apply(lambda x : random.choices([True, False], weights = [40, 60])[0] if x >= 1 else False)
        return self.df

    def create_defaulted_dur(self) -> pd.DataFrame: 
        self.df['Default_Dur'] = self.df['Defaulted'].apply(lambda x : random.choices([1,2,3,4], weights = (10,7,4,3))[0] if x == True else 0)
        return self.df
    
    def create_education(self) -> pd.DataFrame: 
        education = ['Graduate', 'No Graduate']
        self.df['Education'] = self.df['Age'].apply(lambda x : random.choices(education, weights = [60, 40])[0] if x >= 27 else ('No Graduate' if x < 22 else random.choices(education, weights = [50,50])[0]))
        return self.df
    
    def create_marriage_stats(self) -> pd.DataFrame:
        married_stats = ['Married', 'Not Married']
        def mar_stats(df, num_2, gen, choice): 
            self.df.loc[(self.df['Age'] <= num_2) & (self.df['Gender'] == gen), 'Marital_Status'] = choice
        def mar_stats_2(df, num_2, gen, choice):
            self.df.loc[(self.df['Age'] > num_2) & (self.df['Gender'] == gen), 'Marital_Status'] = choice

        mar_stats(self.df, 26, 'Male', random.choices(married_stats, weights =[30,70], k = len(self.df.loc[(self.df.Age <=26) & (self.df.Gender == 'Male')])))
        mar_stats(self.df, 25, 'Female', random.choices(married_stats, weights =[50,50], k = len(self.df.loc[(self.df.Age <= 25) & (self.df.Gender == 'Female')])))
        mar_stats_2(self.df, 26, 'Male', random.choices(married_stats, weights =[70, 30], k = len(self.df.loc[(self.df.Age > 26) & (self.df.Gender == 'Male')])))
        mar_stats_2(self.df, 25, 'Female', random.choices(married_stats, weights =[80,20], k = len(self.df.loc[(self.df.Age > 25) & (self.df.Gender == 'Female')])))
        return self.df

    def create_dependants(self) -> pd.DataFrame:
        self.df['Dependants'] = self.df['Marital_Status'].apply(lambda x : np.random.randint(0,6) if x == 'Married' else np.random.randint(0,2))
        return self.df
 
    def create_get_score(self) -> pd.DataFrame:
        for index, row in self.df.iterrows():
            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0 
            c5 = 0
            c6 = 0
            c7 = 0
            c8 = 0
            c9 = 0
            score = 0
    
            if (row['Occupation Status'] == 'Employed'):
                c1 = 3
            elif (row['Occupation Status'] == 'Self Employed'): 
                c1 = 2
            c1 = 1

            if (row['Education'] == 'Graduate'):
                c2 = 5
            c2 = 2

            if (row['Marital_Status'] == 'Married'):
                c3 = 4
            c3 = 2 

            if (row['Dependants'] == 0):
                c4 = 5
            elif (row['Dependants'] == 1):
                c4 = 4
            elif (row['Dependants'] == 2):
                c4 = 3 
            c4 = 2

            if (row['Salary'] > 0):
                c5 = row['Salary'] / 10000
            
            if (row['State_Code'] == 5): 
                c6 = 5
            elif (row['State_Code'] == 4):
                c6 = 4
            elif (row['State_Code'] == 3): 
                c6 = 3
            c6 = 2 

            if (row['Current Loan'] == True):
                c7 = 0
            elif ((row['Previous Loans'] ==1) and (row['Defaulted'] == True)):
                c7 = 0
            elif ((row['Previous Loans'] > 0) and (row['Defaulted'] == False)):
                c7 = 5
            c7 = 3
            
            c8 = c1+c2+c3+c4
            c9 = c5*c6*c7
            score = c8*c9

            self.df.loc[[index], 'newscore'] = score

        return self.df

    def create_get_target_data(self)  -> pd.DataFrame:  
        self.df['Status'] = self.df['newscore'].apply(lambda x: 1 if x > 500 else 0)
        return self.df

    def create_data(self, save = False) -> pd.DataFrame:
        self.create_unique_id()
        self.create_gender()
        self.create_occupation()
        self.create_age()
        self.create_state()
        self.create_state_code()
        self.create_current_loan()
        self.create_loan_amount()
        self.create_tenure()
        self.create_previous_loans()
        self.create_salary()
        self.create_defaulted()
        self.create_defaulted_dur()
        self.create_marriage_stats()
        self.create_education()
        self.create_dependants()
        self.create_get_score()
        self.create_get_target_data()
        
        if save:
            self.df.to_csv('../data/auction_data.csv', index=False)
            print('File Successfully Saved.!!!')
        return self.df

if __name__ == "__main__":
    cleaner = Create_Dataset(df)
    cleaner.create_data(True)