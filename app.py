import streamlit as st
import joblib

# Load model
model = joblib.load("rf_energy_model.pkl")

# --- Page setup ---
st.set_page_config(page_title="Energy Predictor", page_icon="⚡", layout="centered")

# --- Background color ---
st.markdown(
    """
    <style>
    /* Entire app background black */
    .css-18e3th9 {background-color: #000000 !important;}
    .css-1d391kg {background-color: #000000 !important;}
    .main {background-color: #000000 !important;}
    
    /* Text color white */
    body, .stText, .stMarkdown, .stButton, .stNumberInput, .stSelectbox {
        color: #FFFFFF !important;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #00FFFF !important; /* cyan for headings */
    }

    /* Metric numbers */
    .stMetricValue {
        color: #FFD700 !important; /* gold color */
    }

    /* Info boxes */
    .stAlert {
        background-color: #111111 !important;
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# --- Heading & Summary ---
st.markdown("<h1 style='text-align: center; font-weight: bold; color: #2E86C1;'>🏠 Household Energy Consumption Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-weight: bold; color: #1B4F72;'>Estimate your monthly energy consumption & electricity bill!</h3>", unsafe_allow_html=True)
st.markdown("---")

# --- Session state for step flow ---
if "step" not in st.session_state:
    st.session_state.step = 0

# --- Step 0: Name input ---
if st.session_state.step == 0:
    user_name = st.text_input("Enter Your Name", value="User")
    start = st.button("Start Inputs")
    if start and user_name.strip() != "":
        st.session_state.step = 1
        st.session_state.user_name = user_name

# --- Step 1: Appliance counts ---
if st.session_state.step == 1:
    user_name = st.session_state.user_name
    st.markdown(f"### Hello **{user_name}**, enter your appliance details below:")

    if "appliances" not in st.session_state:
        st.session_state.appliances = {
            "Fans": {"count": 0, "hours": 0},
            "ACs": {"count": 0, "hours": 0},
            "Fridges": {"count": 0, "hours": 24},  # always on
            "TVs": {"count": 0, "hours": 0},
            "Laptops": {"count": 0, "hours": 0},
            "Washing Machines": {"count": 0, "hours": 0}
        }

    for app in st.session_state.appliances:
        st.session_state.appliances[app]["count"] = st.number_input(f"Number of {app}", min_value=0, max_value=10, value=st.session_state.appliances[app]["count"], step=1)

    next_step = st.button("Next")
    if next_step:
        st.session_state.step = 2

# --- Step 2: Daily usage & tariff ---
if st.session_state.step == 2:
    appliances = st.session_state.appliances
    st.markdown("### Do you want to calculate **daily consumption and monthly bill**?")
    show_usage = st.radio("", ("No", "Yes"))

    if show_usage == "Yes":
        st.markdown("### Select Daily Usage Hours (Dropdown):")
        hours_options = [i for i in range(0, 25)]
        for app in appliances:
            if appliances[app]["count"] > 0 and app != "Fridges":
                appliances[app]["hours"] = st.selectbox(f"Daily Hours for {app}", options=hours_options, index=1)

        tariff = st.number_input("Enter your electricity tariff (Rs per kWh)", min_value=0.0, value=8.0, step=0.1)

        calculate = st.button("Calculate")
        if calculate:
            input_features = [[
                appliances["Fans"]["count"], appliances["ACs"]["count"], appliances["Fridges"]["count"],
                appliances["TVs"]["count"], appliances["Laptops"]["count"], appliances["Washing Machines"]["count"],
                appliances["Fans"]["hours"], appliances["ACs"]["hours"], appliances["Fridges"]["hours"],
                appliances["TVs"]["hours"], appliances["Laptops"]["hours"], appliances["Washing Machines"]["hours"]
            ]]

            prediction = model.predict(input_features)[0]
            bill = prediction * tariff
            daily_consumption = sum([appliances[app]["count"] * appliances[app]["hours"] for app in appliances])

            col1, col2 = st.columns(2)
            col1.metric("Monthly Energy Consumption (kWh)", f"{prediction:.2f}")
            col2.metric("Estimated Monthly Bill (₹)", f"{bill:.2f}")

            st.info(f"Approximate daily energy usage (kWh-equivalent units): {daily_consumption:.2f}")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #2E86C1;'>Made with ❤️ by <b>MOHAMMAD HASSAN KHALID</b></p>", unsafe_allow_html=True)
