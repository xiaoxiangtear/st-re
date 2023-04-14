## 正则表达式
import streamlit as st
import re 

# str1 = '20191118-20201117,票面利率:0.2%;20201118-20211117,票面利率:0.4%;20211118-20221117,票面利率:0.6%;20221118-20231117,票面利率:0.8%;20231118-20241117,票面利率:1.2%;20241118-20251117,票面利率:2.0%'
# str2 = '在本次发行的可转债期满后5个交易日内，公司将按债券面值的106%（含最后一期利息）的价格赎回未转股的可转债。'

txt_input = st.text_area('请输入文本：')
re_input = st.text_input('请输入正则：')
btn = st.button('查询')
lt1 = re.findall(re_input, txt_input) 
if btn == True:
    st.write('查询结果为：')
    st.write(lt1)