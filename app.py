import streamlit as st
import google.generativeai as genai

# Gemini Setup
API_KEY = "AIzaSyDMtOwtoyaojUnpxbGjErQgzgHwP1DZdEQ"  # તમારી API Key અહીં નાખો
genai.configure(api_key=API_KEY)

# ૨૦૨૬ ના લેટેસ્ટ મોડેલનો ઉપયોગ
model = genai.GenerativeModel('gemini-3-flash-preview') # અથવા 'gemini-2.0-flash'

# App નું ગુજરાતી ટાઈટલ
st.title("🍲 રસોઈ : બપોરનું જમણ, સાંજની મિજબાની")
st.subheader("બપોરની વધેલી રસોઈમાંથી બનાવો સાંજ માટે ટેસ્ટી વાનગી!")

# User Input in Gujarati
leftover_food = st.text_input("બપોરે શું વધ્યું છે?", placeholder="દા.ત. તુવેરની દાળ, ભાત, રોટલી")

if st.button("નવી વાનગી બતાવો ✨"):
    if leftover_food:
        # Prompt ને ગુજરાતીમાં સૂચના આપવી
        prompt = f"""
        મારી પાસે બપોરના જમવામાંથી '{leftover_food}' વધ્યું છે. 
        તેનો ઉપયોગ કરીને રાત્રે કઈ નવી વાનગી બનાવી શકાય તેના 3 બેસ્ટ આઈડિયા આપો.
        જવાબ નીચે મુજબ આપવો:
        1. વાનગીનું નામ.
        2. જરૂરી વધારાની સામગ્રી.
        3. બનાવવાની રીત (ટૂંકમાં).
        બધી જ માહિતી શુદ્ધ ગુજરાતીમાં આપવી.
        """
        
        with st.spinner('શું શું બનાવી સકી ??...'):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"ભૂલ આવી છે: {e}")
    else:
        st.warning("મહેરબાની કરીને સામગ્રીનું નામ લખો!")



