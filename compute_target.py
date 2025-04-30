import pandas as pd
import numpy as np         

def compute_tunh(df):
    """Efficient calculation for daily Time to New High (TUNH) using a sorted stack approach."""
    
    df["Date"] = pd.to_datetime(df["Date"])

    times = df["Date"].values
    highs = df["High"].values
    results = np.full(len(highs), np.nan)  # Pre-allocate results array
    
    sorted_highs = []
    sorted_times = []
    
    for i in range(len(highs) - 1, -1, -1):  # Iterate backwards (right to left)
        while sorted_highs and sorted_highs[-1] <= highs[i]:
            sorted_highs.pop()
            sorted_times.pop()
        
        if sorted_highs:
            time_difference = (sorted_times[-1] - times[i]).astype('timedelta64[D]').astype(int)  # Convert to days correctly
            results[i] = time_difference
        
        sorted_highs.append(highs[i])
        sorted_times.append(times[i])

    df["tunh"] = results
    return df