import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🚚 Logistics Pricing Optimization Engine")

# Load compiled predictive file
df = pd.read_csv("dashboard_pricing_data.csv")

# --- SIDEBAR INTERACTIVE FILTERS & SLICERS ---
st.sidebar.header("Dashboard Slicers")
selected_origin = st.sidebar.multiselect("Origin Hub", options=df['Origin'].unique(), default=df['Origin'].unique())
selected_mode = st.sidebar.multiselect("Transport Mode", options=df['Transport_Mode'].unique(), default=df['Transport_Mode'].unique())
weight_slider = st.sidebar.slider("Maximum Cargo Weight (Lbs)", int(df['Weight_Lbs'].min()), int(df['Weight_Lbs'].max()), int(df['Weight_Lbs'].max()))

# Filter dataset dynamically based on UI selection
filtered_df = df[
    (df['Origin'].isin(selected_origin)) & 
    (df['Transport_Mode'].isin(selected_mode)) & 
    (df['Weight_Lbs'] <= weight_slider)
]

# --- DASHBOARD METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Shipments Routed", len(filtered_df))
col2.metric("Avg Actual Price Paid", f"${filtered_df['Actual_Price_USD'].mean():.2f}")
col3.metric("Avg Predicted Price Model", f"${filtered_df['Predicted_Price_USD'].mean():.2f}")

# --- DASHBOARD GRAPH VISUALIZATIONS ---
st.subheader("Model Performance: Actual Costs vs. Model Projections")
fig = px.scatter(filtered_df, x="Actual_Price_USD", y="Predicted_Price_USD", color="Transport_Mode",
                 hover_data=["Origin", "Destination", "Distance_Miles"],
                 labels={"Actual_Price_USD": "Actual Invoice ($)", "Predicted_Price_USD": "Model Forecast ($)"})
st.plotly_chart(fig, use_container_width=True)
