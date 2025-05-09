import streamlit as st

@st.fragment
def page_about():
	col = st.columns((0.8,0.1,1))
	with col[0]:
		st.image("./static/CCP.png")
	with col[2]:
		with st.container(border=True):
			st.header("[Chaochao Pan's Lab](https://xlxy.nwnu.edu.cn/2022/0707/c130a193405/page.htm)")
			st.subheader("*Northwest Normal University - School of psychology*")
			st.subheader("Email: chaochaopan_nwnu@163.com")
			st.subheader("Reasearch: Personality and mental health")
			st.subheader(":orange[1.Self-deficit, cross-channel integration, etc., in the schizophrenia spectrum.]")
			st.subheader(":orange[2.The sense of autonomy, sense of ownership and so on in schizophrenia.]")
			
