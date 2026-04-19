from konversi_skala_bacaan import konversi #from nama file import nama fungsinya

def konversi (value_in_mGal, skala_bacaan, counter_reading, factor_for_interval):
    return counter_reading + (skala_bacaan - value_in_mGal) * factor_for_interval

print("Nilai Skala Bacaan\n", konversi)
