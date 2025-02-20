import matplotlib.pyplot
import pandas
from load_csv import load


def main():
    try:
        dataset: pandas.DataFrame = load("life_expectancy_years.csv")

        france: pandas.DataFrame = dataset.loc[dataset["country"] == "France"]

        if france.empty:
            print("Data not found for France")
            return

        years = france.columns[1:].astype(int)
        life_expectancy = france.iloc[0, 1:]

        matplotlib.pyplot.figure(figsize=(10, 6))
        matplotlib.pyplot.plot(years, life_expectancy)

        matplotlib.pyplot.title("Life Expectancy in France over the Years")
        matplotlib.pyplot.xlabel("Year")
        matplotlib.pyplot.ylabel("Life Expectancy (years)")

        matplotlib.pyplot.show()

    except Exception:
        pass


if __name__ == "__main__":
    main()
