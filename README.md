# Startup-Acquisition-Status-Prediction.
#### Business Objective:
Given a startup's financial information, can we predict its current financial status?

#### Methodology:
This section deals with the methodology followed to accomplish and achieve the goals of the project. Code snippets are shown here for reference purposes, but the entire code is available in the # updated-Startup-Acquisition-Status-Prediction files. The methodology we followed is divided into main four parts: Data Collection, Data Preprocessing, EDA, Feature Engineering Data Modelling, pipeline, and Deployment 

#### 1. Data Collection:
The data provided by CrunchBase. Each row contains a Company’s Financial Information and is labeled with the company’s status (Operating, IPO, Acquired, Closed). This dataset is quite huge and thus it has 196553 rows and 44 columns.

#### 2. Data Preprocessing:
1. Each row represents one company and has its financial information such as founded_at, description, category_code, funding_total_usd, etc, and labeled with the company’s status (Operating, IPO, Acquired, Closed)
2. removed unwanted columns which are irrelevant to our problem.
3. Checked and Removed the columns which have more than 98% of missing values.
4. Found and removed outliers from the funding_total_usd, relationship using the IQR method.
5. Converted category_code from 42 unique categories to 15 categories
6. Converted country_code from 91 unique categories to 10 categories.
7. Created ‘isClosed’ dependent column from the status column
8. Created active_days column from founded_at and closed_at column
9. Removed duplicate columns from the dataset 
10. Removed irrelevant columns

#### 3. EDA

#### 4. Feature Engineering

Multicollinearity

Imbalance Dataset

Scaling

#### 5. Modelling

Logistic Regression

Random Forrest Classifier

XGBoost

SVM

#### 6. Pipeline
	
#### 7. Deployment

Created web app through Flask and deployed on heroku.

###### Detailed explanation of project is given bellow

[Startup.pdf](https://github.com/MelroyPer/Startup-Acquisition-Status-Prediction./files/9859717/Startup.pdf)
