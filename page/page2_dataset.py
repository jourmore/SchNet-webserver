import streamlit as st
import pandas as pd

@st.fragment
def page_dataset():
	st.subheader('Form information, Descriptor transformation, raining dataset')

	tab1, tab2, tab3 = st.tabs(["📚 Form information", "📚 Descriptor transformation", "📚 Training dataset"])
	with tab1:
		st.markdown('''Interval of sound (1-1000ms)''')
		st.markdown('''Intensity of sound (1-9)''')
	with tab2:
		st.markdown('''A1 = float((M[2] + M[4] + M[6] + M[18] + M[24] + M[25] + M[30]) / 7)''')
		st.markdown('''A3 = float((M[8] + M[15] + M[23] + M[27] + M[32] + M[34] + M[36]) / 7)''')
		st.markdown('''A5 = float((M[5] + M[7] + M[10] + M[12] + M[17] + M[26] + M[31]) / 7)''')
		st.markdown('''A7 = float((M[11] + M[13] + M[16] + M[21] + M[22] + M[28] + M[33]) / 7)''')
		st.markdown('''A9 = float((M[3] + M[9] + M[14] + M[19] + M[20] + M[29] + M[35]) / 7)''')
		st.markdown('''B1 = float((M[2] + M[4] + M[6] + M[18] + M[24] + M[25] + M[30]) / 7)''')
		st.markdown('''B3 = float((M[8] + M[15] + M[23] + M[27] + M[32] + M[34] + M[36]) / 7)''')
		st.markdown('''B5 = float((M[5] + M[7] + M[10] + M[12] + M[17] + M[26] + M[31]) / 7)''')
		st.markdown('''B7 = float((M[11] + M[13] + M[16] + M[21] + M[22] + M[28] + M[33]) / 7)''')
		st.markdown('''B9 = float((M[3] + M[9] + M[14] + M[19] + M[20] + M[29] + M[35]) / 7)''')
		st.markdown('''AA1 = float((ans[2] + ans[4] + ans[6] + ans[18] + ans[24] + ans[25] + ans[30]) / 7)''')
		st.markdown('''AA3 = float((ans[8] + ans[15] + ans[23] + ans[27] + ans[32] + ans[34] + ans[36]) / 7)''')
		st.markdown('''AA5 = float((ans[5] + ans[7] + ans[10] + ans[12] + ans[17] + ans[26] + ans[31]) / 7)''')
		st.markdown('''AA7 = float((ans[11] + ans[13] + ans[16] + ans[21] + ans[22] + ans[28] + ans[33]) / 7)''')
		st.markdown('''AA9 = float((ans[3] + ans[9] + ans[14] + ans[19] + ans[20] + ans[29] + ans[35]) / 7)''')
		st.markdown('''R1 = float(B1 / A1)''')
		st.markdown('''R3 = float(B3 / A3)''')
		st.markdown('''R5 = float(B5 / A5)''')
		st.markdown('''R7 = float(B7 / A7)''')
		st.markdown('''R9 = float(B9 / A9)''')
		st.markdown('''sex = 1(Man) or 2(Woman)''')
	with tab3:
		st.markdown("Schnet training dataset")
		df=pd.read_csv("./static/class.csv")
		st.dataframe(df, use_container_width=True, height=600)
