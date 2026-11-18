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

## 2026-11-18: Time-based split (provisional)
**Canvas block:** 7
**Decision:** Training Jul 2013 – Jul 2017; validation Aug 2017 – Jul 2018; test = Kaggle year Aug 2018 – Jul 2019, used once at the end. Provisional: the team may change it before modelling starts.
**Reason:** Strictly in time order (no future information in training); validation covers a full year with one Christmas and one Kiel Week.
**Limit:** Validation contains only 1 Christmas and 1 Kiel Week; training only 4 Kiel Weeks.
**Alternatives considered:** Several rolling validation years (more robust, more work).
**Decided by:** Team (via /explore-data)

## 2026-11-18: Public and school holidays from external sources
**Canvas block:** 7
**Decision:** Public holidays from the Python package `holidays` (`Germany(subdiv="SH")`, version 0.109). School holidays for Schleswig-Holstein 2013–2019 from a hand-made CSV in the repo, built from the official dates.
**Reason:** Block 6 lists holidays as allowed inputs, but the data doesn't contain them. The package correctly includes Reformation Day (31.10.2017 one-off, from 2018 permanently).
**Alternatives considered:** No holidays (leaves out a strong driver); a holiday API (adds a dependency at run time).
**Decided by:** Team (via /explore-data)

## 2026-11-18: Weather gaps and weather code
**Canvas block:** 7
**Decision:** `Wettercode` is turned into "precipitation yes/no"; a missing code counts as "no". The 3 sales days without a weather row and the 10 days without cloud cover (30.10.–08.11.2017) are filled from the days just before and after the gap.
**Reason:** Missing codes come with clearer, warmer weather, and their share falls from 36% (2013) to 8% (2018); keeping "missing" as a category would teach the model the change in recording practice. Only 13 days need filling.
**Alternatives considered:** Drop `Wettercode`; keep the codes with "missing" as a category; drop the rows with gaps.
**Decided by:** Team (via /explore-data)

## 2026-11-18: Level shift from August 2015
**Canvas block:** 7
**Decision:** Default: use all years and add a time trend or year input. Validation decides whether training only from Aug 2015 works better.
**Reason:** Rolls, croissants and cakes are about 10–15% lower from Aug 2015 onwards, but the older years contain Christmas and Kiel Week cases we can't afford to lose (only 5 of each).
**Alternatives considered:** Train only from Aug 2015 (fewer special-day cases).
**Decided by:** Team (via /explore-data)

## 2026-11-18: Unusual values: New Year's Eve kept, 2014-05-05 removed
**Canvas block:** 7
**Decision:** The New Year's Eve cake peaks (all 5 years) stay in the data; New Year's Eve becomes a calendar input. 2014-05-05 is removed from training and evaluation, unless the manager gives a different explanation.
**Reason:** New Year's Eve is a real, recurring peak. 2014-05-05 is about 2.5–3× normal in every group right after a weekend with no sales; most likely 3 days were booked together, and their real spread is unknown.
**Alternatives considered:** For 2014-05-05: split evenly over 03.–05.05. (makes up numbers); keep it (false Monday spike).
**Decided by:** Team (via /explore-data); waiting for the manager's answer

## 2026-11-18: Missing rows are "not on offer", not zero
**Canvas block:** 7
**Decision:** The 38 no-sale days, the 53 days without confectionery and the 15 in-season days without seasonal bread are left out; they are not set to 0. Seasonal bread is only forecast on days it's on offer; "on offer" is known in advance from the manager's plan.
**Reason:** The neighbouring days show no sign of zero demand; the manager knows closed days and the offer. Zeros would also break MAPE.
**Alternatives considered:** Set to 0; fill in estimates.
**Decided by:** Team (via /explore-data)

## 2026-11-18: Joining sales, weather and Kiel Week
**Canvas block:** 7
**Decision:** Left join of weather and Kiel Week onto sales by `Datum`; missing Kiel Week values become 0.
**Reason:** Keeps every sales row (row count checked: 9,334 before and after).
**Alternatives considered:** Inner join (would lose the 16 rows on the 3 days without weather).
**Decided by:** Team (via /explore-data)

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
