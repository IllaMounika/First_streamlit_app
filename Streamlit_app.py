import streamlit 
streamlit.title('My Parents New History Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🍝Omega 3 & blueberry Oatmeal')
streamlit.text('🥦Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥝🍞Avocado Toast')
streamlit.header('🍌🍓Build Your Own Fruit Smoothie 🥝🍇')
import pandas 
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruits_macros.txt")
streamlit.dataframe(my_fruit_list)
