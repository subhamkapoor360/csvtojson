import pandas as pd

def convert_to_json_and_save():
	dataframe = pd.read_excel('ISO10383_MIC.xls',sheet_name = "MICs List by CC",encoding='utf-8').fillna("N/A")
	list_of_dict = dataframe.T.to_dict('dict')
	dataframe.to_json("mcc.json",orient="records")
	return list_of_dict




