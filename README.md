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

2) Data Sources and ETL: The data for Project 4 was exclusively obtained from the Federal Reserve Economic Database (‘FRED’) maintained by the Federal Reserve Bank of St. Louis downloaded in Excel file format. The time periods for the data is both quarterly and monthly, and as part of the transformation of the data, quarterly data was converted into monthly data. After the data was transformed, it was merged and joined together in Python Pandas.In total, the final dataset had approximately 390 rows and dated back to 1991.

4) Correlation Matrixes and Boxplots: To explore the relationship between the variables, we used Seaborn, Pandas, Matlib, numpy and four different machine learning methods. A correlation matrix was created with Seaborn for each loan group. The correlation matrix was the first attempt to visualize the relationship between the variables. The colors of the correlation matrix corresponded to the strength and direction of the correlation: Darker colors indicated stronger correlations with Red signifying a positive correlation and blue indicating a negative correlation.

For example, The correlation matrix shown here indicates a strong positive correlation between credit card charge offs and delinquencies, household-debt-to-income, and the unemployment rate and the dependent value credit card charge offs. 

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/e40026b1-d187-4bb8-8c41-5f6e8d120357)

All four loan groups demonstrated positive correlations between delinquencies and the unemployment rate and loan charge offs. The box plot for credit cards was organized into 4 quartiles of charge off risk and showed a strong positive correlation between delinquencies and credit card charge offs. 

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/f004e2aa-7f6e-45c0-bfa9-ff6b3c22c1b0)

5) Decision Trees and Random Forest Trees were amongst some of the highest scoring machine learning models tested in Project 4. For example, the credit card Decision Tree shown here reported a 93.9% accuracy score. Consider the following connection between the variables shown in the Tree:

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/12b3d01e-591b-4b73-9015-7ece0f9515eb)

Along the right branch of the tree, if Household-Debt-to-Income Ratio is above 10.43% and the Fed Funds Rate is above 2.19% and delinquencies are above 4.42% and the unemployment rate is above 4.45% and Consumer Confidence index is above 100.3, then the result is class 4 risk of charge off which signifies the highest quartile of credit card charge off risk. 

This branch describes the relationship between several variables in the model: a higher Fed Funds rate could make the Household debt to Income ratio higher indicating a higher load of household debt. This increased debt load could strain household income and increase the risk of delinquent loan payments. In turn, a higher unemployment rate could cause the risk of delinquent loan payments to go up as there are less jobs available to earn income which is needed to pay make loan payments. Finally, the Consumer Confidence index could be a leading or lagging indicator for increased credit card charge off risk in the model. In the past, Consumer Confidence has dipped before the onset of an economic recession. 

6) Neural Networks and Deep Learning: Deep Learning models were made for all 4 Loan Groups with the same model design. The models used actual numerical data as opposed to transformed dummy data.For example, the credit cards group reported the following design characteristics: 4 layers of hidden nodes with 60 nodes for the first 3 layers and 40 nodes for the 4th layer; The activation type for the 4 hidden layers was ‘relu’; The activation type for the final layer was ‘softmax’ amd there were 200 epochs for the calculation.

![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/4fffc41e-8b54-4d4e-8c9d-97b13c259a52)

The accuracy scores varied from loan group to loan group. Credit cards had the highest accuracy score at 90.82% while the C&I group had the lowest at 76.53%. Overall, it appears that the Deep learning model did better with Consumer type loans (Credit Cards and Mortgages) versus Commercial type loans (C&I loans and CRE loans). 

7) Project Summary Loan Results:



Random Forest with actual numerical values (as opposed to dummies) produced the highest average accuracy score of 93.91%. The lowest average accuracy score was the Deep Learning model that used dummy values at 27.55%. Next to the Deep Learning using dummy data, the Logistic Regression model produced the lowest average accuracy score of 80.86%. Compared to Random Forests model (Actual), it appears that Logistic Regressions was less accurate at predicting outcomes. 

The Overall Accuracy Score indicated that the Mortgage loans group was the highest at 91.63% and closely followed by the Credit cards group at 89.79%. Overall, the Consumer loans (credit cards and mortgages) performed better than the business loans (C&I and CRE) which appears to be influenced by the Deep Learning model accuracy scores. 
The lowest performing loan group was C&I loans with an 83.67% Overall Accuracy Score. This appears to be ‘across the board’ in terms of the model types, and in particular the Logistic Regression model and Deep Learning with actual numerical values model. 

It is noted that the different loan groups contain many of the same variables however some unique variables. The group design may have had an affect on the the accuracy scores as well as the different models.

Model Type	Decision Tree (Actual)	Random_Forest (dummies)	Random_Forest (Actual)	Logistic Regression	Deep Learning (actual)		Deep Learning (dummies)		
Loan Group	Accuracy Score	Accuracy Score	Accuracy Score	Accuracy Score	Accuracy Score	Loss Rate	Accuracy Score	Loss Rate	Overall Accruacy Score*
Credit cards	93.88%	88.75%	94.90%	80.61%	90.82%	30.67%	25.51%	-6.7051e	89.79%
Mortgage loans	91.84%	94.90%	93.88%	86.73%	88.78%	37.52%	32.65%	-8.9701e	91.23%
C&I loans	83.67%	90.82%	92.86%	74.48%	76.53%	69.54%	25.51%	-5.8487e	83.67%
CRE loans	88.88%	95.18%	93.98%	81.63%	83.67%	42.86%	26.53%	-1.0892e	88.67%
Average:	89.57%	92.41%	93.91%	80.86%	84.95%	45.15%	27.55%	N/A	
	*Note: excludes deep learning dummies approach accuracy score. 								![image](https://github.com/RyakDL/Project-Loan-Charge-Offs/assets/132794157/7da327ea-9d96-464a-b279-2aa8af0bd3a7)


