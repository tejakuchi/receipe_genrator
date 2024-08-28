import openai
import streamlit as st
import os  # To access environment variables

# Initialize OpenAI API with environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate a recipe based on ingredients and cuisine type
def generate_recipe(ingredients, cuisine):
    prompt = (
        f"Create a detailed and complete {cuisine} recipe using the following ingredients: "
        f"{', '.join(ingredients)}. Please include step-by-step cooking instructions."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates detailed recipes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,  # Adjust as needed
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# Streamlit App
st.title("AI-Powered Recipe Generator")

# Input ingredients
ingredients = st.text_input("Enter the ingredients (comma separated):")

# Cuisine options
cuisine_options = ["Italian", "Mexican", "Indian", "Chinese", "French", "Japanese", "Mediterranean", "Thai", "American", "Greek"]
cuisine = st.selectbox("Select the cuisine type:", cuisine_options)

if st.button("Generate Recipe"):
    if ingredients:
        ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
        recipe = generate_recipe(ingredients_list, cuisine)
        st.subheader("Generated Recipe")
        st.write(recipe)
    else:
        st.write("Please enter the ingredients.")
