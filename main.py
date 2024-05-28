import streamlit as st
from daima_1 import generate_script

st.title("节日祝福语生成器")

name= st.text_input("💡 请输入祝福对象的姓名")
festival = st.text_input("💡 请输入节日名称")
creativity = st.slider("✨ 请输入祝福语的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)
submit = st.button("生成祝福语")


if submit and not name:
    st.info("请输入祝福对象姓名")
    st.stop()
if submit and not festival:
    st.info("请输入节日名称")
    st.stop()
if submit:
    with st.spinner("AI正在思考中，请稍等..."):
        script = generate_script(name, festival, creativity)
    st.success("祝福语已生成！")
    st.subheader("🔥 节日祝福语：")
    st.write(script)

