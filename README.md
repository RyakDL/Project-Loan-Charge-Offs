# Project 4: A study on Loan ChargeOffs
Project 4 

Group Members: Ryan Lund, Hamid Nazari, Lu Ye, Joseph Gonzalez, Cristian Guerrero, Stephanie Patrica Anshell

1) Project 4 Overview: 
The objective of this project is to study the relationship between loan charge offs and several other economic and loan variables that may have predictive power in determining if a loan charge off will occur or not. Four groups of different loan types have been formed and were studied: a) Credit Cards, b) Mortgages, c) Commercial Loans, and d) Commercial Real Estate loans. The dependent variable (or Y) for each group is the loan charge off rate by that particular category. The independent variables will included economic and loan related variables such as the Unemployment Rate, Change in Real GDP, Household Savings Rate, Consumer Confidence Index, the Federal Funds Interest Rate, Household Debt to Income Ratio and loan delinquencies (by the particular loan type). A list of the variables identified by loan file name is below:
   A.	Group A: Credit Cards 
   a.	Y = CCARD_CO_QTR.xls
   b.	X’s = CCARD_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; SAVINGS_RATE_MO.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Consumer_Confidence_MO.xls; Household_DBT_Inc_QTR.xls

  B.	Group B: Mortgage Loans 
  a.	Y =Mortage_CO_CO_QTR.xls
  b.	X’s = Mortage_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; SAVINGS_RATE_MO.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Consumer_Confidence_MO.xls;    Rental_Vacancy_Rate_CTR.xls; Household_DBT_Inc_QTR.xls

  C.	Group C: C&I Loans 
  a.	Y =C&I_CO_CO_QTR.xls
  b.	X’s = C&I_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; CORP_DEBT_NET_WORTH_QTR.xls; CORP_SAVINGS_LEVEL_QTR.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Manufacturing_Confidence_MO.xls

  D.	Group D: CRE_loans
  a.	Y =CRE_CO_CO_QTR.xls
  b.	X’s = CRE_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; CORP_DEBT_NET_WORTH_QTR.xls; CORP_SAVINGS_LEVEL_QTR.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Manufacturing_Confidence_MO.xls; Rental_Vacancy_Rate_CTR.xls

We primarily used four different machine learning methods to test our data: Decision Trees, Random Forests, Logistic Regressions and Deep Learning Networks.

2) The data for Project 4 was exclusively obtained from the Federal Reserve Economic Database (‘FRED’) maintained by the Federal Reserve Bank of St. Louis. 
downloaded in Excel file format. The time periods for the data is both quarterly and monthly, and as part of the transformation of the data, quarterly data was converted into monthly data. After the data was transformed, it was merged and joined together in Python Pandas.In total, the final dataset had approximately 390 rows and dated back to 1991.

3) To explore the relationship between the variables, we used Seaborn, Pandas, Matlib, numpy and four different machine learning methods. A correlation matrix was created with Seaborn for each loan group. The correlation matrix was the first attempt to visualize the relationship between the variables. The colors of the correlation matrix corresponded to the strength and direction of the correlation: Darker colors indicated stronger correlations with Red signifying a positive correlation and blue indicating a negative correlation.

For example, The correlation matrix shown here indicates a strong positive correlation between credit card charge offs and delinquencies, household-debt-to-income, and the unemployment rate and the dependent value credit card charge offs. 
![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/e40026b1-d187-4bb8-8c41-5f6e8d120357)

All four loan groups demonstrated positive correlations between delinquencies and the unemployment rate and loan charge offs.
The box plot for credit cards was organized into 4 quartiles of charge off risk and showed a strong positive correlation between delinquencies and credit card charge offs. 



6) To explore if the correlations between data can be improved, the independent variables will be time-lagged in a Scenario 2 for all the loan types. It is possible that variables such as Unemployment Rate and Loan Delinquences could 'lead' loan charge offs by up to 6 months.
7) After the visualizations are created, the group will move on to running Supervised Machine Learning Models with Regressions. The data is continous and will have a 'middle' and therefore lends itself to Regressions. The Regressions used will be Logistic Regressions and Ploynominal Regressions.
8) Last but certainly not least, the dataset will be modeled and predicted with a neural network. 
