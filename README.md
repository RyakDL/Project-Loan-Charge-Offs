# Project-Loan-Charge-Offs
Project 4 

Group Members: Ryan Lund, Hamid Nazari, Lu Ye, Joseph Gonzalez, Cristian Guerrero

Project 4 Overview: 
1) The objective of this prject is to study the relationship between loan charge offs and several other economic and loan variables that may have predictive power in determining if a loan charge off will occur or not. Four groups of different loan types have been formed and will be studied: a) Credit Cards, b) Mortgages, c) Commercial Loans, and d) Commercial Real Estate loans. The dependent variable (or Y) for each group is the loan charge off rate by that particular category. The independent variables will include (but not be limited to) variables such as the Unemployment Rate, Change in Real GDP, Household Savings Rate, Consumer Confidence Index, the Federal Funds Interest Rate, Household Debt to Income Ratio and loan delinquencies (by the particular loan type). The commercial loans will have similar variables except instead of Consumer Confidence it will be Business Confidence and savings rates will be corporate instead of household.
2) The source of data for this project is the Saint Luis Federal Reserve known as FRED. Data has been downloaded in Excel file format. The time periods for the data is both quarterly and monthly, and as part of the transformation of the data, quarterly data will be converted into monthly data. After the data has been transformed, it will be merged and joined together in Python Pandas. 
3) To explore the relationship between the variables, we will use Seaborn, Pandas and Matlib. Particular focus will be paid attention to correlations between the data by using Seaborn visualizations such as the diagonal correlation matrix and correlgrams.
4) To explore if the correlations between data can be improved, the independent variables will be time-lagged in a Scenario 2 for all the loan types. It is possible that variables such as Unemployment Rate and Loan Delinquences could 'lead' loan charge offs by up to 6 months.
5) After the visualizations are created, the group will move on to running Supervised Machine Learning Models with Regressions. The data is continous and will have a 'middle' and therefore lends itself to Regressions. The Regressions used will be Logistic Regressions and Ploynominal Regressions.
6) Last but certainly not least, the dataset will be modeled and predicted with a neural network. 
