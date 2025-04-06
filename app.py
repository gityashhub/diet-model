# import streamlit as st
# import requests
# import re
# import logging
# import time

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # Replace with your actual Hugging Face Inference API Token
# API_TOKEN = "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"
# API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"

# headers = {"Authorization": f"Bearer {API_TOKEN}"}

# def query_huggingface(payload, max_retries=5):
#     for attempt in range(max_retries):
#         try:
#             response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
#             response.raise_for_status()
#             logger.debug(f"API Response (attempt {attempt + 1}): {response.json()}")
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             logger.warning(f"Attempt {attempt + 1} failed: {e}")
#             if attempt < max_retries - 1:
#                 time.sleep(2 ** (attempt + 1))
#             else:
#                 logger.error(f"All attempts failed: {e}")
#                 return {"error": str(e)}

# # Streamlit app
# def main():
#     st.title("Diet and Workout Recommendation System")

#     # Input form
#     with st.form(key="recommendation_form"):
#         age = st.text_input("Age", "")
#         gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])
#         weight = st.text_input("Weight (e.g., 70 kg)", "")
#         height = st.text_input("Height (e.g., 170 cm)", "")
#         veg_or_noveg = st.selectbox("Diet Preference", ["", "Vegetarian", "Non-Vegetarian"])
#         disease = st.text_input("Any Generic Disease (optional)", "")
#         region = st.text_input("Region", "Unknown Region")
#         allergics = st.text_input("Allergies (optional)", "")
#         foodtype = st.text_input("Preferred Food Type (optional)", "")
#         submit_button = st.form_submit_button(label="Get Recommendations")

#     # Process form submission
#     if submit_button:
#         # Validate required fields
#         if not all([age, gender, weight, height, veg_or_noveg, region]):
#             st.error("❌ Please fill in all required fields (Age, Gender, Weight, Height, Veg/Non-Veg, Region).")
#             return

#         # Construct prompt (same as before)
#         prompt = (
#             "You are a Diet and Workout Recommendation System. Based on the following criteria, generate exactly 6 unique restaurant names, 6 unique breakfast options, 5 unique dinner options, and 6 unique workout plans tailored to the specified region. Use the exact format below with numbered lists, ensuring no repetition, and include only the requested items without extra text.\n"
#             "Format:\n"
#             "Restaurants:\n1. [Restaurant 1]\n2. [Restaurant 2]\n3. [Restaurant 3]\n4. [Restaurant 4]\n5. [Restaurant 5]\n6. [Restaurant 6]\n"
#             "Breakfast:\n1. [Breakfast 1]\n2. [Breakfast 2]\n3. [Breakfast 3]\n4. [Breakfast 4]\n5. [Breakfast 5]\n6. [Breakfast 6]\n"
#             "Dinner:\n1. [Dinner 1]\n2. [Dinner 2]\n3. [Dinner 3]\n4. [Dinner 4]\n5. [Dinner 5]\n"
#             "Workouts:\n1. [Workout 1]\n2. [Workout 2]\n3. [Workout 3]\n4. [Workout 4]\n5. [Workout 5]\n6. [Workout 6]\n"
#             "Criteria:\n"
#             f"Person age: {age}\n"
#             f"Person gender: {gender}\n"
#             f"Person weight: {weight}\n"
#             f"Person height: {height}\n"
#             f"Person veg_or_nonveg: {veg_or_noveg}\n"
#             f"Person generic disease: {disease}\n"
#             f"Person region: {region}\n"
#             f"Person allergics: {allergics}\n"
#             f"Person foodtype: {foodtype}"
#         )

#         with st.spinner("Generating recommendations..."):
#             try:
#                 response = query_huggingface({"inputs": prompt, "max_length": 500, "temperature": 0.7})
#                 if "error" in response:
#                     st.error(f"❌ An error occurred: {response['error']}")
#                     return
#                 generated_text = response[0]["generated_text"] if isinstance(response, list) and len(response) > 0 and "generated_text" in response[0] else response.get("generated_text", "")

#                 if not generated_text:
#                     st.error(f"❌ No valid response generated. Raw output: {generated_text}")
#                     return

#                 # Parse output (same as before)
#                 restaurant_names = list(dict.fromkeys(re.findall(r'Restaurants:\s*[\d\.]+\.\s*([^\n]+)', generated_text, re.DOTALL)))
#                 restaurant_names = [name.strip() for name in restaurant_names[:6] if name.strip()]

#                 breakfast_names = list(dict.fromkeys(re.findall(r'Breakfast:\s*[\d\.]+\.\s*([^\n]+)', generated_text, re.DOTALL)))
#                 breakfast_names = [name.strip() for name in breakfast_names[:6] if name.strip()]

#                 dinner_names = list(dict.fromkeys(re.findall(r'Dinner:\s*[\d\.]+\.\s*([^\n]+)', generated_text, re.DOTALL)))
#                 dinner_names = [name.strip() for name in dinner_names[:5] if name.strip()]

#                 workout_names = list(dict.fromkeys(re.findall(r'Workouts:\s*[\d\.]+\.\s*([^\n]+)', generated_text, re.DOTALL)))
#                 workout_names = [name.strip() for name in workout_names[:6] if name.strip()]

#                 if not (restaurant_names or breakfast_names or dinner_names or workout_names):
#                     st.error("❌ The model failed to generate valid recommendations. Please try again with different inputs or contact support.")
#                     return

#                 # Display results
#                 st.subheader(f"Recommendations for {region}")
#                 st.markdown("### Restaurants")
#                 for i, name in enumerate(restaurant_names, 1):
#                     st.write(f"{i}. {name}")

#                 st.markdown("### Breakfast")
#                 for i, name in enumerate(breakfast_names, 1):
#                     st.write(f"{i}. {name}")

#                 st.markdown("### Dinner")
#                 for i, name in enumerate(dinner_names, 1):
#                     st.write(f"{i}. {name}")

#                 st.markdown("### Workouts")
#                 for i, name in enumerate(workout_names, 1):
#                     st.write(f"{i}. {name}")

#             except Exception as e:
#                 st.error(f"❌ An error occurred: {str(e)}")

# if __name__ == "__main__":
#     main()


import streamlit as st
import requests
import re
import logging
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Hugging Face API config
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Set custom background
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1605296867304-46d5465a13f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1400&q=80");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.88);
            padding: 2rem 2rem;
            border-radius: 16px;
            backdrop-filter: blur(4px);
        }}
        h1 {{
            text-align: center;
            color: #084C61;
            font-weight: 800;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# API call
def query_huggingface(payload, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            logger.debug(f"API Response (attempt {attempt + 1}): {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** (attempt + 1))
            else:
                logger.error(f"All attempts failed: {e}")
                return {"error": str(e)}

# Main app
def main():
    set_background()

    st.title("🏋️‍♀️ Diet & Workout Recommendation System 🍽️")

    st.markdown("Fill in the details below to get personalized health recommendations 👇")

    with st.form(key="recommendation_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.text_input("🎂 Age", "")
            weight = st.text_input("⚖️ Weight (e.g., 70 kg)", "")
            veg_or_noveg = st.selectbox("🥗 Diet Preference", ["", "Vegetarian", "Non-Vegetarian"])
            disease = st.text_input("🩺 Any Generic Disease (optional)", "")
        with col2:
            gender = st.selectbox("🚻 Gender", ["", "Male", "Female", "Other"])
            height = st.text_input("📏 Height (e.g., 170 cm)", "")
            region = st.text_input("🌍 Region", "Unknown Region")
            allergics = st.text_input("❌ Allergies (optional)", "")

        foodtype = st.text_input("🍱 Preferred Food Type (optional)", "")
        submit_button = st.form_submit_button(label="🚀 Get Recommendations")

    if submit_button:
        if not all([age, gender, weight, height, veg_or_noveg, region]):
            st.error("❌ Please fill in all required fields.")
            return

        prompt = (
            "You are a Diet and Workout Recommendation System. Based on the following criteria, generate exactly 6 unique restaurant names, "
            "6 unique breakfast options, 5 unique dinner options, and 6 unique workout plans tailored to the specified region. Use the exact "
            "format below with numbered lists, ensuring no repetition, and include only the requested items without extra text.\n"
            "Format:\n"
            "Restaurants:\n1. [Restaurant 1]\n2. [Restaurant 2]...\n"
            "Breakfast:\n1. [Breakfast 1]...\n"
            "Dinner:\n1. [Dinner 1]...\n"
            "Workouts:\n1. [Workout 1]...\n"
            "Criteria:\n"
            f"Person age: {age}\n"
            f"Person gender: {gender}\n"
            f"Person weight: {weight}\n"
            f"Person height: {height}\n"
            f"Person veg_or_nonveg: {veg_or_noveg}\n"
            f"Person generic disease: {disease}\n"
            f"Person region: {region}\n"
            f"Person allergics: {allergics}\n"
            f"Person foodtype: {foodtype}"
        )

        with st.spinner("💡 Generating recommendations..."):
            try:
                response = query_huggingface({"inputs": prompt, "max_length": 500, "temperature": 0.7})
                if "error" in response:
                    st.error(f"❌ An error occurred: {response['error']}")
                    return

                generated_text = response[0]["generated_text"] if isinstance(response, list) and len(response) > 0 and "generated_text" in response[0] else response.get("generated_text", "")

                if not generated_text:
                    st.error(f"❌ No valid response generated. Raw output: {generated_text}")
                    return

                restaurant_names = re.findall(r"Restaurants:\n(.*?)\n\n", generated_text, re.DOTALL)
                breakfast_names = re.findall(r"Breakfast:\n(.*?)\n\n", generated_text, re.DOTALL)
                dinner_names = re.findall(r"Dinner:\n(.*?)\n\n", generated_text, re.DOTALL)
                workout_names = re.findall(r"Workouts:\n(.*?)$", generated_text, re.DOTALL)

                def parse_list(text):
                    return [line.split(". ", 1)[-1].strip() for line in text.strip().split("\n") if ". " in line]

                st.subheader(f"📍 Recommendations for **{region}**")

                if restaurant_names:
                    st.markdown("### 🍽️ Recommended Restaurants")
                    for i, name in enumerate(parse_list(restaurant_names[0])[:6], 1):
                        st.write(f"{i}. {name}")

                if breakfast_names:
                    st.markdown("### 🥣 Breakfast Options")
                    for i, name in enumerate(parse_list(breakfast_names[0])[:6], 1):
                        st.write(f"{i}. {name}")

                if dinner_names:
                    st.markdown("### 🍛 Dinner Options")
                    for i, name in enumerate(parse_list(dinner_names[0])[:5], 1):
                        st.write(f"{i}. {name}")

                if workout_names:
                    st.markdown("### 🏃‍♂️ Workout Plans")
                    for i, name in enumerate(parse_list(workout_names[0])[:6], 1):
                        st.write(f"{i}. {name}")

            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()



