
import streamlit as st
st.set_page_config(page_title="Trac nghiem tinh cach", page_icon=":question:", layout='wide')
st.title('Trac nghiem tinh cach')
st.write('Hay chon 1 con vat, toi se cho ban biet tinh cach cua ban')
Tinh_cach = {
    'con meo': 'Ban co ve thich nghi ngoi',
    'con cho': 'Ban co ve kha chung thanh, nang dong',
    'con su tu': 'Ban co ve kha manh me, thich dan dau',
    'con ngua': 'Ban yeu thich su tu do',
    'thien nga':'Ban co ve ngoai kha la thu hut!'}
cols = st.columns(len(Tinh_cach))
chon = None
for i, (con_vat, tinh_cach) in enumerate(Tinh_cach.items()):
    with cols[i]:
        if cols[i].button(con_vat):
            chon = con_vat
if chon:
    with st.expander(chon):
         st.write(Tinh_cach[chon])
with st.sidebar:
    st.write('Trac nghiem tinh cach')
    if chon:
        st.success(f'Con vat ban chon la: {chon}')
        st.write(Tinh_cach[chon])
    else:
        st.info('Hay chon 1 con vat')
