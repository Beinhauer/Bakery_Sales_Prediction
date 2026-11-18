# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| `Umsatz` (turnover) | Money taken for a product group on one day | Currency units (currency not stated) | **Not pieces.** Recorded sales, not demand: on a sell-out day, demand was higher. |
| `Warengruppe` (product group) | Product category | 1 Bread, 2 Rolls, 3 Croissants, 4 Confectionery, 5 Cakes, 6 Seasonal bread | 6 is only sold Oct–Jan; 4 has no row on 53 days. |
| `id` | Row key of the sales data | `YYMMDD` + group, e.g. `1307011` | Also the Kaggle format. Not a feature. |
| `Datum` | Date | `YYYY-MM-DD` | Join key for all files. |
| No-sale day | Date inside the sales period with no row for any group (38 days, mostly holidays) | | Shop presumably closed; not a day with 0 sales. |
| `Bewoelkung` (cloud cover) | Mean cloud cover of the day | Octas, 0 = clear … 8 = overcast | Missing 30.10.–08.11.2017. |
| Sunny day | Day with `Bewoelkung` ≤ 2 | 0/1 | Team definition for hypothesis 4. Based on observed cloud cover; not defined on the 10 days without cloud cover (30.10.–08.11.2017) until they are filled. |
| `Temperatur` (temperature) | Mean temperature of the day | °C | Observed. |
| `Windgeschwindigkeit` (wind speed) | Mean wind speed of the day | m/s | Observed. |
| `Wettercode` (weather code) | WMO present-weather code | 0–99 | Missing on 25% of sales-period days; missing means clearer/warmer weather and is rarer in later years. |
| `KielerWoche` (Kiel Week) | 1 on the 9 Kiel Week days | 0/1 | The file only lists Kiel Week days; others must be set to 0. Only 5 Kiel Weeks (2014–2018) fall in the sales period. |
| Season (seasonal bread) | Period in which group 6 is on offer | Oct–Jan | Start date differs per year (24.10. – 03.11.). |
| Aug–Jul year | Year running from 1 August to 31 July, named after its start year | | Matches the Kaggle test year (Aug 2018 – Jul 2019). |
| Pieces | Number of items to bake | Count | = turnover ÷ average price per product group. Prices come from the bakery, not the data. |
| Expected sales | Our forecast of turnover (and pieces) per product group and day, with a range | Turnover / pieces | Contains no safety margin; the manager adds that. |
| Weekly plan | Baking plan made Sunday evening, after closing, for each day of the coming week | Horizon 1–7 days | |
| Daily adjustment | Change to tomorrow's plan, made the evening before, after closing | Horizon 1 day | Can use that day's sales and the weather forecast. |
| MAPE | Mean absolute percentage error: on average, by how many % the forecast is off | % | Main metric, per product group. Becomes very large on days with small turnover. |
| MAE | Mean absolute error: average size of the error | Pieces (for the manager) or turnover | |
| Observed weather | Weather as measured on the day (`wetter.csv`) | | Not available ahead of time; used as a stand-in for a forecast. |
| Weather forecast | Weather predicted for a future day | | Only usable in live operation; no archive for 2013–2019. |
| Leakage boundary | The list of inputs allowed at planning time (canvas block 6) | | Every feature must be on this list. |
| Baseline | The method our forecast has to beat | | Ideally the manager's current practice; stand-in: same weekday last week. |
