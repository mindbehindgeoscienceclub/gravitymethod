import pandas as pd
import numpy as np

from konversi_skala_bacaan import konversi #from 

def konversi (value_in_mGal, skala_bacaan, counter_reading, factor_for_interval):
    return counter_reading + (skala_bacaan - value_in_mGal) * factor_for_interval

print("Nilai Skala Bacaan\n", konversi)
