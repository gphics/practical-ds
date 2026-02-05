import { LoanProject } from "./CONSTANTS";

const loanData = {
  title: LoanProject,
  description:
    "The dataset includes 14 columns representing different factors influencing loan approvals and defaults",
  link: "https://www.kaggle.com/datasets/udaymalviya/bank-loan-data",
  insightSummary: `The provided analysis of the Bank Loan Dataset offers a data-driven perspective on credit risk, revealing that traditional indicators often yield unexpected results. Notably, the financial profile of a borrower shows a counterintuitive trend: defaulters possess a higher median income ($72,928) than non-defaulters ($50,629). Furthermore, while variables such as age, employment length, and education level are often scrutinized during applications, this data suggests they have a statistically negligible impact on a borrower's likelihood to repay.

Risk is more clearly defined by financial ratios and loan intent. While the typical industry threshold for Debt-to-Income (DTI) sits between 36% and 43%, predictive modeling on this dataset identifies a much stricter risk threshold of 24%. Behavioral patterns also emerge regarding the purpose of the loan; Debt Consolidation and Medical expenses represent the highest-risk categories, whereas Venture and Education loans are statistically the safest.

Finally, the analysis confirms that external costs and collateral status remain relevant. Interest rates maintain a mild positive correlation with default, suggesting that higher costs of borrowing do increase the probability of non-payment. Additionally, home ownership type serves as a moderate predictor of loan status. Collectively, these findings suggest that for this population, specific financial burdens and loan categories are more reliable predictors of risk than general demographic stability. `,
  insights: [
    {
      topic: "Demographics",
      informations: [
        {
          question:
            "What is the average and median income of loan applicants, and how does it differ between those who repay and those who default?",
          answer: `Generally the mean and median income of loan applicants are 80319.05 and 67048.00 respectively. The mean and median income of loan defaulters are 86157.04 and 72928.00 respectively. The mean and median income of non-defaulters are 59886.09 and 50629.00 respectively. In conclusion, loan defaulters earn more than those that repay loan.
`,
        },
        {
          question: `Does the length of employment or "Years at Current Job" correlate with a lower likelihood of default?`,
          answer:
            "Using spearman rank order correlation method, the correlation coeficient is -0.027 and the pvalue is 6.691968733916838e-09. Hence there is a weak to non-existent statistically significant correlation between the employment experience and loan status. The statistical significance was further confirmed with mannwhitneyu test and a pvalue of 6.731452348334923e-09. In conclusion there is a statistically.",
        },
        {
          question:
            "How do loan default/repay rates vary across different education levels ?",
          answer:
            "Using cochran armitage trend test, a pvalue of 0.71 was gotten when comparing education levels and loan status. Hence there is no significant association between the two. This was further confirmed using chi-square test and a pvalue of 0.73 was gotten.",
        },
        {
          question:
            "What is the average Debt-to-Income (DTI) ratio of borrowers, and at what threshold does the risk of default significantly increase?",
          answer:
            "The DTI have a mean of 13% and a median 12%. The data distribution of the DTI is right skewed hence the median was chosen as the appropriate centre of tendency. Median also means the 50th percentile meaning less than 50% of the entire population have a DTI value less than 12% and more than 50% of the entire population have a DTI value greater than 12%. In the financial field the acceptable threshold of DTI is between 36-43%, any value above this range signifies a high risk loan. To get the DTI threshold in my dataset, I used logistic regression and decision tree classifier and I got a threshold of 24%.",
          imgs: ["/loan_visuals/dti_sigmoid_curve_threshold.png"],
        },
        {
          question:
            "Which home ownership shows the highest concentration of loan applications or default rates?",
          answer:
            "Using chi-square test to investigate the associativity between home ownership type and loan status, a pvalue of 0.0 was gotten which implies a statistically significant relationship between the two. Using Cramer's V test to check the strength, I got a value of 0.257 which implies there is a weak to moderate assosciativity test between the two.",
          imgs: ["/loan_visuals/home_ownership_count_plot.png"],
        },
        {
          question:
            "what is the relationship between age and whether loan applicant would repay or default ?",
          answer:
            "Using spearmans rank correlation test, a correlation coeficient of -0.03 was gotten which implies that there is a weak negative correlation between the two hence age have little to no effect statistically on whether the loan applicant will default or not.",
        },
      ],
    },

    {
      topic: "Loan Details",
      informations: [
        {
          question:
            "What are the most common reasons for seeking a loan (e.g., debt consolidation, home improvement, small business), and which category has the highest risk?",
          answer:
            "The following are the reasons people request for loan : HOMEIMPROVEMENT, DEBTCONSOLIDATION, PERSONAL, VENTURE, MEDICAL, EDUCATION. Using Chi-square test a statistically significant assosciation (pvalue:2.173084187054017e-194) was observed between loan purpose and loan status. Residuals was calculated from the result from the chi-square and  the category the highest risk is DEBTCONSOLIDATION with a value of 14.43 followed by the medical category with a value of 10.97. The safest category are PERSONAL, VENTURE, and EDUCATION which show a statistically significant deficit.",
          imgs: [
            "/loan_visuals/loan_intent_bar_plot.png",
            "/loan_visuals/loan_count.png",
            "/loan_visuals/loan_intent_residuals.png",
          ],
        },
        {
          question:
            "Is there a clear relationship between higher interest rates and an increase in defaults?",
          answer:
            "The relationship between interest rate and loan status is a mild positive correlation with a coeficient of 0.33 hence high interest rate would cause mild increase in chance of loan default. ",
        },
      ],
    },
  ],
};

export default loanData;
