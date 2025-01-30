import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset and display its dimensions
    
    Parameters:
        path (str): Path to the CSV file
    
    Returns:
        pd.DataFrame: The loaded dataset, or None if there's an error
    """
    try:
        # Read the CSV file
        dataset = pd.read_csv(path)
        
        # Get and display the dimensions
        print(f"Loading dataset of dimensions {dataset.shape}")
        
        return dataset
    
    except (FileNotFoundError, pd.errors.EmptyDataError, 
            pd.errors.ParserError, PermissionError):
        return None
