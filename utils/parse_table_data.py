from typing import List
import pandas as pd


async def parse_table_data(file_name: str) -> List[List[str]]:
    df = pd.read_excel(file_name)
    df.drop(columns=df.columns[0])

    return df.values.tolist()
