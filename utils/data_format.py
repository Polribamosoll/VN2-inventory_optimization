import pandas as pd
from pathlib import Path

def wide_to_long_sales(df: pd.DataFrame, id_cols: list = ['Store', 'Product'],
                       date_col_name: str = 'Date', value_col_name: str = 'Sales') -> pd.DataFrame:
    """
    Convert a wide-format sales dataframe to long format for forecasting.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe in wide format (one column per date).
    id_cols : list
        Columns to keep as identifiers (e.g., ['Store', 'Product']).
    date_col_name : str
        Name of the new date column.
    value_col_name : str
        Name of the new value column.

    Returns
    -------
    pd.DataFrame
        Long-format dataframe with columns [id_cols, date_col_name, value_col_name].
    """
    value_vars = [col for col in df.columns if col not in id_cols]

    # Melt the dataframe
    df_long = df.melt(
        id_vars=id_cols,
        value_vars=value_vars,
        var_name=date_col_name,
        value_name=value_col_name
    )
    df_long[date_col_name] = pd.to_datetime(df_long[date_col_name])

    # Sort
    df_long = df_long.sort_values(by=id_cols + [date_col_name]).reset_index(drop=True)

    return df_long