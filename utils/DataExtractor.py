import re
import json
import jmespath
import pandas as pd
from bs4 import BeautifulSoup


def extract_text(pattern, string):
    try:
        if re.search(pattern, string).group(1):
            return re.search(pattern, string).group(1)
        else:
            return re.search(pattern, string).group(2)
    except Exception as e:
        raise ValueError("Invalid query: {0}, {1}".format(pattern, str(e)))


def extract_json(target, source):
    try:
        return jmespath.search(target, json.loads(source))

    except Exception as e:
        raise ValueError("Invalid query: {0}, {1}".format(target, str(e)))


def extract_html(target, source):
    soup = BeautifulSoup(source, features='lxml')
    if target == 'rdt_url':
        try:
            formfield = soup.find_all('form', {'id': 'submitForm'})
            rdt_url = [d['action'] for d in formfield]
            return rdt_url[0]

        except Exception as e:
            raise ValueError("Invalid query: {0}".format(str(e)))

    elif target == 'form_data':
        try:
            formfield = soup.find_all('input', {'type': 'hidden'})
            key = [d['name'] for d in formfield]
            value = [d['value'] for d in formfield]
            form_data = dict(zip(key, value))
            return form_data

        except Exception as e:
            raise ValueError("Invalid query: {0}".format(str(e)))


# 先以讀取excel並回傳所需數值為主, 後續視情況調整
def extract_excel(row_index, column, file_path, *use_cols, skip_rows=None):
    cols = None
    if use_cols:
        cols = list(use_cols)
    df = pd.read_excel(file_path, usecols=cols, skiprows=skip_rows)

    target_value = None
    if type(column) == int:  # iat[資料索引值,欄位順序]
        target_value = df.iat[row_index, column]
    elif type(column) == str:  # at[資料索引值,欄位名稱]
        target_value = df.at[row_index, column]
    else:
        print("Please input column order or name.")
    return target_value


# For test_UI/page/AdminTool.py get_export_file_data用, 避免新版xlrd不支援.xlsx的問題
def get_excel_columnName(file_path, use_cols=None, skip_rows=None):
    df = pd.read_excel(file_path, usecols=use_cols, skiprows=skip_rows)
    return df.columns.values.tolist()


if __name__ == '__main__':
    pass
