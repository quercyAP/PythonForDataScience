import pandas


def load(path: str) -> pandas.DataFrame:
    """
    Load a CSV dataset and display its dimensions

    Parameters:
        path (str): Path to the CSV file

    Returns:
        pd.DataFrame: The loaded dataset, or None if there's an error
    """
    try:
        dataset = pandas.read_csv(path)

        print(f"Loading dataset of dimensions {dataset.shape}")

        return dataset

    except (
        FileNotFoundError,
        pandas.errors.EmptyDataError,
        pandas.errors.ParserError,
        PermissionError,
    ) as e:
        print(f'Error : {str(e)}')
        return None
