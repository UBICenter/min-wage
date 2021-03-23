import pandas as pd
import us

import io
from zipfile import ZipFile


def read_zip(zip_fn, extract_fn=None):
    zf = ZipFile(zip_fn)
    if extract_fn:
        return zf.read(extract_fn)
    else:
        return {name: zf.read(name) for name in zf.namelist()}


raw = pd.read_excel(
    io.BytesIO(read_zip("oes_2019.xlsx.zip", "all_data_M_2019.xlsx")),
    engine="openpyxl",
)

raw.to_csv("oes.csv.gz", index=False, compression="gzip")
