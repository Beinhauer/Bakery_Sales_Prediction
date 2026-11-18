# Agentic Data Science Canvas

**Project:** 13_RBMP
**Team:** <!-- names: still to be filled in by the team -->
**Version:** 2026-11-18 (blocks 1–4 and 6 confirmed by the team)

> Owners: 👤 human decides · 🤖 agent drafts, human approves.
> Keep each block short. Details go in linked files; decisions go in `DECISIONS.md`.

---

## Problem

### 1. Decision 👤
<!-- Who decides what, when and how often? What happens today without this analysis? -->
The bakery's **operations manager** decides **how much of each product group (1–6) to bake** at the one branch in Kiel. Two steps:
- **Weekly plan:** every Sunday evening, after closing, for each day of the coming week (1–7 days ahead).
- **Daily adjustment:** the evening before each day, after closing, the plan for tomorrow may be changed based on today's sales and the weather.

Our answer: **expected turnover per product group and day, with a range**, plus the **same in pieces** (turnover ÷ average price per group, prices from the bakery). The safety margin is the manager's choice. A recommended baking amount that already includes a margin is optional, if the bakery provides the cost of leftovers and of selling out.
Today's practice (the baseline to beat) is unknown → Open questions.

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
1. **Weekly plan:** What turnover will each product group have on each day of the coming week (1–7 days ahead)? *Can answer:* weekday, season, holiday, Kiel Week and weather patterns. *Cannot answer:* promotions or price changes (not in the data); true demand on sell-out days; Christmas, Kiel Week and the seasonal-bread season rest on **only 5 cases each**.
2. **Daily adjustment:** How much better does tomorrow's forecast get with today's sales and tomorrow's weather forecast? This tells us whether the adjustment is worth the effort. *Cannot answer:* the effect of *real* forecasts, because archived forecasts only exist from about 2021 (we test with observed weather instead, see block 6).
3. **Pieces:** How many pieces per product group is that? Needs average prices from the bakery (Open questions).

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->
- **Operations manager** (decision-maker): one-page table per day × product group with turnover, pieces and range, plus one plain sentence per special day (e.g. "Kiel Week: Rolls about +30%").
- **Technical readers** (course instructors, team): notebooks plus README with the metrics per product group and the comparison against the baseline.
- **Kaggle competition** (side output): turnover forecast for 01.08.2018–31.07.2019 in the required `id` format.

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->
- **Main metric:** MAPE per product group (course and Kaggle). **For the manager:** MAE in pieces per product group.
- **Baseline:** same weekday last week (stand-in until we know today's practice; works for both horizons).
- **Good enough:** beats the baseline in **every** product group, not just on average. A % threshold follows once today's practice is known.
- **Which error is worse** (too little vs. too much): unknown; treated as equal for now. Open question for the manager.
- **Segments reported separately:** Saturdays and Sundays, days around public holidays, Kiel Week, Christmas, the seasonal-bread season (with the 5-case limit stated).

---

## Data and method

### 5. Data 🤖
<!-- Sources, unit of observation, period covered, keys, known gaps. Link the data fact sheet. -->

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
- **Weekly plan (Sunday evening, after closing):** all sales up to and including that Sunday; the calendar (weekday, public and school holidays, Kiel Week dates); weather: **observed weather** for the planned days (team decision, see risk).
- **Daily adjustment (evening before, after closing):** the same, plus that day's sales and the weather forecast for tomorrow. Live use: a forecast from a weather website or API. Training and testing: observed weather as a stand-in, because no archived forecasts exist for 2013–2019.
- **Not allowed:** anything from the day being forecast (e.g. other groups' sales that day).
- ⚠️ **Risk:** observed weather 1–7 days ahead is more accurate than any real 7-day forecast, so test results for the weekly plan will look **better than in real use**. Results are reported with and without weather, so the size of this effect is visible.

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it. -->
- Team members and responsibilities: the team fills in the header and the `## Team` section of `AGENTS.md`.
- **How does the manager plan the baking today?** (same weekday last week, gut feeling, a fixed plan per weekday, …). This defines the baseline. Resolves: the team asks the operations manager. Until then: "same weekday last week" as a stand-in.
- **Average price per product group** (needed to convert turnover into pieces; not in the data). Resolves: the team asks the bakery. Without it, the piece analysis is not possible.
- **Cost of leftovers vs. cost of selling out**, per group (only needed for the optional recommended baking amount). Resolves: the team asks the bakery.
- **Which error costs more, baking too little or too much?** (maybe per product group). Resolves: the team asks the operations manager. Until then: both treated as equal.
- **How to split the data** into training, validation and test (by time; the Kaggle year has no sales for us to check against). Resolves: the team, before any modelling.
- **Staffing decisions** (from the earlier README draft): parked, possibly a later decision. Resolves: the team.

## Decision log
See `DECISIONS.md`.
