import { RetailProject } from "./CONSTANTS";

const retailData = {
  title: RetailProject,
  description:
    "This Online Retail II data set contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011.The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.",
  link: "https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci",
  insightSummary: `The Online Retail II Dataset provides a snapshot of a UK-based wholesaler's performance, identifying clear peaks in demand and specific product dominance. The WHITE HANGING HEART T-LIGHT HOLDER is the most frequently purchased item, appearing in 5,783 transactions, while WORLD WAR 2 GLIDERS ASSTD DESIGNS leads in total quantity sold at 110,249 units.
Seasonally, November stands out as the highest volume month with over 162,000 transactions, likely driven by holiday gift-ware demand. Weekly operations peak on Sundays at 12:00 PM, marking the busiest window for sales activity. `,
  insights: [
    {
      topic: "Product Performance",
      informations: [
        {
          question:
            " Which products are the best-sellers by quantity or frequency?",
          answer:
            "By frequency WHITE HANGING HEART T-LIGHT HOLDER with a value of 5783 is the highest while GREEN CHENILLE SHAGGY C/COVER with a value of 1 is the lowest. By quantity WORLD WAR 2 GLIDERS ASSTD DESIGNS  with a value of 110249 is the highest while I LOVE LONDON MINI RUCKSACK with a value of 1 is the lowest.",
          imgs: [
            "/retail_visuals/top_product_performance_by_quantity.png",
            "/retail_visuals/top_product_performance_by_freq.png",
          ],
        },
      ],
    },

    {
      topic: "Sales And Temporal Trends",
      informations: [
        {
          question: "Which months see the highest transaction volume?",
          answer:
            "The month with the highest transaction volume is November with a transaction volume of 162339.",
          imgs: ["/retail_visuals/monthly_transaction_volume.png"],
        },
        {
          question:
            "What are the busiest days of the week and hours of the day for sales?",
          answer:
            "The busiest days of the week and hours of the day for sales is Sunday at 12:00.",
          imgs: ["/retail_visuals/busiest_hour.png"],
        },
      ],
    },
  ],
};

export default retailData;
