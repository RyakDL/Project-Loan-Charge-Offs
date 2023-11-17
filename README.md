# Project 4: A study on Loan ChargeOffs
Project 4 

Group Members: Ryan Lund, Hamid Nazari, Lu Ye, Joseph Gonzalez, Cristian Guerrero, Stephanie Patrica Anshell

1) Project 4 Overview: 
The objective of this project is to study the relationship between loan charge offs and several other economic and loan variables that may have predictive power in determining if a loan charge off will occur or not. Four groups of different loan types have been formed and were studied: a) Credit Cards, b) Mortgages, c) Commercial Loans, and d) Commercial Real Estate loans. The dependent variable (or Y) for each group is the loan charge off rate by that particular category. The independent variables will included economic and loan related variables such as the Unemployment Rate, Change in Real GDP, Household Savings Rate, Consumer Confidence Index, the Federal Funds Interest Rate, Household Debt to Income Ratio and loan delinquencies (by the particular loan type). A list of the variables identified by loan file name is below:

A. Group A: Credit Cards: Y = CCARD_CO_QTR.xls. X’s = CCARD_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; SAVINGS_RATE_MO.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Consumer_Confidence_MO.xls; Household_DBT_Inc_QTR.xls

B. Group B: Mortgage Loans: Y =Mortage_CO_CO_QTR.xls. X’s = Mortage_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; SAVINGS_RATE_MO.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Consumer_Confidence_MO.xls;    Rental_Vacancy_Rate_CTR.xls; Household_DBT_Inc_QTR.xls

C. Group C: C&I Loans: Y =C&I_CO_CO_QTR.xls. X’s = C&I_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; CORP_DEBT_NET_WORTH_QTR.xls; CORP_SAVINGS_LEVEL_QTR.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Manufacturing_Confidence_MO.xls

D. Group D: CRE_loans: Y =CRE_CO_CO_QTR.xls. X’s = CRE_DELINQ_QTR.xls; UNRATE_MONTHLY.slx; CORP_DEBT_NET_WORTH_QTR.xls; CORP_SAVINGS_LEVEL_QTR.xls; GDP_QTR.xls; FEDFUNDS_MO.xls; Manufacturing_Confidence_MO.xls; Rental_Vacancy_Rate_CTR.xls

We primarily used four different machine learning methods to test our data: Decision Trees, Random Forests, Logistic Regressions and Deep Learning Networks.

2) Data Sources and ETL: The data for Project 4 was exclusively obtained from the Federal Reserve Economic Database (‘FRED’) maintained by the Federal Reserve Bank of St. Louis downloaded in Excel file format. The time periods for the data is both quarterly and monthly, and as part of the transformation of the data, quarterly data was converted into monthly data. After the data was transformed, it was merged and joined together in Python Pandas.In total, the final dataset had approximately 390 rows and dated back to 1991.

4) Correlation Matrixes and Boxplots: To explore the relationship between the variables, we used Seaborn, Pandas, Matlib, numpy and four different machine learning methods. A correlation matrix was created with Seaborn for each loan group. The correlation matrix was the first attempt to visualize the relationship between the variables. The colors of the correlation matrix corresponded to the strength and direction of the correlation: Darker colors indicated stronger correlations with Red signifying a positive correlation and blue indicating a negative correlation.

For example, The correlation matrix shown here indicates a strong positive correlation between credit card charge offs and delinquencies, household-debt-to-income, and the unemployment rate and the dependent value credit card charge offs. 

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/e40026b1-d187-4bb8-8c41-5f6e8d120357)

All four loan groups demonstrated positive correlations between delinquencies and the unemployment rate and loan charge offs. The box plot for credit cards was organized into 4 quartiles of charge off risk and showed a strong positive correlation between delinquencies and credit card charge offs. 

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/f004e2aa-7f6e-45c0-bfa9-ff6b3c22c1b0)

5) Decision Trees and Random Forest Trees were amongst some of the highest scoring machine learning models tested in Project 4. To begin, our group converted the independent variables in the loan groups to dummy variables and run the Random Forest models. This approach yielded good accuracy results, the however, as an example, the accuracy score for credit cards using dummy variables was 88.75% as compared to credit card Random Forest that used the actual numerical values which reported a 94.9% accuracy score. Consider the following connection between the variables shown in the Tree:

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/28a3c72f-3a84-4728-b1d7-23f8f38e103f)

Along the right branch of the tree, if Household-Debt-to-Income Ratio is above 10.43% and the Fed Funds Rate is above 2.19% and delinquencies are above 4.42% and the unemployment rate is above 4.45% and Consumer Confidence index is above 100.3, then the result is class 4 risk of charge off which signifies the highest quartile of credit card charge off risk. 

This branch describes the relationship between several variables in the model: a higher Fed Funds rate could make the Household debt to Income ratio higher indicating a higher load of household debt. This increased debt load could strain household income and increase the risk of delinquent loan payments. In turn, a higher unemployment rate could cause the risk of delinquent loan payments to go up as there are less jobs available to earn income which is needed to pay make loan payments. Finally, the Consumer Confidence index could be a leading or lagging indicator for increased credit card charge off risk in the model. In the past, Consumer Confidence has dipped before the onset of an economic recession. 

6) Neural Networks and Deep Learning: Deep Learning models were made for all 4 Loan Groups with the same model design. We first modeled transformed dummy data and later got much higher accuracy scores with actual numerical data. For example, the credit cards group reported the following design characteristics: 4 layers of hidden nodes with 60 nodes for the first 3 layers and 40 nodes for the 4th layer; The activation type for the 4 hidden layers was ‘relu’; The activation type for the final layer was ‘softmax’ amd there were 200 epochs for the calculation.

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/97232e0d-a341-4481-9ed0-78f9cfc78bbe)

The accuracy scores varied from loan group to loan group. Credit cards had the highest accuracy score at 90.82% while the C&I group had the lowest at 76.53%. Overall, it appears that the Deep learning model did better with Consumer type loans (Credit Cards and Mortgages) versus Commercial type loans (C&I loans and CRE loans). 

7) Project Summary Loan Results:

![Screenshot 2023-11-14 at 7 53 10 PM](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/23039b31-c6ed-4c72-8cb3-ddd6be0adb7d)
       
Random Forest with actual numerical values (as opposed to dummies) produced the highest average accuracy score of 93.91%. The lowest average accuracy score was the Deep Learning model that used dummy values at 27.55%. Next to the Deep Learning using dummy data, the Logistic Regression model produced the lowest average accuracy score of 80.86%. Compared to Random Forests model (Actual), it appears that Logistic Regressions was less accurate at predicting outcomes. 

The Overall Accuracy Score indicated that the Mortgage loans group was the highest at 91.63% and closely followed by the Credit cards group at 89.79%. Overall, the Consumer loans (credit cards and mortgages) performed better than the business loans (C&I and CRE) which appears to be influenced by the Deep Learning model accuracy scores. 
The lowest performing loan group was C&I loans with an 83.67% Overall Accuracy Score. This appears to be ‘across the board’ in terms of the model types, and in particular the Logistic Regression model and Deep Learning with actual numerical values model. 

It is noted that the different loan groups contain many of the same variables however some unique variables. The group design may have had an affect on the the accuracy scores as well as the different models.

8) Further Considerations with the Data for Future Studies: Several concepts could be tested with the data and existing models to further explore the relationship between the nature of loan charge offs and the independent variables:

A. Time elements could be tested with the existing data set and run through all the models used in Project 4: Time lags and Time deltas. Time lags would effectively ‘lag’ one or more variables by a period of months. For example, loan charge offs may lag between loan delinquencies and a rising unemployment rate. Time deltas would calculate the difference between two different points in time for one or more variables. This could reveal if the change in a variable’s value had an affect on loan charge offs. 

B. Other considerations for further studies could be expanding the existing data set where it is possible with the existing variables. For example, what would the accuracy scores look like scaled up 10 times, or 100 times? There may be limits to scaling up economic variables, however variables such as delinquency rates could hypothetically be measured on a weekly or even daily basis, thus providing a much larger dataset. 

C. The selection of independent variables could be expanded, changed and reconfigured. For example, further studies on variables and conditions related to C&I loan charge offs could be explored. 

9) Finally, the Correlation Matrix below shows that the majority of all 4 loan groups’ delinquencies, charge offs and the unemployment rate are positively correlated.  This suggests that these independent variables may have relationships across the four loan groups.

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/8a3dd6c0-7aca-4e53-919c-760a17d81962)






