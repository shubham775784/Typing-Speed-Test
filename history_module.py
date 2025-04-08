# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# def show_history():
#     st.header("📊 Score Graphs & Performance History")
#     try:
#         df = pd.read_csv("user_data.csv", names=["name", "speed", "accuracy", "difficulty"])
#         name = st.text_input("Enter your name to view history:")
#         user_df = df[df['name'] == name]

#         if user_df.empty:
#             st.warning("No data found for this user.")
#             return

#         st.subheader("Performance Table")
#         st.dataframe(user_df.reset_index(drop=True))

#         # Graph
#         fig, ax = plt.subplots()
#         ax.plot(user_df.index + 1, user_df['speed'], label='Speed (WPM)', marker='o')
#         ax.plot(user_df.index + 1, user_df['accuracy'], label='Accuracy (%)', marker='s')
#         ax.set_title("Typing Performance Over Time")
#         ax.set_xlabel("Test Number")
#         ax.set_ylabel("Metrics")
#         ax.legend()
#         ax.grid(True)
#         st.pyplot(fig)

#     except FileNotFoundError:
#         st.error("No performance data available.")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

SAVE_PATH = "C:/Users/gouta/Documents/user_data.csv"

def show_history():
    st.header("📊 Score Graphs & Performance History")

    try:
        df = pd.read_csv(SAVE_PATH, names=["name", "speed", "accuracy", "difficulty", "characters_typed", "timestamp"])

        name = st.text_input("Enter your name to view history:")
        if not name:
            return

        user_df = df[df['name'] == name]

        if user_df.empty:
            st.warning("No data found for this user.")
            return

        st.subheader("Performance Table")
        st.dataframe(user_df.reset_index(drop=True))

        # Delete by timestamp
        selected_row = st.selectbox("Select a timestamp to delete:", user_df["timestamp"].unique())
        if st.button("Delete Selected Entry"):
            df = df[~((df["name"] == name) & (df["timestamp"] == selected_row))]
            df.to_csv(SAVE_PATH, index=False, header=False)
            st.success(f"✅ Deleted entry for {name} on {selected_row}")
            st.rerun()

        # Graph
        fig, ax = plt.subplots()
        ax.plot(user_df.index + 1, user_df['speed'], label='Speed (WPM)', marker='o')
        ax.plot(user_df.index + 1, user_df['accuracy'], label='Accuracy (%)', marker='s')
        ax.set_title("Typing Performance Over Time")
        ax.set_xlabel("Test Number")
        ax.set_ylabel("Metrics")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    except FileNotFoundError:
        st.error("🚫 No performance data available.")

show_history()

