import requests
import streamlit as st

# Prepare API key and API url
api_key = "Tu2ggKINNd7h2YS4EtVaicAchPQduwhLWjtVNwcv"

        # This URL - gives us the whole content of the atrology pic of the day context.
        # When you have these, and call for them with the requests.get(url), then have it in dictionaries
        # like the .json() - we can click debug, and go through the type of file and what is contained in what
        # from here.
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

        # at the end of the link add "?" then api_key="ur api key".


#Get the request data as a dictionary
response = requests.get(url)
data = response.json()


# Extract the image title, url and, explanation.
title = data["title"]          # these dictionary keys we know represent what they rep because we saw it - when we debug and see the data dictionary.
date = data["date"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_path = "img.png"
response2 = requests.get(image_url)              # basically running the image code.
with open(image_path, "wb") as file:
    file.write(response2.content)

st.title(title)
st.write(date)
st.image(image_path)
st.write(explanation)



# with open("image.jpg", "wb") as file:
    # file.write(response.content)

