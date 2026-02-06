import streamlit as st
import google.generativeai as genai
import os

# 1. Setup Gemini
# Replace 'YOUR_API_KEY' with your actual key or use environment variables
API_KEY = "AIzaSyDMtOwtoyaojUnpxbGjErQgzgHwP1DZdEQ" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')

st.title("🍲 Leftover Alchemist")
st.write("Turn your noon leftovers into a brand-new dinner!")

# 2. User Input
leftover_food = st.text_input("What is left over from lunch?", placeholder="e.g., Toor Dal, Rice, Roasted Veggies")

if st.button("Transform for Dinner"):
    if leftover_food:
        # 3. The Prompt (The instructions for the AI)
        prompt = f"""
        I have leftover {leftover_food} from lunch. 
        Give me 3 creative ideas on how to transform this into a completely different dish for dinner. 
        For each idea:
        1. Give it a catchy name.
        2. List any 'extension' ingredients needed.
        3. Give 3 simple cooking steps.
        Format the output clearly using bold headers.
        """
        
        with st.spinner('Chef Gemini is thinking...'):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:

        st.warning("Please enter an ingredient first!")
