url = f"https://docs.google.com/spreadsheets/d/{1nctiWcQFaB5UlIs6z8d1O6ZgMHFDMAoo3twVxYnBUws}/gviz/tq?tqx=out:csv&sheet={charlas}"
df = pd.read_csv(url, dtype=str)


# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Python Talks Search Engine", page_icon="🐍", layout="wide")
st.title("Python Talks Search Engine")

# Connect to the Google Sheet
sheet_id = "1nctiWcQFaB5UlIs6z8d1O6ZgMHFDMAoo3twVxYnBUws"
sheet_name = "charlas"
url = f"<https://docs.google.com/spreadsheets/d/{1nctiWcQFaB5UlIs6z8d1O6ZgMHFDMAoo3twVxYnBUws}/gviz/tq?tqx=out:csv&sheet={charlas}>"
df = pd.read_csv(url, dtype=str).fillna("")

# Show the dataframe (we'll delete this later)
st.write(df)

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search videos by title or speaker", value="")

# Filter the dataframe using masks
m1 = df["Autor"].str.contains(text_search)
m2 = df["Título"].str.contains(text_search)
df_search = df[m1 | m2]

# Show the results, if you have a text_search
if text_search:
    st.write(df_search)

# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.caption(f"{row['Evento'].strip()} - {row['Lugar'].strip()} - {row['Fecha'].strip()} ")
            st.markdown(f"**{row['Autor'].strip()}**")
            st.markdown(f"*{row['Título'].strip()}*")
            st.markdown(f"**{row['Video']}**")
