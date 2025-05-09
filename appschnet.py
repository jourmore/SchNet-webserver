import streamlit as st
import streamlit_antd_components as sac
from streamlit_extras.stylable_container import stylable_container
import warnings
warnings.filterwarnings("ignore")
from page import *
from page.utility import name_title2, footer

st.set_page_config(page_title="Schnet v.2025", page_icon="app/static/logo.png", layout="wide")

def local_css(file_name):
	 with open(file_name) as f:
		  st.html('<style>{}</style>'.format(f.read())) 
local_css("./static/style.css")

css_styles_header = '''
	   {
		   position: fixed; /* 让容器固定在页面顶部 */
		   position: -webkit-sticky;
		   top: 0rem; /* 距顶部距离 */
		   left: 8%;  /* 距左边界距离 */
		   width: 100%; /* 宽度 */
		   height: 5%;
		   background: #e0e0e0; /* 背景 #FFFFFF */
		   display: flex;
		   z-index: 1000; /* 确保容器层级高于其他内容 */
		   padding: 10 10; /* 内边距 */
		   box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 投影效果 */
		   text-align: center;
		   font-weight: bold;
		   font-style: italic;
		   font-size: 160%;
		   color: #bb2649;
		   align-items: center;
		   justify-content: center;
	   }
   '''

with stylable_container(key='page_fixed', css_styles=css_styles_header):
	st.html("""
		<div>
			🌟 Schnet: Prediction models for schizophrenia (v.2025.05.01)
		</div>
	""")

st.logo(image="./static/logo.png", size="large", link="http://100.140.0.213:8501/", icon_image="./static/logo.png")

with st.sidebar:
	st.image("static/banners.jpg")
	page = sac.menu([
		sac.MenuItem('Home', icon='house-fill', tag=[sac.Tag('Schnet', color='green'), sac.Tag('2025', 'blue')]),
		 sac.MenuItem(type='divider'),
		 sac.MenuItem('Schnet', icon='box-fill', description='Schnet app'),
		 sac.MenuItem(type='divider'),
		 sac.MenuItem('Dataset', icon='box-fill', description='Training dataset'),
		 sac.MenuItem(type='divider'),
		 sac.MenuItem('About', icon='box-fill', description='About us')
	], open_all=True, height=None, index=0, open_index=[1], indent=30, color='#4682b4', variant='left-bar', size=20)

if page == "Home":
	page_home()
	st.html(footer)
elif page == "Schnet":
	name_title2(text='☁️ Schnet: Predict whether or not schizophrenia')
	page_Schnet()
elif page == "Dataset":
	name_title2(text='☁️ Download Datasets')
	page_dataset()
elif page == "About":
	name_title2(text='☁️ About us')
	st.divider()
	page_about()
