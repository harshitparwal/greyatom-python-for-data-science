# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank= pd.read_csv(path)

#Code starts here
#step1
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var.head())
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var.head())
print(categorical_var.shape)
print(numerical_var.shape)


#step2
banks=bank.drop(columns='Loan_ID', axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
for x in banks.columns.values:
    banks[x]=banks[x].fillna(value=bank_mode[x].iloc[0])
#banks['Gender'].fillna(value=bank_mode['Gender'],inplace=True)
print(banks.shape)
print(banks.isnull().sum().values.sum())


#step3
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)


#step4
seloan= banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')] 
loan_approved_se = len(seloan)
percentage_se=loan_approved_se/614*100
nseloan = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]
loan_approved_nse = len(nseloan)
percentage_nse = loan_approved_nse/614*100
print(percentage_se)
print(percentage_nse)


#step5
loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)
loan_term=loan_term[loan_term>=25]
big_loan_term=len(loan_term)
print(big_loan_term)


#step6
loan_groupby=banks.groupby(by='Loan_Status')
mean_values=loan_groupby[['ApplicantIncome','Credit_History']].mean()
print(mean_values)




