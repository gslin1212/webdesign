
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error: {e}")
            return None
        return df
    return None

def visualize_data(df, x_axis, y_axis, plot_type):
    if plot_type == 'Bar':
        fig = plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x=x_axis, y=y_axis)
    elif plot_type == 'Line':
        fig = plt.figure(figsize=(10, 6))
        plt.plot(df[x_axis], df[y_axis], marker='o')
    elif plot_type == 'Scatter':
        fig = plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=x_axis, y=y_axis)
    else:
        st.error("Unsupported plot type selected.")
        return None
    return fig

# Streamlit widgets to interact with the user
st.title("CSV Data Processor")
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    if df is not None:
        # Display dataframe
        st.write("### Original Data")
        st.write(df)

        # Select options for visualization
        st.write("### Data Visualization")
        plot_type = st.selectbox("Select Plot Type", ['Bar', 'Line', 'Scatter'])
        available_columns = df.columns.tolist()
        x_axis = st.selectbox("Select X-axis", available_columns)
        y_axis = st.selectbox("Select Y-axis", available_columns)

        if st.button("Generate Plot"):
            fig = visualize_data(df, x_axis, y_axis, plot_type)
            if fig is not None:
                st.pyplot(fig)
