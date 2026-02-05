import { CreditCardProject } from "./CONSTANTS";

const creditCardData = {
  title: CreditCardProject,
  description:
    "This comprehensive dataset provides a wealth of information about all countries worldwide, covering a wide range of indicators and attributes. It encompasses demographic statistics, economic indicators, environmental factors, healthcare metrics, education statistics, and much more. With every country represented, this dataset offers a complete global perspective on various aspects of nations, enabling in-depth analyses and cross-country comparisons.",
  link: "https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023",
  insightSummary: `Analysis of the Global Country Information Dataset 2023 reveals that human well-being is driven more by specialized education and healthcare quality than by raw economic output or urbanization. While GDP and urban population correlate with higher CO2 emissions and tertiary education, they have surprisingly negligible effects on life expectancy. Instead, longevity is most accurately predicted by gross tertiary enrollment and is hindered by high infant and maternal mortality rates.
Environmentally, the link between urbanization and emissions is stark—as seen in World Bank Data for China—yet these factors do not directly dictate national health outcomes. In the labor sector, metrics like minimum wage and urban density show little interdependence, with the only notable relationship being a moderate negative correlation between unemployment and labor force participation. Ultimately, the data suggests that advancing physician density and higher education are the most effective levers for improving global living standards.`,
  insights: [
    {
      topic: "Demographics",
      informations: [
        {
          question:
            "Is there a correlation between the cardholder’s age and their preferred spending categories?",
          answer:
            "There is a significant correlation between the age and spending categories as confirmed using anova test. A pvalue < 0.001 was obtained and a partial eta-squared (np2) value of 0.01 was obtained. The pvalue obtained signifies the statistical significant while the np2 value obtained means age only explains 1% of the spending category variance.",
        },
        {
          question:
            "Do spending patterns in categories like travel or food_dining differ significantly between genders?",
          answer:
            "To determine the relationship between gender, spending categories and amount , a two way anova was used. The pvalue gotten between gender and amount is 0.7 which means there is no assosciation between gender and amount. The pvalue gotten for category vs amount and category+gender vs amount is less than 0.01 which implies a statistical significant while the np2 value gotten was far less than 0.01 which implies even though there is a statistical significance, the amount of variability explained is less than 1%.",
        },
      ],
    },

    {
      topic: "Behavioural Patterns",
      informations: [
        {
          question: `At what hour of day do most transactions occur, and do "off-hour" transactions (e.g., 3 AM) show different spending amounts?`,
          answer:
            "Most transactions occur at 23:00 (11:00pm). There is a significant variations in the spending amount at off-hour period. The average amount spent at off-hour period is 78.59($) while 66.24($) for non off-hour period. Using a one-tailed (greater) Mannwhitneyu test on the amount by off-hour feature, a pvalue < 0.001 was gotten hence the mean of the amount spent at off-hour period is significantly greater than the mean of the amount spent at a non off-hour period.",
          imgs: [
            "/credit_card_visuals/hourly_velocity.png",
            "/credit_card_visuals/amount_cat_by_off_hour.png",
          ],
        },
        {
          question:
            "Which categories (e.g., health_fitness vs. online_retail) have the most frequent transactions versus the highest total monetary value?",
          answer:
            "The category with the most frequent transactions is gas transport while the one with the highest monetary value is grocery pos. Using Kruskal wallis test to figure out if there is an assosciation between category and amount spent, a pvalue < 0.001 was gotten which signifies the prescence of significant assosciation between the two features.",
          imgs: ["/credit_card_visuals/category_freq_amnt_sum.png"],
        },
      ],
    },
    {
      topic: "Geographical Anomalies",
      informations: [
        {
          question:
            "What is the average distance between a user's home (lat/long) and the merchant's location?",
          answer:
            "The average  distance between a user's home (lat/long) and the merchant's location is 70.11 km.",
        },
        {
          question:
            "Are there specific states or cities that exhibit significantly higher average transaction valu",
          answer:
            "Base on transaction volume the city and state with the highest value are Birmingham and TX respectively. Base on transaction amount($) the city and state with the highest value are Meridian and TX respectively. ",
          img: [
            "/credit_card_visuals/city_state_transaction_amount.png",
            "/credit_card_visuals/city_state_transaction_freq.png",
          ],
        },
      ],
    },
    {
      topic: "Financial Ouliers",
      informations: [
        {
          question:
            "How do individual transaction amounts compare to the user’s overall mean spending?",
          answer: `The average amount spent is $70.35, the minimum amount spent is $1, the maximum amount spent is $28948.9. 25% of the total population spent exactly or below $9.65. 50% of the total population spent exactly or below $47.52 .75% of the total population spent exactly or below $83.14.`,
        },
        {
          question: `Which specific merchants or categories are responsible for the most "outlier" (extreme value) transactions?`,
          answer:
            "The merchant and category responsible for most outlier is Fraud kilback LLC and Grocery POS respectively.",
          imgs: ["/credit_card_visuals/outliers_bar_plot.png"],
        },
      ],
    },
    {
      topic: "Temporal Seasonality",
      informations: [
        {
          question:
            "Does spending volume significantly increase on weekends compared to weekdays?",
          answer:
            "The average spending on weekend and weekdays are $69.90  and $70.59 respectively, hence there is less than $1 difference between the two averages. The total pending on weekend and weekdays are $31562634.11 and $59659794.79 respectively. The difference between the sum is large which is because the total count of transactions occuring on weekend(451536) is far less than the ones that occur during the weekday(845139). To determine the significance of weekdays and weekends on the amount spent, pointbiserial and mannwhitneyu test was used. The pointbiserial test reported a correlation coeficient of -0.002 and a pvalue of 0.01 which means the weekday/weekend have no practical effect on the amount spent even if the relationship between them is statistically significant. Using a one-tailed (less) mannwhitneyu test, to test for the statistical significance between the mean of transactions occuring on weekend and those that occurs on weekday, a pvalue of 0.007 was gotten which confirms that the mean amount spent during the weekend($69.90) is significantly less than the mean amount($70.59) spent weekday. This is a case of statistically significant but practically insignificant.",
          imgs: ["/credit_card_visuals/spending_amount.png"],
        },
        {
          question: `Are there visible "payday" spikes in the data where transaction volume surges at the beginning or end of the month?`,
          answer:
            "There are spikes in transaction volume on the following payday: 1,2,28 & 30.",
          imgs: ["/credit_card_visuals/transaction_spikes.png"],
        },
      ],
    },
  ],
};

export default creditCardData;
