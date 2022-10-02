# Recession Yes/No

## Exeucitve Summary

***
[[Goal](#goal)]
[[Project Descriptions](#project_descriptions)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
[[Steps to Reproduce](#reproduce)]
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
- The project will explore three different acquired datasets
- The project will then create a classification model based on the best defined recession.
- Document the conclusion, key takeaways, and recommendations.

***
## Term Defination
- Monetary Policy: the actions that a nation's central bank takes to control the money supply in an economy with the goal of helping grow a slowing economy or to contract an economy that is growing too fast.
[[Back to the Background](#background)]






[^1]: https://www.economist.com/the-economist-explains/2022/08/12/what-is-a-recession
[^2]: https://www.bloomberg.com/news/articles/2022-07-12/no-us-recession-until-obscure-panel-of-eggheads-says-it-is-so?sref=6JSdcyMu
[^3]: https://www.conference-board.org/topics/recession/US-recession-probabilities-reach-96-percent