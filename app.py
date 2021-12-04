from Libraries import *
import streamlit as st

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
   .sidebar .sidebar-content {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Covid-19 Visualization Dashboard</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title('Adjust your Parameters of the Covid Dashboard')
countries = ['United States', 'United Kingdom', 'Australia', 'China', 'Egypt', 'Sri Lanka', 'France', 'Canada', 'India', 'Brazil', 'Denmark', 'Turkey', 'Vietnam', 'Argentina', 'Mexico', 'Japan']
data_types = ['cases', 'deaths', 'recovered']
country_code = {'Sri Lanka': 'lk', 'United States': 'us', 'United Kingdom': 'gb',
                'China': 'cn', 'India': 'in', 'Mexico': 'mx', 'Denmark': 'dk', 'Brazil': 'br', 'France': 'fr', 'Vietnam': 'vn', 'Argentina': 'ar', 'Japan': 'jp', 'Canada': 'ca', 'Turkey': 'tr', 'Australia': 'au', 'Egypt': 'eg'}

data_types = ['cases', 'deaths', 'recovered']
country = st.sidebar.selectbox('Select the Country', countries)

days = st.sidebar.slider('Select the no. of Days', min_value=1, max_value=100)
data_type = st.sidebar.multiselect('Select the data types', data_types)

total_cases = get_historic_cases(country, str(days))
total_deaths = get_historic_deaths(country, str(days))
total_recoveries = get_historic_recoveries(country, days)
total_df = pd.concat([total_cases, total_deaths, total_recoveries], axis=1).astype(int)

daily_cases = get_daily_cases(country, str(days))
daily_deaths = get_daily_deaths(country, str(days))
daily_recoveries = get_daily_recoveries(country, str(days))
daily_df = pd.concat([daily_cases, daily_deaths, daily_recoveries], axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)

col1, col2 = st.columns(2)
col1.metric(label="Selected Country", value=country)
col2.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")

col1, col2, col3 = st.columns(3)
col1.metric('Total Cases', yesterday_cases)
col2.metric('Total Deaths', yesterday_deaths)
col3.metric('Total Recovered', yesterday_recoveries)

st.line_chart(daily_df[data_type])
st.bar_chart(daily_df[data_type])

st.markdown("<h1 style='text-align: center;'>Let's look at the inside of the Covid-19 virus</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

st.image('zdiagram.jpg')

st.markdown("<h1 style='text-align: center;'>Do you know what happens when you get Covid-19 Virus?</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

st.video('https://www.youtube.com/watch?v=5DGwOJXSxqg')

st.markdown("<h1 style='text-align: center;'>How to prevent from Covid-19 Virus?</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

st. write('These are some of the health regulations you will have to follow in order to get rid from covid-19.')
st.image('stay-safe-en.jpg')

st.markdown("<h1 style='text-align: center;'>Thank you!</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Made by Yomin Rajapakshe</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    }
    </style>
    """, unsafe_allow_html=True)