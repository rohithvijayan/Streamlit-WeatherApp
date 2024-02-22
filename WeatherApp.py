import requests
import streamlit as st

api_key = "a833da2ea0ffccd99997fa69e7cf0f81"
st.set_page_config(page_title="Weather App",
                   page_icon="https://icons.iconarchive.com/icons/fasticon/hand-draw-iphone/128/Weather-icon.png")


def find_current_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    weather_data = requests.get(url).json()
    # st.write(weather_data)
    try:
        general = weather_data["weather"][0]["main"]
        general_desc = weather_data["weather"][0]["description"]
        icon_id = weather_data["weather"][0]["icon"]
        temperature = weather_data["main"]["temp"]
        icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("city not found")
        st.stop()
    return general, general_desc, temperature, icon


def main():
    st.header("Find The Weather")
    city = st.text_input(label="City Name", placeholder="Enter City Name").lower()
    if st.button("Find"):
        general, general_desc, temperature, icon = find_current_weather(city)

        col_1, col_2 = st.columns(2)
        with col_1:
            st.title(general)
            st.subheader(general_desc)
        with col_2:
            st.header(temperature)
            st.image(icon)


if __name__ == '__main__':
    main()
