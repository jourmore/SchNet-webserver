import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import streamlit_antd_components as sac
import pandas as pd
import requests, json
from io import StringIO

url = 'http://121.37.24.233:5000/schnetapi'

def show_metric(predictions, probability):
	if len(predictions)==1:
		if predictions[0] == 1:
			st.metric("Schizophrenia", "Yes", f"{probability[0]*100} %")
		else:
			st.metric("Non-schizophrenia", "No", f"{-probability[0]*100} %")
		style_metric_cards()
	else:
		for i, (prediction, proba) in enumerate(zip(predictions, probability)):
			st.write(f":green[Samples: {i}]")
			if prediction == 1:
				st.metric("Schizophrenia", "Yes", f"{probability[i]*100}")
			else:
				st.metric("Non-schizophrenia", "No", f"{-probability[i]*100}")
			style_metric_cards()

def Single_task():
	st.subheader(":violet[Single task]")

	col = st.columns((3,2))
	with col[0]:
		st.subheader(":orange[Step 1: Sense of agency (SoA) testing]")
		st.video('./static/MTVideo2.mp4', format="video/mp4", start_time=0, autoplay=False, muted=False, subtitles="./static/subtitles_predict.vtt")
	with col[1]:
		st.subheader(":orange[Step 2: Fill out a form]")
		with st.container(height=400, border=True, key="ForPred"):
			sex_name = st.selectbox("Man or Woman.", ("Man", "Woman"), key="Man or Woman")
			col = st.columns((1,0.1,1))
			with col[0]:
				st.write(":red[Interval of sound (1-1000ms)]")
				M = {}
				for i in range(37):
					M[i] = st.number_input(f":blue[{i+1}/37]", min_value=1, max_value=1000, value="min", key=f"Interval of sound {i+1}")
			with col[2]:
				st.write(":red[Intensity of sound (1-9)]")
				ans = {}
				for i in range(37):
					ans[i] = st.number_input(f":green[{i+1}/37]", min_value=1, max_value=9, value="min", key=f"Intensity of sound {i+1}")
		submitted = st.button("Click to Predict >>>", type="primary", icon="🛑")

	st.subheader(":orange[Step 3: Output]")
	st.write(f":red[***Convert to 16 descriptors (A1, A3, A5, A7, A9, AA1, AA3, AA5, AA7, AA9, R1, R3, R5, R7, R9, sex)**]")
	if submitted:
		placeholder = st.empty()
		placeholder.image("./static/loading.gif")
		A1 = float((M[2] + M[4] + M[6] + M[18] + M[24] + M[25] + M[30]) / 7)
		A3 = float((M[8] + M[15] + M[23] + M[27] + M[32] + M[34] + M[36]) / 7)
		A5 = float((M[5] + M[7] + M[10] + M[12] + M[17] + M[26] + M[31]) / 7)
		A7 = float((M[11] + M[13] + M[16] + M[21] + M[22] + M[28] + M[33]) / 7)
		A9 = float((M[3] + M[9] + M[14] + M[19] + M[20] + M[29] + M[35]) / 7)
		B1 = float((M[2] + M[4] + M[6] + M[18] + M[24] + M[25] + M[30]) / 7)
		B3 = float((M[8] + M[15] + M[23] + M[27] + M[32] + M[34] + M[36]) / 7)
		B5 = float((M[5] + M[7] + M[10] + M[12] + M[17] + M[26] + M[31]) / 7)
		B7 = float((M[11] + M[13] + M[16] + M[21] + M[22] + M[28] + M[33]) / 7)
		B9 = float((M[3] + M[9] + M[14] + M[19] + M[20] + M[29] + M[35]) / 7)
		AA1 = float((ans[2] + ans[4] + ans[6] + ans[18] + ans[24] + ans[25] + ans[30]) / 7)
		AA3 = float((ans[8] + ans[15] + ans[23] + ans[27] + ans[32] + ans[34] + ans[36]) / 7)
		AA5 = float((ans[5] + ans[7] + ans[10] + ans[12] + ans[17] + ans[26] + ans[31]) / 7)
		AA7 = float((ans[11] + ans[13] + ans[16] + ans[21] + ans[22] + ans[28] + ans[33]) / 7)
		AA9 = float((ans[3] + ans[9] + ans[14] + ans[19] + ans[20] + ans[29] + ans[35]) / 7)
		R1 = float(B1 / A1)
		R3 = float(B3 / A3)
		R5 = float(B5 / A5)
		R7 = float(B7 / A7)
		R9 = float(B9 / A9)
		sex = 1 if sex_name == "Man" else 2

		col = st.columns((1,7))
		with col[0]:
			varss = ['A1', 'A3', 'A5', 'A7', 'A9', 'AA1', 'AA3', 'AA5', 'AA7', 'AA9', 'R1', 'R3', 'R5', 'R7', 'R9', 'sex']
			for var in varss:
				st.write(f":blue[*{var}]: {locals()[var]}")
		with col[1]:
			with st.container(height=620, border=True, key="SchPred"):
				# 特征转换为json，然后api计算
				data = [A1, A3, A5, A7, A9, AA1, AA3, AA5, AA7, AA9, R1, R3, R5, R7, R9, sex]
				# data = {'A1':A1, 'A3':A3, 'A5':A5, 'A7':A7, 'A9':A9, 'AA1':AA1, 'AA3':AA3, 'AA5':AA5, 'AA7':AA7,
				# 		'AA9':AA9, 'R1':R1, 'R3':R3, 'R5':R5, 'R7':R7, 'R9':R9, 'sex':sex}

				# data_dict = dict(zip(varss, data))
				json_data = [dict(zip(varss, data))]
				# st.write(json_data)

				try:
					response = requests.post(url, json=json_data)
					response.raise_for_status()
					result = response.json()
					st.success(f'_Calculation complete !_', icon="✅")

					result_json_str = json.dumps(result['Result'])
					result_df = pd.read_json(StringIO(result_json_str))
					st.dataframe(result_df, use_container_width=True, height=120)

					predictions = result['Predictions']
					probability = result['Probability']
					# st.write(predictions, probability)

					col = st.columns((0.2, 0.1, 0.4, 0.1, 0.5))
					with col[0]:
						show_metric(predictions, probability)
					with col[2]:
						st.image("./predict/shap_one_0.svg")
					with col[4]:
						st.image("./predict/lime_one_0.svg")

				except:
					st.warning('_Service Exceptions._', icon="⚠️")

		placeholder.empty()


def Multiple_task():
	st.subheader(":violet[Multiple task]")

	st.write(":red[*Refer to the sample form, fill in the information, upload the form, and click Predict.]")
	with open(f"./static/Schnet_Multiple.csv", "rb") as filename:
		st.download_button(label="Example csv (with header)", data=filename, file_name='Schnet_Multiple.csv', mime='application/octet-stream')

	data = False
	uploaded_file = st.file_uploader(":gray[👇 Upload a file with **CSV** format.]", type=["csv"], accept_multiple_files=False, key="csv_file")
	type_sel = sac.checkbox(items=['Loading Examples'],label=None, index=None, align='center', size='lg', radius='xs', color='pink')
	column_names = ['A1', 'A3', 'A5', 'A7', 'A9', 'AA1', 'AA3', 'AA5', 'AA7', 'AA9', 'R1', 'R3', 'R5', 'R7', 'R9', 'sex']

	# 将文件转换为可读取
	if st.button("Click to Predict >>>", type="primary", icon="🛑"):
		placeholder = st.empty()
		placeholder.image("./static/loading.gif")	

		if type_sel != []:
			data = [
					[278,378,571,800,814,7.21,6.14,4.35,2.07,2,0.36,1.02,0.98,0.79,0.82,2,1],
			        [142,200,185,192,235,7.93,7,7.07,7,6.86,0.9,1.21,2.39,2.3,2.09,1,1],
			        [100,185,278,385,514,9,8.14,7.28,6.21,4.85,2,1.85,1.62,1.61,1.44,2,0],
			        ]
		elif uploaded_file is not None:
			df = pd.read_csv(uploaded_file, header=None, skiprows=1)
			data = df.values.tolist()
		else:
			st.warning('_Please upload data first._', icon="⚠️")

		if data:
			json_data = [dict(zip(column_names, row)) for row in data]

		try:
			response = requests.post(url, json=json_data)
			response.raise_for_status()
			result = response.json()
			st.success(f'_Calculation complete !_', icon="✅")

			result_json_str = json.dumps(result['Result'])
			result_df = pd.read_json(StringIO(result_json_str))
			st.dataframe(result_df, use_container_width=True, height=220)
			
			predictions = result['Predictions']
			probability = result['Probability']

			# show_metric(predictions, probability)
			for i in range(len(predictions)):
				st.write(f":red[Samples: {i}]")
				col = st.columns((0.2, 0.1, 0.4, 0.1, 0.5))
				with col[0]:
					show_metric([predictions[i]], [probability[i]])
				with col[2]:
					st.image(f"./predict/shap_one_{i}.svg")
				with col[4]:
					st.image(f"./predict/lime_one_{i}.svg")

		except:
			st.warning('_Service Exceptions._', icon="⚠️")

		placeholder.empty()


@st.cache_resource
def example_csv():
	result_df = pd.read_csv("./example/results.csv")
	return result_df

def Example_task():
	st.subheader(":violet[Example output]")
	df = example_csv()
	st.dataframe(df, use_container_width=True, height=250)

	st.subheader(":rainbow[> Analysis result:]", divider="rainbow")
	for i in range(len(df)):
		st.write(f"**:red[Sample {i+1}:]**")
		col = st.columns((0.3,1,0.1,1))
		with col[0]:
			show_metric([int(df['Ensemble'][i])], [float(df['Probability'][i])])
		with col[1]:
			st.image(f"./example/shap_barone_RF_{i}.png")
		with col[3]:
			st.image(f"./example/lime_one_RF_{i}.png")


@st.fragment
def page_Schnet():
	with st.container(border=True):
		st.write("**Welcome to the Schnet (Schizophrenia Prediction Model)**")
		st.write(":orange[Step 1: Sense of agency (SoA) testing]")
		st.write(":orange[Step 2: Fill out a form]")
		st.write(":orange[Step 3: Output]")

		Tool_page = st.pills(':blue[*Select a page:]',['🔵 +++Single+++', '🔷 +++Multiple+++', '✅ ---Example---'],
					default='🔵 +++Single+++', key="Tool_page", selection_mode="single")

	if Tool_page == "🔵 +++Single+++":
		Single_task()
	elif Tool_page == "🔷 +++Multiple+++":
		Multiple_task()
	else:
		Example_task()
