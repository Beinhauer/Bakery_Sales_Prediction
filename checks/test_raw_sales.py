"""Checks 1-4 (canvas block 8): facts about the raw sales data that must stay true.

If one of these fails, the source file has changed or was loaded incorrectly.
Run all checks with: uv run pytest checks
"""

import pandas as pd
import pytest

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"


@pytest.fixture(scope="module")
def sales():
    return pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv", parse_dates=["Datum"])


def test_one_row_per_date_and_group(sales):
    """Check 1: no duplicates, and id = YYMMDD + product group."""
    assert not sales.duplicated(["Datum", "Warengruppe"]).any()
    assert sales["id"].is_unique
    expected_id = (sales["Datum"].dt.strftime("%y%m%d") + sales["Warengruppe"].astype(str)).astype(int)
    assert (sales["id"] == expected_id).all()


def test_valid_values(sales):
    """Check 2: groups only 1-6, turnover always > 0, no missing values."""
    assert set(sales["Warengruppe"].unique()) <= {1, 2, 3, 4, 5, 6}
    assert (sales["Umsatz"] > 0).all()
    assert not sales.isna().any().any()


def test_complete_period(sales):
    """Check 3: dates from 2013-07-01 to 2018-07-31, exactly 1,819 days with sales."""
    assert sales["Datum"].min() == pd.Timestamp("2013-07-01")
    assert sales["Datum"].max() == pd.Timestamp("2018-07-31")
    assert sales["Datum"].nunique() == 1819


def test_seasonal_bread_only_in_season(sales):
    """Check 4: product group 6 (seasonal bread) only from October to January."""
    months = sales.loc[sales["Warengruppe"] == 6, "Datum"].dt.month
    assert months.isin([10, 11, 12, 1]).all()
