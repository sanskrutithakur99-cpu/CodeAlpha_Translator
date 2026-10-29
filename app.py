import streamlit as st
from deep_translator import MyMemoryTranslator
from deep_translator.exceptions import LanguageNotSupportedException

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translator")
st.write("Translate text between different languages in seconds!")

languages = {
    "English": "en-GB",
    "Hindi": "hi-IN",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "German": "de-DE",
    "Japanese": "ja-JP",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar-SA",
    "Bengali": "bn-IN",
    "Urdu": "ur-PK",
    "Marathi": "mr-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Punjabi": "pa-IN",
    "Gujarati": "gu-IN",
    "Korean": "ko-KR",
    "Russian": "ru-RU",
    "Portuguese": "pt-PT"
}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Translate from",
        list(languages.keys()),
        index=0
    )

with col2:
    target_language = st.selectbox(
        "Translate to",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter text",
    placeholder="Type something to translate...",
    height=150
)

if st.button("Translate 🌐", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text first.")
    elif source_language == target_language:
        st.warning("Please select two different languages.")
    else:
        try:
            with st.spinner("Translating..."):
                translated_text = MyMemoryTranslator(
                    source=languages[source_language],
                    target=languages[target_language]
                ).translate(text.strip())

            st.subheader("Translation")
            st.success(translated_text)
            st.caption(
                f"{source_language} → {target_language}"
            )

            st.download_button(
                "Download translation",
                data=translated_text,
                file_name="translated_text.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:
                st.error(f"Translation failed: {e}")

st.divider()
st.caption("Built with Python, Streamlit and deep-translator.")