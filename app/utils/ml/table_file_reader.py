from app.utils.ml.ml import run_preditcion_on_model
import pandas as pd
from .ml import normal_int


def read_df(df: pd.DataFrame) -> pd.DataFrame:
    predictions = list()

    for index, row in df.iterrows():
        prediction = run_preditcion_on_model(
            row['district'],	
            row['metro_name'],	
            row['metro_time'],	
            row['metro_get_type'],	
            row['size'],	
            row['kitchen'],	
            row['floor'],	
            row['floors'],	
            row['constructed'],	
            row['fix'],	
            row['type_of_building'],	
            row['type_of_walls']
        )
        predictions.append(normal_int(prediction[0]))

    df['prediction'] = predictions

    return df
