import streamlit as st
import pandas as pd 
import plotly.express as px 
 

st.sidebar.title ("Top 650 Players FIFA 22")
x = st.sidebar.selectbox("select from ",["Home","Table","Visualization"])
if x == "Home":
    st.title('Hello in my assignment !')
    st.image ("https://th.bing.com/th/id/OIP._g7Ej43LSuhz9lVYSn8hDwHaEK?pid=ImgDet&rs=1", width = 800)
    st.markdown(
"""
# Top 650 Players FIFA 22 	
## My project talks about Top 650 Players FIFA 22
#### the table contain : short name of player, long name of player, overall, age, data of birth,height_cm, weight_kg,club_position,Position, club_name, league_name, nationality_name, club_jersey_number,preferred_foot,weak_foot, skill_moves, player_traits, pace, shooting, passing,dribbling,defending,physic,attacking,skill,movement,power,mentality
"""
)
df = pd.read_csv("Top_650_FIFA.csv")
if x == "Table":
    df = pd.read_csv("Top_650_FIFA.csv")
    st.write  (df)
if x ==  "Visualization":
    A= df['age'].unique().tolist()
    B = df ['club_position'].unique().tolist()
    b = st.selectbox ("which club_position would you like to see ?", B, 0)
    df = df[df['club_position'] == b]
    fig = px.scatter(df, x="age", y="club_position",size="overall",color="club_name")
    fig.update_layout(width=800, height=600)
    st.write(fig)

    X = df['age'].unique().tolist()
    Y = df ['club_jersey_number'].unique().tolist()
    y = st.selectbox ("which club_jersey_number would you like to see ?", Y, 0)
    df = df[df['club_jersey_number'] == y]
    fig1 = px.pie(df, values = "club_jersey_number",names= "dribbling")
    fig1.update_layout(width=800, height=600)
    st.write(fig1)
