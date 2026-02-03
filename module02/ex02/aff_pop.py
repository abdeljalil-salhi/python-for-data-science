import sys
import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Load population dataset and plot population projection
    for Morocco vs France.
    """
    dataset_path = "population_total.csv"

    df = load(dataset_path)
    if df is None:
        sys.exit(1)

    my_country = "Morocco"
    compare_country = "France"

    missing = []
    for c in [my_country, compare_country]:
        if c not in df["country"].values:
            missing.append(c)

    if missing:
        print(
            f"Error: Country not found: {', '.join(missing)}",
            file=sys.stderr,
        )
        sys.exit(1)

    my_data = df[df["country"] == my_country].iloc[0]
    comp_data = df[df["country"] == compare_country].iloc[0]

    years = my_data.index[1:]
    years = pd.to_numeric(years, errors="coerce")

    my_pop = my_data.values[1:]
    comp_pop = comp_data.values[1:]

    # convert population strings like "12.34M" to numbers
    def convert_pop(x: str) -> float:
        if isinstance(x, str):
            if "M" in x:
                return float(x.replace("M", "")) * 1_000_000
            elif "K" in x:
                return float(x.replace("K", "")) * 1_000
            else:
                try:
                    return float(x)
                except ValueError:
                    return 0.0
        return float(x) if pd.notna(x) else 0.0

    my_pop = [convert_pop(v) for v in my_pop]
    comp_pop = [convert_pop(v) for v in comp_pop]

    mask = (years >= 1800) & (years <= 2050)
    years_filtered = years[mask]
    my_pop_filtered = [my_pop[i] for i in range(len(my_pop)) if mask[i]]
    comp_pop_filtered = [comp_pop[i] for i in range(len(comp_pop)) if mask[i]]

    plt.figure(figsize=(10, 6))
    plt.plot(
        years_filtered,
        my_pop_filtered,
        label=my_country,
        linewidth=2.2,
        color="#1f77b4",
    )
    plt.plot(
        years_filtered,
        comp_pop_filtered,
        label=compare_country,
        linewidth=2.2,
        color="#ff7f0e",
    )

    plt.title("Population Projections", fontsize=14, fontweight="bold")
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population", fontsize=12)

    def millions(x: float, _) -> str:
        return f"{x / 1e6:.0f}M"

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(millions))
    plt.legend(loc="upper left", fontsize=11)
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
