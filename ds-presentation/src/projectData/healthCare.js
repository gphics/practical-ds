import { HealthCareProject } from "./CONSTANTS";

const healthcareData = {
  title: HealthCareProject,
  description:
    "This synthetic healthcare dataset has been created to serve as a valuable resource for data science, machine learning, and data analysis enthusiasts. It is designed to mimic real-world healthcare data, enabling users to practice, develop, and showcase their data manipulation and analysis skills in the context of the healthcare industry.",
  link: "https://www.kaggle.com/datasets/prasad22/healthcare-dataset",
  insightSummary: `An analysis of a synthetic healthcare dataset indicates a lack of expected real-world medical correlations across several categories. Key findings include no significant association between age or gender and specific conditions, an average billing amount of $25,539 without correlation between insurance providers and costs or stay length, and Aspirin being the most frequent medication with no impact on admission duration. The analysis also found no link between medical conditions and the length of hospital stays, even though many patients had maximum 30-day stays.`,
  insights: [
    {
      topic: "Demographics",
      informations: [
        {
          question: `Does a specific age group or gender correlate with higher rates of certain conditions (e.g., are older patients more frequently admitted for "Diabetes" or "Hypertension")?`,
          answer:
            "Using chi-square test and anova, no significant assosciation was discovered between age-group/age vs medical contion or gender vs medical condition. According to domain knowledge there is a significant relationship between age or gender vs medical conditions (Arthritis, Asthma, Cancer, Diabetes, Hypertension, Obesity) but this dataset did not provide such information. At some point, I perform random sampling on the data hoping I can get a different opinion but the result was the same. Even the bar plot for the three features shows no significant information.",
          imgs: [
            "/health_care_visuals/age_group_vs_med_cond1.png",
            "/health_care_visuals/age_group_vs_med_cond2.png",
            "/health_care_visuals/gender_vs_med_cond.png",
          ],
        },
      ],
    },

    {
      topic: "Financial Analysis",
      informations: [
        {
          question:
            "What is the distribution of Billing Amounts? Are certain Insurance Providers (e.g., Cigna vs. Medicare) associated with more expensive treatments or longer stays?",
          answer: `The billing amounts data is not normally distributed and not skewed. The average amount spent on treatment was 25539 dollars. Using kruskal wallis test to determine the assosciativity between insurance providers and billing amount or admission duration, it was confirmed that there is no assosciation between them whatsover.`,
          imgs: ["/health_care_visuals/billing_amnt_dist.png"],
        },
      ],
    },
    {
      topic: "Medication Pattern",
      informations: [
        {
          question: `For a specific condition like "Asthma," what is the most frequently prescribed Medication, and does it impact the length of the stay?`,
          answer:
            "Aspirin is the most frequently used drug for each of the medical condition. There is no significant assosciation between the medication used and admission duration as verified by kruskal wallis test.",
        },
      ],
    },
    {
      topic: "Operational Efficiency",
      informations: [
        {
          question:
            "How many Hospitals or Doctors have the longest average admission durations, and is there a correlation with the Medical Condition being treated?",
          answer: `There are 39876 hospitals and 1186 of them have the highest admission duration of 30 days.There are  40341 doctors and 1131 of them have the highest admission duration of 30 days. Using kruskal-wallis test because admission duration is not normally distributed, a pvalue of 0.32 was gotten hence there is no correlation between admission duration and medical condition.`,
        },
      ],
    },
  ],
};

export default healthcareData;
