import { LoanProject } from "./CONSTANTS";

const loanData = {
  title: LoanProject,
  description:
    "The dataset includes 14 columns representing different factors influencing loan approvals and defaults",
  link: "https://www.kaggle.com/datasets/udaymalviya/bank-loan-data",
  insightSummary: `The provided analysis of the Bank Loan Dataset offers a data-driven perspective on credit risk, revealing that traditional indicators often yield unexpected results. Notably, the financial profile of a borrower shows a counterintuitive trend: defaulters possess a higher median income ($72,928) than non-defaulters ($50,629). Furthermore, while variables such as age, employment length, and education level are often scrutinized during applications, this data suggests they have a statistically negligible impact on a borrower's likelihood to repay.

Risk is more clearly defined by financial ratios and loan intent. While the typical industry threshold for Debt-to-Income (DTI) sits between 36% and 43%, predictive modeling on this dataset identifies a much stricter risk threshold of 24%. Behavioral patterns also emerge regarding the purpose of the loan; Debt Consolidation and Medical expenses represent the highest-risk categories, whereas Venture and Education loans are statistically the safest.

Finally, the analysis confirms that external costs and collateral status remain relevant. Interest rates maintain a mild positive correlation with default, suggesting that higher costs of borrowing do increase the probability of non-payment. Additionally, home ownership type serves as a moderate predictor of loan status. Collectively, these findings suggest that for this population, specific financial burdens and loan categories are more reliable predictors of risk than general demographic stability. `,
  insights: [],
};

export default loanData;
