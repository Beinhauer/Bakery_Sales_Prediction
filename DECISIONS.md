# Decisions

Newest first. One entry per decision taken at a stop point.

<!--
## YYYY-MM-DD: <short title>
**Canvas block:** <number>
**Decision:** <what was decided>
**Reason:** <why>
**Alternatives considered:** <what else, and why not>
**Decided by:** <names>
-->

## 2026-11-18: Weather inputs per horizon
**Canvas block:** 6
**Decision:** Weekly plan: observed weather for the planned days. Daily adjustment: weather forecast for tomorrow (live: from a weather website or API; training and testing: observed weather as a stand-in).
**Reason:** Team choice. Archived forecasts for 2013–2019 don't exist (Open-Meteo Historical Forecast API: from about 2021–2022; Previous Runs API: from 2024), so real forecasts can only be used in live operation.
**Risk:** Weekly-plan test results will be optimistic, because observed weather is more accurate than a 7-day forecast. Mitigation: report results with and without weather.
**Alternatives considered:** No weather in the weekly plan (honest, but leaves out a likely useful input); no weather at all.
**Decided by:** Team (via /grill-question)

## 2026-11-18: Metric, baseline and success threshold
**Canvas block:** 4
**Decision:** MAPE per product group as the main metric, plus MAE in pieces for the manager. Baseline: same weekday last week. Success: beat the baseline in every product group. Segments reported separately: weekends, days around holidays, Kiel Week, Christmas, the seasonal-bread season.
**Reason:** MAPE is the course and Kaggle metric; MAE in pieces is easier for the manager to read. Beating the baseline in every group prevents a good average from hiding a bad group.
**Alternatives considered:** MAE only; a fixed % improvement (postponed until today's practice is known); average over all groups.
**Decided by:** Team (via /grill-question)

## 2026-11-18: Audiences
**Canvas block:** 3
**Decision:** Operations manager: one-page table per day × group (turnover, pieces, range) with plain sentences for special days. Technical readers: notebooks plus README. Kaggle as a side output.
**Reason:** The manager needs something to act on; the instructors need to be able to check the method.
**Alternatives considered:** Also the bakers directly (not requested).
**Decided by:** Team (via /grill-question)

## 2026-11-18: Two planning horizons: weekly plan plus daily adjustment
**Canvas block:** 1
**Decision:** The baking amount is planned every Sunday evening (after closing) for the coming week, and can be adjusted the evening before each day (after closing) based on that day's sales and the weather.
**Reason:** This is how the client wants to plan. The weekly plan gives the bakery lead time; the daily adjustment uses the newest information.
**Alternatives considered:** Only a daily forecast made the evening before (simpler, but doesn't match the client's planning rhythm); a morning plan with adjustments during the day (no hourly data, so not possible).
**Decided by:** Team (via /grill-question)

## 2026-11-18: Expected sales with a range, not a baking amount with a margin
**Canvas block:** 1
**Decision:** We forecast the expected turnover per product group and day, with a range. The manager chooses the safety margin. A recommended baking amount (including a margin) is optional, only if the bakery provides the costs of leftovers and selling out.
**Reason:** The data records sales, not demand or leftovers; the cost of each type of error is not in the data.
**Alternatives considered:** A recommended baking amount right away (would need costs we don't have).
**Decided by:** Team (via /grill-question)

## 2026-11-18: Results in turnover and in pieces
**Canvas block:** 1
**Decision:** Results are given both as turnover and as pieces (turnover ÷ average price per product group). Both are required.
**Reason:** The data only holds turnover, but the manager bakes pieces.
**Alternatives considered:** Turnover only (doesn't match how the manager plans); share of a typical day (harder to act on).
**Risk:** Prices aren't in the data; the bakery has to provide them (see Open questions).
**Decided by:** Team (via /grill-question)

## 2026-11-18: The baking amount replaces the draft decision
**Canvas block:** 1
**Decision:** The canvas decision is "how much of each product group to bake". It replaces the README draft "inventory and staffing decisions". Staffing is parked under Open questions.
**Reason:** One canvas holds one decision; the baking amount is what the client asked about.
**Alternatives considered:** Keep both (two decisions in one canvas, with different timing and different targets).
**Decided by:** Team (via /grill-question)
