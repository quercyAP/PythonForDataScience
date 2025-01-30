import matplotlib.pyplot
import pandas
from load_csv import load


def main():
    dataset : pandas.DataFrame = load("day02/assets/life_expectancy_years.csv")
    
    france_data : pandas.DataFrame = dataset.loc[dataset['country'] == 'France']
    
    if france_data.empty:
        print("Data not found for France")
        return
    
    years = france_data.columns[1:].astype(int)
    life_expectancy = france_data.iloc[0, 1:]
    
    matplotlib.pyplot.figure(figsize=(10, 6))
    matplotlib.pyplot.plot(years, life_expectancy)
    
    matplotlib.pyplot.title("Life Expectancy in France over the Years")
    matplotlib.pyplot.xlabel("Year")
    matplotlib.pyplot.ylabel("Life Expectancy (years)")
    
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()
