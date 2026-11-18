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

Hypotheses:
1. Average daily bakery sales are higher during Kiel Week than during comparable days outside the festival periode. (M)
2. Public holidays (except for Kiel week) influence daily sales. (P)
3. Sales are lower during school holidays. (R)
4. On sunny days cake sales are higher. (B)

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
Details: [`docs/data-fact-sheet.md`](docs/data-fact-sheet.md).
- **Sales** (meteolytix, via the course): one row per day × product group, only on days with sales; 2013-07-01 – 2018-07-31; 9,334 rows; key (`Datum`, `Warengruppe`) unique; no missing values. 38 days with no sales (mostly holidays); confectionery has no row on 53 days (2013–2016 only); seasonal bread only Oct–Jan (292 rows). The 2014-05-05 value is probably 3 days booked together. Level about 10–15% lower from Aug 2015.
- **Weather**: one row per day, 2012-01-01 – 2019-08-01; 3 sales days have no row; cloud cover missing 30.10.–08.11.2017; `Wettercode` missing on 25% of days, **not at random** (clearer, warmer days, and less often in later years). Observed values only.
- **Kiel Week**: 9 days per year; **only 5 Kiel Weeks (2014–2018) fall inside the sales period**.
- **Missing for our questions:** prices (for pieces), public and school holidays (external source needed), weather forecasts.

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
- **Weekly plan (Sunday evening, after closing):** all sales up to and including that Sunday; the calendar (weekday, public and school holidays, Kiel Week dates); weather: **observed weather** for the planned days (team decision, see risk).
- **Daily adjustment (evening before, after closing):** the same, plus that day's sales and the weather forecast for tomorrow. Live use: a forecast from a weather website or API. Training and testing: observed weather as a stand-in, because no archived forecasts exist for 2013–2019.
- **Not allowed:** anything from the day being forecast (e.g. other groups' sales that day).
- ⚠️ **Risk:** observed weather 1–7 days ahead is more accurate than any real 7-day forecast, so test results for the weekly plan will look **better than in real use**. Results are reported with and without weather, so the size of this effect is visible.

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->
All with reasons in `DECISIONS.md` (2026-11-18).
- **Join:** left join of weather and Kiel Week onto sales by date; missing Kiel Week = 0.
- **Missing rows = not on offer, not 0:** leave out the 38 no-sale days, the 53 days without confectionery and the 15 in-season days without seasonal bread. Seasonal bread is only forecast when it's on offer (known from the manager's plan).
- **Unusual values:** keep the New Year's Eve cake peaks (New Year's Eve becomes an input). Remove 2014-05-05 from training and evaluation (probably 3 days booked together; manager asked).
- **Level shift from Aug 2015:** all years plus a trend or year input by default; validation decides whether training from Aug 2015 only is better.
- **Weather:** `Wettercode` → precipitation yes/no (missing = no). Fill the 3 missing weather days and 10 missing cloud values from neighbouring days.
- **Holidays:** public holidays from the `holidays` package (Schleswig-Holstein); school holidays from a hand-made CSV (still to build).
- **Split (provisional):** training Jul 2013 – Jul 2017 · validation Aug 2017 – Jul 2018 · test = Kaggle year, used once.

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
- **What happened on 2014-05-05?** (no sales on 03./04.05., then about 3× normal). Resolves: the team asks the manager. Until then the day is removed.
- **Start of the seasonal-bread season** each year (needed as known-in-advance input). Resolves: the team asks the manager.
- **School holiday CSV for Schleswig-Holstein 2013–2019**: still to be built from the official dates. Resolves: the team (who?).
- **Split:** provisional (block 7); the team may change it before modelling starts.
- **Staffing decisions** (from the earlier README draft): parked, possibly a later decision. Resolves: the team.

## Decision log
See `DECISIONS.md`.
