import streamlit as st
import streamlit_antd_components as sac
from page.utility import name_title, clean_all, text_a

@st.fragment
def page_home():
	name_title(text='Welcome to Schnet')

	st.subheader("**> Why do Schnet?**")
	col = st.columns(2)
	with col[0]:
		content1 = "✔ **:blue[Schizophrenia]** is a high-risk, high-burden,\
		 high-disability psychiatric disorder with a prolonged course, and early identification\
		 and intervention can help alleviate socioeconomic adversities, including illness-induced\
		  poverty and public safety risks. Traditional clinical diagnosis of schizophrenia has\
		   predominantly relied on structured clinical interviews, with subjective bias and\
		    misdiagnosis rates. Sense of agency (SoA) is a core feature of schizophrenia, yet\
		     directly predicting schizophrenia from this trait and quantifying its diagnostic\
		      importance remain critical gaps in the field. In recent years, computer-aided\
		       diagnosis using machine learning (ML) has emerged as a research hotspot."
		content2 = "✔ **:blue[Schnet]** Thus, this study develops ML models to investigate\
		 the potential of quantifiable SoA features for schizophrenia prediction. First,\
		  agency rating, time interval estimation and intentional binding were obtained for\
		   measuring SoA. Then, six baseline ML algorithms were trained, with RF and TabPFN\
		    demonstrating optimal performance. To enhance reliability, we implemented ensemble\
		     model strategy with RF and TabPFN, yielding a high-performance classifier SchNet (Accuracy of 0.90).\
		      To bridge theory and practice, we deployed SchNet webserver (https://github.com/jourmore/SchNet-webserver),\
		       offering SoA test online, schizophrenia risk prediction and interpretability analysis.\
		        This tool serves as a translational bridge between computer research and clinical application,\
		         supporting data-informed therapeutic strategies."
		text_a(None, '14px', content1)
		text_a(None, '14px', content2)
	with col[1]:
		st.image("./static/homebg.png")

	st.subheader("**> Overview**")
	content3 = "➀ SchNet: Schizophrenia risk prediction. \n"
	content4 = "➁ Individual interpretability analysis: \n"
	text_a(None, '15px', content3)
	text_a(None, '15px', content4)

	with st.popover(" ⌛️ Update Timelines"):
		st.write("* :green[_Now: Under review..._]\n"
				"* 2024-4-30: Models and Webserver.\n"
				"* 2024-12-20: Webserver Development.\n"
				"* 2024-12-19: Prediction models were developed.\n"
				"* 2024-11-19: Dataset was constructed.\n"
				"* 2024-11-01: The Schnet Project was Launched.")
		clean_all()
