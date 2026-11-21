# Fact sheet for the operations manager

**Status:** 21.11.2026 · first results, not yet a forecast
**Based on:** canvas block 5 (`CANVAS.md`), the technical [data fact sheet](data-fact-sheet.md) and the team's analysis notebooks

<!--
HOW THIS FACT SHEET IS BUILT (for team members; this comment is not shown when the file is displayed)

Page 1 (the summary) must stay on ONE page: "In short", the overview table and the questions.
Everything else goes under "Details" (page 2 onwards).

To add your result:
1. Page 1: update your row in the overview table. "First answer" = at most 15 words
   (Yes / No / Partly + the key figure). Status values: "open" -> "in progress" -> "first answer".
2. Details: fill in your subsection under "First answers in detail", using the same parts as hypothesis 4:
   - **Answer:** one sentence that answers the question, first.
   - Key figures: at most 3 numbers, rounded, in % or turnover, always compared with something
     (e.g. "+30% compared with similar days outside Kiel Week"). A small table is fine.
   - **How sure we are:** in plain words (no p-values), e.g. "very unlikely to be chance", "only 5 cases".
   - **What this does not show:** link vs. cause, missing data, special cases.
   - **What this means for the forecast:** how the result will be used.
3. Write for the operations manager: no code, no technical terms without explanation, no recommendation
   (recommendations need the team's sign-off, canvas block 11).
4. Link your notebook in the "Source" line.
-->

## In short

- **Data:** five years of daily sales from your branch (**01.07.2013 – 31.07.2018**, 1,819 sales days) for all six product groups, plus the daily weather and the Kiel Week dates. All figures are **turnover**, not pieces.
- **Missing:** the **prices** per product group (needed to turn turnover into pieces), **holiday dates** (we add them from official sources) and **weather forecasts** (we only have the weather as it actually was).
- **Special periods are rare:** Kiel Week, Christmas and the seasonal-bread season occur only **5 times each** in the data, so results for them are less certain.

## First answers to our hypotheses

| # | Hypothesis | Owner | First answer | Status |
|---|---|---|---|---|
| 1 | Sales are higher during Kiel Week than on comparable days. | Mercy | *still open* | open |
| 2 | Public holidays (except Kiel Week) influence sales. | Phelgon | *still open* | open |
| 3 | Sales are lower during school holidays. | Romina | *still open* | open |
| 4 | Cake sales are higher on sunny days. | Britta | **Partly:** yes in autumn (+9%) and winter (+14%), not in spring and summer | first answer |

These are links found in past sales, not yet proven causes. Details from page 2.

## Questions for you

1. How do you plan the baking amounts today? (This is what our forecast has to beat.)
2. What is the average price per product group?
3. What happened on 05.05.2014? (All groups sold about 3× the normal amount after a weekend without sales.)
4. When does the seasonal-bread season start each year?
5. Which is worse for you: baking too little or too much?

<div style="page-break-after: always;"></div>

# Details

## Which data we used

| Data | What it contains | Source |
|---|---|---|
| **Sales** | Turnover per product group and day: bread, rolls, croissants, confectionery, cakes, seasonal bread | Your branch in Kiel (provided by meteolytix via the course) |
| **Weather** | Observed weather per day: temperature, cloud cover, wind, weather type (e.g. rain) | Weather data provided with the course |
| **Kiel Week** | The 9 Kiel Week days of each year | Provided with the course |

All figures are **turnover** (money taken), not pieces.

## Which period is covered

- **Sales:** 01.07.2013 – 31.07.2018, which is **1,819 days with sales**.
- **The shop had no sales on 38 days**, mostly Christmas (25./26.12.), New Year's Day, 1 May and Good Friday. We treat these as closed days, not as days with zero demand.
- **Weather:** every day from 2012 to mid-2019.
- **Kiel Week:** only **5 Kiel Weeks** (2014–2018) fall in the sales period. The same goes for Christmas and the seasonal-bread season (October to January): only 5 cases each. Results for these special periods are therefore less certain.

## What is missing or unusual

**Not in the data. We need these from you or from other sources:**
- **Prices per product group.** Without them we cannot turn turnover into pieces to bake.
- **Public and school holidays.** We add them from official sources.
- **Weather forecasts.** The data only holds the weather as it actually was. When you plan, you only have a forecast, which is less accurate, especially a week ahead. Our results with weather will therefore look somewhat better than they will in practice.
- **How much was left over, or when an item sold out.** The data shows what was sold, not what customers would have bought. On a sell-out day, demand was higher than the sales show.

**Gaps and unusual values in the data:**
- **Confectionery** has no sales on 53 days (2013–2016 only), and **seasonal bread** is only sold from October to January. We treat these as "not on offer".
- **Cloud cover is missing on 12 days.** We filled these from the neighbouring days.
- **On 05.05.2014 all groups sold about 3× the normal amount**, after a weekend with no sales. We assume three days were booked together and left this day out. *Can you confirm what happened?*
- **New Year's Eve:** cake sales are 5–7× a normal day, every year. This is real and is kept.
- **From August 2015 on**, rolls, croissants and cakes sell about 10–15% less than before, and they stay at that lower level.

## First answers in detail

### Hypothesis 1: Are sales higher during Kiel Week?

*Owner: Mercy · Source: notebook still to be linked*

*Still open.*

### Hypothesis 2: Do public holidays influence sales?

*Owner: Phelgon · Source: notebook still to be linked*

*Still open.*

### Hypothesis 3: Are sales lower during school holidays?

*Owner: Romina · Source: notebook still to be linked*

*Still open.*

### Hypothesis 4: Are cake sales higher on sunny days?

*Owner: Britta · Source: `1_DatasetCharacteristics/britta-sun.ipynb`*

A **sunny day** here is a day with little or no cloud: at most 2 on the usual 0–8 scale, where 0 = clear sky and 8 = fully overcast. About one day in four is sunny.

**Answer: Yes, in autumn and winter. Not in spring and summer.**

| Season | Typical cake turnover on a sunny day compared with a cloudy day |
|---|---|
| Spring (Mar–May) | +4%, could be chance |
| Summer (Jun–Aug) | −2%, could be chance |
| Autumn (Sep–Nov) | **+9%**, clear |
| Winter (Dec–Feb) | **+14%**, clear |

- Over the whole year the difference is only about **+5%**, because most sunny days fall in spring and summer, when the sun hardly matters for cake sales.
- **How sure we are:** in autumn and winter the difference is very unlikely to be chance. The winter figure rests on only 52 sunny days, so it is the least precise.
- **What this does not show:** that the sun is the *cause*. Sunny days may also fall more often on weekends or holidays, and we have not separated those effects yet. That is the next step.
- **What this means for the forecast:** we will test the weather as an input for the cake forecast, with an effect that can differ by season, and check whether it actually makes the forecast more accurate.
