# Data fact sheet

Produced by `/explore-data` on 2026-11-18. All numbers come from running code on the files in the [course repository](https://github.com/opencampus-sh/intro-to-data-science-and-ml/tree/main/data/bakery). The data was provided by meteolytix GmbH for the course; no license is stated. The raw data is read-only.

## 1. Sales: `umsatzdaten_gekuerzt.csv`

| Item | Value |
|---|---|
| Shape | 9,334 rows × 4 columns (`id`, `Datum`, `Warengruppe`, `Umsatz`) |
| Grain | one row = one product group on one day, **only for days with sales** |
| Keys | `id` unique; (`Datum`, `Warengruppe`) unique; `id` = `YYMMDD` + group for all 9,334 rows |
| Period | 2013-07-01 – 2018-07-31 (1,857 calendar days, 1,819 with sales; first and last months complete) |
| Missing values | none in any column |
| `Umsatz` | always > 0 (min 7.1, max 1,879.5) |

### Turnover per product group

| Group | Rows | Mean | Median | Min | Max |
|---|---|---|---|---|---|
| 1 Bread | 1,819 | 122.1 | 120.1 | 23.1 | 416.8 |
| 2 Rolls | 1,819 | 402.5 | 370.8 | 175.0 | 1,203.4 |
| 3 Croissants | 1,819 | 163.3 | 142.8 | 37.7 | 565.9 |
| 4 Confectionery | 1,766 | 88.0 | 80.0 | 27.4 | 430.5 |
| 5 Cakes | 1,819 | 276.8 | 266.0 | 121.5 | 1,879.5 |
| 6 Seasonal bread | 292 | 66.9 | 62.9 | 7.1 | 172.9 |

### Missing rows (not missing values)

- **No sales at all on 38 days.** 25.12., 26.12. and 01.01. in every year (5 each), 01.05. in 4 years, plus single days such as Good Friday. Groups 1, 2, 3 and 5 have a row on **every** one of the 1,819 sales days.
- **Confectionery (4): no row on 53 sales days**, all between 2013-07 and 2016-07; none since then. By year: 2013: 16, 2014: 23, 2015: 10, 2016: 4. The gaps cluster at 27–31.07.2013 (5 days in a row) and in December (e.g. 24.12. in 2013 and 2014; 18.–31.12.2014 with 7 gaps). There are no unusually low values next to the gaps.
- **Seasonal bread (6): 292 rows, only in Oct–Jan** (Oct 13, Nov 140, Dec 133, Jan 6). The season starts on a different day each year: 24.10.2013, 25.10.2014 (Jan 2015 days counted with that season), early Nov 2015, 03.11.2016, 30.10.2017. Inside the seasons there are 15 sales days without a seasonal-bread row (2013: 2, 2014: 6, 2015: 5, 2016: 2, 2017: 0).

### Unusual values

- **31.12. Cakes: 1,433–1,879 in all 5 years**, compared with a median of 266. This is a regular New Year's Eve peak, not an error.
- **2014-05-05 (Monday): every group about 2.5–3× normal** (Rolls 1,203 vs. about 400). The shop shows no sales on Sat 03.05. and Sun 04.05., which are normally the busiest days. Most likely three days' sales were booked on 05.05.
- Other values above Q3 + 3·IQR: Bread 8, Rolls 1, Croissants 1, Confectionery 27, Cakes 9 (most of them are 31.12. or holiday-related).

### Level over time

Mean daily turnover per August–July year (e.g. "2013" = Aug 2013 – Jul 2014):

| Year | Bread | Rolls | Croissants | Confectionery | Cakes |
|---|---|---|---|---|---|
| 2013 | 129 | 433 | 174 | 91 | 297 |
| 2014 | 125 | 437 | 175 | 88 | 297 |
| 2015 | 112 | 382 | 147 | 88 | 267 |
| 2016 | 117 | 370 | 150 | 87 | 256 |
| 2017 | 125 | 369 | 160 | 86 | 260 |

Rolls, croissants and cakes drop by about 10–15% from Aug 2015 onwards and stay at the lower level. Summer is much higher for rolls (July 2013: about 650–870 per day).

Mean daily total over all groups, Monday to Sunday: 994, 965, 957, 995, 1,008, 1,235, 1,272.

## 2. Weather: `wetter.csv`

| Item | Value |
|---|---|
| Shape | 2,601 rows × 5 columns |
| Grain | one row = one day; `Datum` unique |
| Period | 2012-01-01 – 2019-08-01 (also covers the Kaggle test year) |
| Missing days | 169 in total (2012: 33, 2013: 120, 2016: 1, 2017: 2, 2018: 12, 2019: 1). **Inside the sales period only 3 sales days have no weather row:** 2016-12-11, 2017-10-04, 2017-10-05. |
| `Bewoelkung` | 0–8 octas, integers. 10 missing values, **all in one block: 30.10.–08.11.2017** |
| `Temperatur` | −10.2 to 32.7 °C, none missing |
| `Windgeschwindigkeit` | 3–35 m/s, integers, none missing |
| `Wettercode` | WMO codes 0–95, 41 distinct values (most common: 61 slight rain, 21, 0, 10). **669 missing overall, 463 (25%) in the sales period** |

**The missing `Wettercode` values are not random.**
- On days without a code the weather is clearer and warmer: mean cloud cover 2.9 vs. 5.3 octas, temperature 16.1 vs. 10.8 °C. 125 of the 451 days without a code (but with a cloud value) are completely clear (0 octas).
- The share without a code **falls over time**: 2013: 36%, 2014: 35%, 2015: 27%, 2016: 24%, 2017: 18%, 2018: 8%. So the recording practice changed over the years.

These are **observed** values, not forecasts.

## 3. Kiel Week: `kiwo.csv`

- 72 rows, `KielerWoche` is always 1; `Datum` unique. Each year has 9 consecutive days (Saturday to Sunday of the following week), 2012–2019.
- Kiel Week 2013 (22.–30.06.2013) is **before** the start of the sales data. **The sales period therefore contains only 5 Kiel Weeks (2014–2018), 45 days**, all with sales.
- Rolls average 539 on Kiel Week days vs. 399 otherwise (no other effects removed).

## 4. Joins

- Sales ← weather (left join on `Datum`): 9,334 rows before and after. 16 rows (the 3 days above) get no weather values.
- ← Kiel Week (left join on `Datum`): 9,334 rows; 223 rows with `KielerWoche = 1`; all other rows are missing and must be set to 0.
- 98% of the weather days in the sales period match a sales day; the rest are the 38 no-sale days.

## 5. Not in the data

- **Prices / pieces**: not available (needed for canvas question 3).
- **Public and school holidays**: not in the data, but listed as allowed inputs in canvas block 6. They need an external source.
- **Weather forecasts**: none; no archive exists for 2013–2019.
- **Sales for the Kaggle test year (Aug 2018 – Jul 2019)**: held back; it can only be scored on Kaggle.
