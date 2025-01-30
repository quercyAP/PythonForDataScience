import matplotlib.pyplot
from load_csv import load


def main():
    life_exp = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if life_exp is None or income is None:
        print("Error loading files")
        return

    life_exp_1900 = life_exp["1900"]
    income_1900 = income["1900"]

    matplotlib.pyplot.figure(figsize=(10, 6))
    matplotlib.pyplot.scatter(income_1900, life_exp_1900)

    matplotlib.pyplot.xscale("log")

    matplotlib.pyplot.title("Life Expectancy vs GDP per Capita (1900)")
    matplotlib.pyplot.xlabel("GDP per Capita ($ adjusted for inflation)")
    matplotlib.pyplot.ylabel("Life Expectancy (years)")

    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
