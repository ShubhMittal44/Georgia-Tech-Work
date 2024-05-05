import streamlit as st
import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import app_main as backend
import os

# Configure seaborn style
sns.set_theme(style="darkgrid")

# Visualization functions
def bar_chart(df, x_field, y_field):
    """Generate a bar chart using seaborn."""
    try:
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x=x_field, y=y_field)
        plt.title(f"Comparison of {y_field} and {x_field}")
        plt.xlabel(x_field)
        plt.ylabel(y_field)
        st.pyplot(plt)
    except Exception as error:
        st.error(f"Error drawing bar chart: {error}")


def box_plot(df, x_field, y_field):
    """Create a box plot using seaborn."""
    try:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=x_field, y=y_field)
        plt.title(f"Box Plot of {y_field} across {x_field}")
        plt.xlabel(x_field)
        plt.ylabel(y_field)
        st.pyplot(plt)
    except Exception as error:
        st.error(f"Error creating box plot: {error}")


def heatmap(df, x_field, y_field):
    """Create a heatmap to show correlations using seaborn."""
    try:
        # Generate a correlation matrix between the two fields
        correlation_data = df[[x_field, y_field]].corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_data, annot=True, cmap='coolwarm', square=True)
        plt.title(f"Correlation Heatmap between {x_field} and {y_field}")
        st.pyplot(plt)
    except Exception as error:
        st.error(f"Heatmap creation error: {error}")


def violin_plot(df, x_field, y_field):
    """Generate a violin plot using seaborn."""
    try:
        plt.figure(figsize=(10, 6))
        sns.violinplot(data=df, x=x_field, y=y_field)
        plt.title(f"Violin Plot of {y_field} across {x_field}")
        plt.xlabel(x_field)
        plt.ylabel(y_field)
        st.pyplot(plt)
    except Exception as error:
        st.error(f"Error creating violin plot: {error}")


# Data processing functions
def response_to_dataframe(json_data):
    """Convert JSON response to DataFrame while ensuring appropriate keys."""
    try:
        keys = list(json_data.keys())
        if len(keys) < 2:
            st.error("JSON must have at least two fields.")
            return None, None, None

        x_field = keys[0]
        y_field = keys[1]
        x_vals = json_data.get(x_field, [])
        y_vals = json_data.get(y_field, [])

        if len(x_vals) != len(y_vals):
            st.error(f"Length mismatch between '{x_field}' and '{y_field}'.")
            return None, None, None

        data_entries = [{x_field: x, y_field: y} for x, y in zip(x_vals, y_vals)]
        df = pd.DataFrame(data_entries)
        df[y_field] = pd.to_numeric(df[y_field], errors='coerce')
        return df, x_field, y_field
    except Exception as error:
        st.error(f"Data processing error: {error}")
        return None, None, None


# Main application
def app_main():
    """Load ticker files and provide UI for data visualization."""
    document_dir = "documents"
    available_files = [f for f in os.listdir(document_dir) if f.endswith('.txt')]

    st.title("Financial Services Innovation Lab, Georgia Tech Programming Task for Summer Research")
    selected_file = st.selectbox('Choose the required file:', available_files)
    query = st.text_input('Prompt')

    if st.button('Submit Query'):
        context = []
        response = backend.get_gemini_answer(query, context)

        st.subheader('Answer:')
        st.write(response)

        json_response = json.loads(response)
        df, x_field, y_field = response_to_dataframe(json_response)

        if df is not None:
            st.subheader('Bar Chart')
            bar_chart(df, x_field, y_field)

            st.subheader('Box Plot')
            box_plot(df, x_field, y_field)

            st.subheader('Heatmap')
            heatmap(df, x_field, y_field)

            st.subheader('Violin Plot')
            violin_plot(df, x_field, y_field)

if __name__ == '__main__':
    app_main()
