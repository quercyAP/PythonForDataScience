import matplotlib.pyplot
from load_csv import load


def main():
    try:
        dataset = load("population_total.csv")

        france = dataset.loc[dataset["country"] == "France"]
        germany = dataset.loc[dataset["country"] == "Belgium"]

        if france.empty or germany.empty:
            print("Data not found for one or both countries")
            return

        years = france.columns[1:].astype(int)
        france_pop = france.iloc[0, 1:].apply(
            lambda x: float(str(x).replace("M", ""))
            if "M" in str(x) else float(x)
        )
        germany_pop = germany.iloc[0, 1:].apply(
            lambda x: float(str(x).replace("M", ""))
            if "M" in str(x) else float(x)
        )

        mask = (years >= 1800) & (years <= 2050)
        years = years[mask]
        france_pop = france_pop[mask]
        germany_pop = germany_pop[mask]

        matplotlib.pyplot.figure(figsize=(10, 6))
        matplotlib.pyplot.plot(years, france_pop, label="France")
        matplotlib.pyplot.plot(years, germany_pop, label="Belgium")

        matplotlib.pyplot.title("Population Projections")
        matplotlib.pyplot.xlabel("Year")
        matplotlib.pyplot.ylabel("Population")
        matplotlib.pyplot.legend()

        matplotlib.pyplot.show()

    except Exception:
        pass


if __name__ == "__main__":
    main()
