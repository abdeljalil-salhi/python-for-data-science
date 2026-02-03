import sys
import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Load two datasets (GDP and life expectancy),
    extract data for year 1900 and create a scatter plot:
    Life Expectancy vs Gross Domestic Product in 1900
    """
    life_path = "life_expectancy_years.csv"
    gdp_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"

    gdp_df = load(gdp_path)
    life_df = load(life_path)

    if gdp_df is None or life_df is None:
        print("Dataset failed to load.", file=sys.stderr)
        sys.exit(1)

    year = "1900"
    if year not in gdp_df.columns or year not in life_df.columns:
        print(
            f"Error: Year '{year}' not found in one or both datasets.",
            file=sys.stderr,
        )
        sys.exit(1)

    # keep only year's column from each
    merged = pd.merge(
        life_df[["country", year]],
        gdp_df[["country", year]],
        on="country",
        how="inner",
        suffixes=("_life", "_gdp"),
    )

    merged = merged.rename(
        columns={
            f"{year}_life": "Life Expectancy",
            f"{year}_gdp": "Gross Domestic Product",
        },
    )

    merged["Life Expectancy"] = pd.to_numeric(
        merged["Life Expectancy"],
        errors="coerce",
    )
    merged["Gross Domestic Product"] = pd.to_numeric(
        merged["Gross Domestic Product"],
        errors="coerce",
    )

    merged = merged.dropna(
        subset=["Life Expectancy", "Gross Domestic Product"],
    )

    if merged.empty:
        print(
            f"No valid data available for year {year} after cleaning.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Number of countries with data in {year}: {len(merged)}")

    plt.figure(figsize=(10, 7))
    plt.scatter(
        merged["Gross Domestic Product"],
        merged["Life Expectancy"],
        s=60,
        alpha=0.7,
        color="#1f77b4",
        edgecolors="white",
        linewidth=0.5,
    )

    plt.title(
        f"Life Expectancy vs Gross Domestic Product in {year}",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Gross Domestic Product", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)

    plt.xscale("log")  # 300 -> 1k -> 10k
    plt.gca().get_xaxis().set_major_formatter(
        plt.FuncFormatter(
            lambda x, _: f"{x/1000:.0f}k" if x >= 1000 else f"{x:.0f}",
        )
    )
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} – {e}", file=sys.stderr)
        sys.exit(1)
