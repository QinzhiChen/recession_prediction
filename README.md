# Recession Yes/No

## Exeucitve Summary
- This project focuses on three different methods to define the recession. The exploration found that it is unjust to say that the United States is in recession solely based on two consecutive declines in the GDP or high-interest rates. The project found that NBER used many different data to determine whether the United States is in a recession. The project retrieved as much data as possible, conducted several explorations, and created a machine learning model to predict the next recession. The model achieved 96% accuracy and a 100% recall rate. The next step is to capture more data that is not available. 

***
[[Goal](#goal)]
[[Project Descriptions](#project-descriptions)]
[[Background](#background)]
[[Planning](#planning)]
[[Data Dictionary](#data-dictionary)]
[[Recommendation, Conclusion, and Next Step](#recommendation,-conclusion,-and-next-step)]
[[Steps to Reproduce](#steps-to-reproduce)]
[[Term Defination](#term-defination)]
[[Reference](#reference)]
___

## Goal
- This project aims to create a Machine Learning model to predict whether the United States will be in a recession.

***
## Project Descriptions
- What is the recession? The Economist published a recent article stating, "Recession is contested...Wikipedia editors cannot agree on the definition of 'recession'. Last month the site barred new and unregistered users from editing its page on the subject after a fierce dispute over the claim that two consecutive quarters of falling GDP indicates a recession". I believe this definition is not quite right.[^1]
- The overall project will examine three different methods to define what the recession is.
- Currently, "it typically takes the National Bureau of Economic Research about a year to decide on a recession call, though some decision have been made in a few months while others have taken almost twice as long." The machine learning model can be created from the best numerical method to predict the next recession and ultimately hope this can shorten the process.[^2]
- However, this machine learning model is not meant to challenge the Markov-switching dynamic regression model, which gives a recession probability to the current market. The classification model this project will create is for identifying whether the next estimated numerical data can put the United States into recession.

***
## Background
- After World War II, the United States lifted the price control, resulting in excessive money left to spend. In less than two years, a more than 20% inflation at its peak happened. The end of WWII brought a new economic downturn to the nation. In 2020, the global pandemic created a traumatic event for the whole world, people lost their jobs, and the unemployment rate jumped from 3.6% to 13.0%. The federal reserve took some emergency procedures, including reducing the interest rate to almost 0% and ease the [monetary policies](#term-defination); similarly, people saved excessive money during the pandemic. In 2022, the ending of the pandemic era brought in similar spending alike in 1946. The current inflation rate is 8.26%, which concerns the United States' long-term economic health.
- At this moment, some media believe there will be a recession by the end of this year. "The Conference Board predicts a 96 percent likelihood of a recession in the US within the next 12 months, based on their probability model." Which comes to the reason for this project, that general common knowledge believes that the two consecutive Gross Domestic Production declines are recession?[^3]

***
## Panning
- The project will have three different acquisitions of different datasets
    - Use the GDP-based method to collect unemployment rate, industrial production, real gdp, gdp, and recession dates.
    - Use general economy data such as CPI, money supply, Core CPI, GDP deflator, unemployment rate, industrial production, PCE to determine the recession.
    - Use NBER data [^4]
- The project will explore three different acquired datasets and answer questions.
- The project will then create a classification model based on the best defined recession.
- Document the conclusion, key takeaways, and recommendations.

***
## Initial Question
- Whether we can determine the recession solely based on the GDP
- Whether we can determine the recession solely based on the interest rate
- Whether we can find correlation from the NBER dataset

***
## Data Dictionary
- First dataset

| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| unem | unemployment rate| float |
| indpro | industrial production | float |
| rgdp | real gross domestic product | float |
| gdp | gross domestic product | float |
| is_recession | whether the United States is in recession | float |
| gdp_pct_change | percentage of the gdp change  | float |

- Second dataset

| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| cpi | consumer price index| float |
| moneysup | current money supply | float |
| corecpi |core consumer price index  |float |
| gdp_def | gross domestic product deflator | float |
| unem |unemployment rate | float |
| indpro |industrial production | float |
| rgdp |real gross domestic production| float |
| gdp |gross domestic production| float |
| rate | interest rate | float |
| is_recession | whether the United States is in recession | float |
| gdp_pct_change | percentage of the gdp change  | float |
| monp_pct_change |money supply percentage change| float |

- Third dataset

| Feature | Definition | Data Type |
| ----- | ----- | ----- |
| rgdi | real gross domestic income| float |
| rmanufacture | Real manufacturing and trade sales associated with change from NAICS to SIC  | float |
| indpro | Index of industrial production |float |
| personincome |  Real personal income less transfers | float |
| weeklyprivate |Aggregate weekly hours index in total private industries  | float |
| payroll |Payroll survey employment | float |
| empp |Household survey employment| float |
| gdp |gross domestic production| float |
| is_recession | whether the United States is in recession | float |
| gdp_pct_change | percentage of the gdp change  | float |
| gdi_pct_change |gross domestic income percentage change| float |
| manu_pct_change |  Real manufacturing and trade sales associated with change from NAICS to SIC percentage change over time | float |
| indpro_pct_change | industrial production percentage change | float |
| payroll_pct_change | payroll percentage change | float |
| empp_pct_change | household survey employment percentage change | float |

***
# Recommendation, Conclusion, and Next Step

## Recommendation
- We should not believe there is recession based on single data
- The RandomForestClassifer can be used for our prediction

## Conclusion 
- In general, the data did show favor for two consecutive declines in GDP to call it a recession.
- The United States NBER used a different formula to call the recession, it could take a few months for NBER to announce it.
- The high unemployment rate doesn't mean there is a recession.
- The United States does not use the GDP-based formula to determine the recession, but an official determination came from NBER. Therefore, the hypothesis t-test can pass the null hypothesis.
- the percentage change has negative correlation with recession
- This is good data to use for the classification prediction because the United States is using those data to announce the recession

## Next Step
- Deploy the machine learning model
- Improvise the machine learning model
- Collect missing data

***
## Steps to Reproduce
- request a API via [FRED](https://fred.stlouisfed.org/docs/api/fred/)
- Create your own env file
- install FRED libary
- Download all files on this repo [github](https://github.com/QinzhiChen/individual_project)
- Enjoy!

***
## Term Defination
- Monetary Policy: the actions that a nation's central bank takes to control the money supply in an economy with the goal of helping grow a slowing economy or to contract an economy that is growing too fast.
[[Back to the Background](#background)]

- Inflation is caused when the money supply in an economy grows at faster rate than the economy’s ability to produce goods and services. In our auction economy the production of goods and services was unchanged, but the money supply grew from round one to round two. Because the money supply grew, and the output of goods and services did not grow, our economy experienced inflation.
[[Back to the Final NoteBook](https://github.com/QinzhiChen/individual_project/blob/main/final%20notebook.ipynb#general_data_based_wrangle)]

- GDP Deflator: A measure of inflation in the prices of goods and services produced in the United States, including exports. The gross domestic price deflator closely mirrors the GDP price index, although they are calculated differently. The GDP deflator is used by some firms to adjust payments in contracts. [^6]
[[Back to the Final NoteBook](https://github.com/QinzhiChen/individual_project/blob/main/final%20notebook.ipynb#general_data_exploration)]


## Reference

[^1]: https://www.economist.com/the-economist-explains/2022/08/12/what-is-a-recession
[^2]: https://www.bloomberg.com/news/articles/2022-07-12/no-us-recession-until-obscure-panel-of-eggheads-says-it-is-so?sref=6JSdcyMu
[^3]: https://www.conference-board.org/topics/recession/US-recession-probabilities-reach-96-percent\
[^4]: https://www.nber.org/news/business-cycle-dating-committee-announcement-september-20-2010
[^5]: https://www.stlouisfed.org/education/feducation-video-series/episode-1-money-and-inflation
[^6]: https://www.bea.gov/data/prices-inflation/gdp-price-deflator
