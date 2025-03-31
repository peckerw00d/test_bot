from typing import List, Tuple
import pandas as pd


async def parse_excel_data(file_name: str) -> List[Tuple[str]]:
    df = pd.read_excel(file_name)
    df.drop(columns=df.columns[0])
    data = [tuple(row) for row in df.to_numpy()]

    return data
