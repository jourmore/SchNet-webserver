import streamlit as st
import tempfile, os, base64, requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#紫色、黄色（run）
cstyles1="""
            button {background-color: #7C2762;
            color: #ffff00;
            border-radius: 3px;}"""
#深蓝，白色（下载）
cstyles2="""
            button {background-color: #3d85c6;
            color: white;
            border-radius: 6px;}"""
#深灰，白色（清理等）
cstyles3="""
            button {background-color: #d9d2e9;
            color: black;
            border-radius: 10px;}"""

#margin-top: 0px; margin-bottom: -10px; padding-top: 0px; padding-bottom: 0px;
footer="""
        <div class="footer_center">
            <p style="font-size:  20px; text-align: center;"><b>SchNet: Sense of Agency Drived Schizophrenia Prediction with Integrated Ensemble Machine Learning and Interpretability.</b> [<a href="https://github.com/jourmore/SchNet-webserver" target="_blank" pcked="1"> link</a></span>]</p>
        </div>
        <div class="footer_center">
            <p style="font-size:  15px; text-align: center;"> &#169; 2025. All rights reserved by <a href="https://xlxy.nwnu.edu.cn/2022/0707/c130a193405/page.htm" target="_blank" pcked="1">Chaochao Pan's Lab</a>, Northwest Normal University.</p>
        </div>
"""

footer2="""
        <div class="footer_center" style="background-color: #fffefb; color: #3F51B5; width: 100%; padding: 10px; box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2);">
            <div class="box1" style="width: auto; height: auto;">
                <a href="https://clustrmaps.com/site/1c0rp" title="Visit tracker">
                    <img src="//clustrmaps.com/map_v2.png?cl=58bddb&w=a&t=tt&d=L_qgpW1IdDkDn1q-MFfEEAwn_crYxXfga4k9JQTpxfM&co=ffffff&ct=160077&w=300&h=200" />
                </a>
            </div>
            <div class="box2; ">
                <p style="font-size:  20px; text-align: center;"><b>Schnet: Prediction models for schizophrenia.</b> [<a href="http://www.nbscal.online/" target="_blank" pcked="1"> link</a></span>]</p>
                <p style="font-size:  15px; text-align: center;"><a href="https://beian.miit.gov.cn/" target="_blank">蜀ICP备2023034695号-1</a> &#169; 2024. All rights reserved by <a href="https://xlxy.nwnu.edu.cn/2022/0707/c130a193405/page.htm" target="_blank" pcked="1">Chaochao Pan's Lab</a>, Northwest Normal University.</p>
            </div>
        </div>
"""

@st.cache_data
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

def time_now():
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write("_🕔 Last click time:_ " + current_time)

    return_time = datetime.now().strftime("%Y%m%d%H%M%S")
    return return_time

def clean_all():
    if st.button("🔘 Clear All Cache"):
        st.cache_data.clear()
        st.cache_resource.clear()

def backgroundfig(figure='bgfig.png'):
    img = get_base64_of_bin_file(figure)
    page_bg_img = f"""
        <style>
        .stAppViewContainer {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 10%;
        background-position: top 60px left 50px;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        </style>
        """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def name_title(text='Welcome to NBsPocket'):
    ttt_css = """
    <style>
        @keyframes text-gradient-title {
            0% { color: #0077C2; }
            50% { color: #bb2649; }
            100% { color: #0077C2; }
        }
        .text-gradient-title {
            position: sticky;
            top: 0px;
            animation: text-gradient-title 4s ease-in-out infinite;
            font-size: 80px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            font-style: italic;
        }
    </style>
    """
    st.html(ttt_css)
    st.markdown(f'<h1 class="text-gradient-title">{text}</h1>', unsafe_allow_html=True)

def name_title2(text='Thermostability Predictor'):
    tt_css = """
    <style>
        @keyframes text-gradient-title {
            0% { color: #0077C2; }
            50% { color: #bb2649; }
            100% { color: #0077C2; }
        }
        .text-gradient-title {
            position: sticky;
            top: 0px;
            animation: text-gradient-title 4s ease-in-out infinite;
            font-size: 36px;
            text-align: left;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
            font-style: italic;
        }
    </style>
    """
    st.html(tt_css)
    st.markdown(f'<h1 class="text-gradient-title">{text}</h1>', unsafe_allow_html=True)

def text_a(color, fs, str):
    st.markdown(f'<span style="font-size:{fs};text-align:left;color:{color}">{str}</span>',
    unsafe_allow_html=True)

def smile_upload():
    from streamlit_ketcher import st_ketcher
    mol_text = st.text_input("*You can paste SMILES text here:", "CC1C(=O)C=CC(=O)C=1", max_chars=100)
    mol_draw = st_ketcher("CC1C(=O)C=CC(=O)C=1", height=400, molecule_format="SMILES", key="ketcher_mol")
    style_pro = st.pills(':green[*Input type select:]',['Paste SMILES','Upload & Draw'], default='Paste SMILES', key="smi_type", selection_mode="single")
    if style_pro == "Paste SMILES":
        smile_code = mol_text
    else:
        smile_code = mol_draw
    st.subheader(f":green[Input molecule (SMILE):] {smile_code}")   
    return smile_code

def smile2sdf(smile_code, output_file_path):
    from rdkit import Chem
    from rdkit.Chem import AllChem
    mol = Chem.MolFromSmiles(smile_code)
    if mol is None:
        st.write(":red[Molecule Error.]")
    else:
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, randomSeed=123)
        AllChem.UFFOptimizeMolecule(mol)
        writer = Chem.SDWriter(output_file_path)
        writer.write(mol)
        writer.close()
        # st.write(":green[Molecule reading finish.]")
    return output_file_path

def pro_addH(file_path):
    if file_path.endswith('.pdb'):
        os.system(f'babel -ipdb {file_path} -opdb {file_path}.pdb -h')
        out_path = file_path + ".pdb"
    elif file_path.endswith('.pqr'):
        os.system(f'babel -ipqr {file_path} -opdb {file_path}.pdb -h')
        out_path = file_path + ".pdb"
    elif file_path.endswith('.cif'):
        os.system(f'babel -icif {file_path} -opdb {file_path}.pdb -h')
        out_path = file_path + ".pdb"
    else:
        st.warning("Please upload protein with format: pdb, pqr, cif.", icon="⚠️")
    return out_path

# lepro_linux_x86 {'1XOZ_clean.pdb'}
# os.rename('pro.pdb','1XOZ_clean_H.pdb')

def lig_addH(file_path):
    if file_path.endswith('.mol2'):
        os.system(f'babel -imol2 {file_path} -osdf {file_path}.sdf -h')
        out_path = file_path + ".sdf"
    elif file_path.endswith('.pdbqt'):
        os.system(f'babel -ipdbqt {file_path} -osdf {file_path}.sdf -h')
        out_path = file_path + ".sdf"
    elif file_path.endswith('.sdf'):
        os.system(f'babel -isdf {file_path} -osdf {file_path}.sdf -h')
        out_path = file_path + ".sdf"
    elif file_path.endswith('.mol'):
        os.system(f'babel -imol {file_path} -osdf {file_path}.sdf -h')
        out_path = file_path + ".sdf"
    elif file_path.endswith('.cif'):
        os.system(f'babel -icif {file_path} -osdf {file_path}.sdf -h')
        out_path = file_path + ".sdf"
    else:
        st.warning("Please upload molecule with format: sdf, mol, mol2, pdbqt, cif.", icon="⚠️")
    return out_path

def str2path(protein, output):
    temp_dir = tempfile.mkdtemp()
    with open(os.path.join(temp_dir, output), "wb") as f:
        f.write(protein.getvalue())
    file_path = os.path.join(temp_dir, output)

    if file_path.endswith(('.pdb', '.pqr', ".cif")):
        out_path = pro_addH(file_path)
    elif file_path.endswith((".sdf", ".mol", ".mol2")):
        out_path = lig_addH(file_path)
    else:
        out_path = file_path

    return out_path

def url2path(link, output):
    temp_dir = tempfile.mkdtemp()
    response = requests.get(link)
    if response.status_code == 200:
        with open(os.path.join(temp_dir, output), 'wb') as f:
            f.write(response.content)
            file_path = os.path.join(temp_dir, output)
        if file_path.endswith(('.pdb', '.pqr')):
            out_path = pro_addH(file_path)
        elif file_path.endswith((".sdf", ".mol", ".mol2", ".pdbqt", ".cif")):
            out_path = lig_addH(file_path)
    return out_path

def color2name(color):
    from static.color2name import rgb2name
    color = color.lstrip('#')
    rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
    return rgb2name(rgb)

def plot_colorbar(colors, labels):   
    fig, ax = plt.subplots(figsize=(9, 1))
    fig.subplots_adjust(bottom=0.5)
    cmap = plt.cm.colors.ListedColormap(colors)
    norm = plt.Normalize(vmin=0, vmax=len(colors)-1)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, cax=ax, orientation='horizontal')
    cbar.set_ticks(np.arange(len(colors)))
    cbar.set_ticklabels(labels)
    st.pyplot(fig)

def plot_radar(df):
    df = df.sort_values('cav_id')

    import plotly.express as px
    aaa = st.columns(2)
    with aaa[0]:
        fig1 = px.bar(df, x="cav_id", y="drug_score", title='Drug Score (druggability score)', color_discrete_sequence=['#FF6B6B'])
        fig1.update_layout(font=dict(family="Times New Roman", size=16, color='black'))
        fig1.update_traces(marker=dict(line=dict(color='black', width=2)))
        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

        fig2 = px.bar(df, x="cav_id", y="hydrophobicity_score", title='Hydrophobicity Score', color_discrete_sequence=['#c2a685'])
        fig2.update_layout(font=dict(family="Times New Roman", size=16, color='black'))
        fig2.update_traces(marker=dict(line=dict(color='black', width=2)))
        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

    with aaa[1]:
        fig3 = px.bar(df, x="cav_id", y="volume", title='Pocket Volume (angstrom^3)', color_discrete_sequence=['#009fb6'])
        fig3.update_layout(font=dict(family="Times New Roman", size=16, color='black'), bargap=0.6)
        fig3.update_traces(marker=dict(line=dict(color='black', width=2)))
        st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

        fig4 = px.bar(df, x="cav_id", y="polarity_score", title='Polarity Score', color_discrete_sequence=['#5DA399'])
        fig4.update_layout(font=dict(family="Times New Roman", size=16, color='black'))
        fig4.update_traces(marker=dict(line=dict(color='black', width=2)))
        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)


def convert_p2rank_fpocket(text):
    # 去掉列表的方括号和空格，然后按逗号分割字符串
    elements = text.strip('[]').split(',')
    # 提取每个元素的编号部分，并转换为整数
    numbers = [int(element.split('_')[1]) for element in elements]
    # 将数字排序
    numbers.sort()
    # 构建结果字符串
    result = ':-:'.join([f'L.{number}' for number in numbers]) + ':-:L'
    return result


# fpocket计算p2rank的描述符
# fpocket -f 1BZQ.pdb -P 103:-:L.118:-:L.119:-:L.120:-:L.44:-:L.50:-:L -d > 1BZQ_des_d.csv

# p2rank重排序fpocket的口袋
# prank fpocket-rescore -fpocket_command "fpocket" -f 1BZQ.pdb -fpocket_keep_output 1 -o ./prank2fpocket -c rescore_2024

