# Add this to your app.py to filter by hierarchy
st.sidebar.header("Filter by Hierarchy")
selected_auh = st.sidebar.selectbox("Select AUH", df['AUH'].unique())
selected_sm = st.sidebar.selectbox("Select Senior Manager", df[df['AUH'] == selected_auh]['Senior_Manager'].unique())
selected_mgr = st.sidebar.selectbox("Select Sales Manager", df[df['Senior_Manager'] == selected_sm]['Sales_Manager'].unique())

# Filtered view
final_df = df[df['Sales_Manager'] == selected_mgr]
st.write(f"Performance for team under {selected_mgr}")
st.dataframe(final_df)
