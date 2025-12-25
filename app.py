import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🐧 Penguen Türü Analiz Uygulaması")
st.markdown("Bu uygulama, penguenlerin fiziksel özelliklerini analiz eder.")

st.sidebar.header("Kullanıcı Giriş Paneli")

@st.cache_data 
def load_data():
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
    return pd.read_csv(url)

df = load_data()

island = st.sidebar.selectbox("Ada Seçiniz", df['island'].unique())
bill_length = st.sidebar.slider("Gaga Uzunluğu (mm)", 30.0, 60.0, 45.0) # [cite: 152]

st.subheader(f"{island} Adasındaki Penguenler")
filtered_df = df[df['island'] == island]
st.dataframe(filtered_df)

st.subheader("Gaga ve Yüzgeç Uzunluğu İlişkisi")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x="bill_length_mm", y="flipper_length_mm", hue="species", ax=ax)
st.pyplot(fig)

st.success("Analiz başarıyla tamamlandı!")