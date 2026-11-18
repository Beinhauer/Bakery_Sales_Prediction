# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| `Umsatz` (turnover) | Money taken for a product group on one day | Currency units (currency not stated) | **Not pieces.** Recorded sales, not demand: on a sell-out day, demand was higher. |
| `Warengruppe` (product group) | Product category | 1 Bread, 2 Rolls, 3 Croissants, 4 Confectionery, 5 Cakes, 6 Seasonal bread | 6 is only sold Oct–Jan; 4 has no row on 53 days. |
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
