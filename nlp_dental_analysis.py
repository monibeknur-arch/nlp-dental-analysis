import streamlit as st

st.set_page_config(page_title="Dental NLP", page_icon="🦷")

st.title("🦷 Стоматологиялық есептерді NLP талдау")
st.write("Медициналық есепті төменге енгізіңіз:")

# Мәтін енгізу
user_input = st.text_area("Есеп мәтіні:", height=150)

# Стоматологиялық терминдер сөздігі (NLP үшін қарапайым база)
keywords = {
    "Диагноз": ["пульпит", "кариес", "пародонтит", "гингивит", "стоматит"],
    "Симптомдар": ["ауырсыну", "ісіну", "қанау", "сезімталдық", "сыздап"],
    "Процедуралар": ["тазалау", "пломбалау", "рентген", "зондтау", "канал"]
}

if st.button("Талдауды бастау"):
    if user_input:
        st.subheader("📊 Талдау нәтижесі:")
        
        # Мәтінді кіші әріпке айналдыру
        text_lower = user_input.lower()
        
        # Экранды екі бағанға бөлу
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("🔍 Табылған терминдер:")
            found_any = False
            for category, terms in keywords.items():
                found_terms = [t for t in terms if t in text_lower]
                if found_terms:
                    st.write(f"**{category}:** {', '.join(found_terms)}")
                    found_any = True
            if not found_any:
                st.write("Арнайы терминдер табылмады.")

        with col2:
            st.info("📈 Статистика:")
            word_count = len(user_input.split())
            st.metric("Сөз саны", word_count)
            st.metric("Маңыздылығы", "Жоғары" if "ауырсыну" in text_lower else "Орташа")

        # Визуалды нәтиже
        st.success("✅ Текст сәтті өңделді. Жүйе бұл жағдайды 'Шұғыл' деп бағалайды.")
    else:
        st.warning("Алдымен мәтінді енгізіңіз!")
