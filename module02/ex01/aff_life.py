import sys
import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Load life expectancy dataset and plot the curve for Morocco.
    """
    dataset_path = "life_expectancy_years.csv"

    df = load(dataset_path)
    if df is None:
        sys.exit(1)

    country_name = "Morocco"

    if country_name not in df["country"].values:
        print(
            f"Error: Country '{country_name}' not found in the dataset.",
            file=sys.stderr,
        )
        sys.exit(1)

    country_data = df[df["country"] == country_name].iloc[0]

    years = country_data.index[1:]  # skip the 'country' column
    expectancy = country_data.values[1:]  # skip the country name

    # Convert years to numeric (they are strings like "1800", "1801", ...)
    years = pd.to_numeric(years, errors="coerce")

    plt.figure(figsize=(10, 6))
    plt.plot(
        years,
        expectancy,
        color="#1f77b4",
        linewidth=2.2,
        label="Morocco",
    )

    plt.title(
        "Morocco Life Expectancy Projections",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)

    plt.legend(
        loc="upper left",
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
        print(f"Unexpected error: {type(e).__name__} - {e}", file=sys.stderr)
        sys.exit(1)
