## Credit Card Transaction Project

### Click [here](https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset) to view dataset

### Objectives
#### Exploratory Data Analysis:

    1. Behavioral Patterns
    Hourly Velocity: At what time of day do most transactions occur, and do "off-hour" transactions (e.g., 3 AM) show different spending amounts?
    Category Spending: Which categories (e.g., health_fitness vs. online_retail) have the most frequent transactions versus the highest total monetary value?

    2. Geographical Anomalies
    Distance Logic: What is the average distance between a user's home (lat/long) and the merchant's location?
    State-Level Trends: Are there specific states or cities that exhibit significantly higher average transaction values?

    3. Demographic Insights
    Age vs. Spending: Is there a correlation between the cardholder’s age (derived from dob) and their preferred spending categories?
    Gender Bias: Do spending patterns in categories like travel or food_dining differ significantly between genders?

    4. Financial Outliers
    Transaction Magnitude: How do individual transaction amounts compare to the user’s overall mean spending?
    High-Volume Merchants: Which specific merchants or merchant categories are responsible for the most "outlier" (extreme value) transactions?

    5. Temporal Seasonality
    Day-of-Week Analysis: Does spending volume significantly increase on weekends compared to weekdays?
    Monthly Cycles: Are there visible "payday" spikes in the data where transaction volume surges at the beginning or end of the month?

#### Models:
    1. Fraud Detection (Classification): Use XGBoost or Random Forest to flag suspicious transactions.
    Challenge: Handling the extreme class imbalance (few frauds vs. many legit transactions).

    2. Spending Forecasting (Time-Series): Use Prophet to predict a user's total spending for the next month.

    5. Customer Segmentation (Clustering): Use K-Means to group users into "Budgeters," "Luxury Spenders," or "Frequent Travelers."

    4. Anomaly Detection (Unsupervised): Use Isolation Forest to find transactions that don't fit any normal spending profile.