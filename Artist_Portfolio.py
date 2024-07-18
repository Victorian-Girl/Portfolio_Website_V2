import streamlit as st


col1, col2 = st.columns(2)                                                                                              # Creating 2 columns in the layout

with col1:                                                                                                              # Adding content to the first column
    st.subheader("Hello! :wave:")                                                                                           # Adding a subheader
    st.title("Welcome to MCrist page")                                                                            # Adding a title

with col2:                                                                                                              # Adding content to the second column
    st.image("assets/logo5.png", width=200)                                                                                      # Adding an image

st.title(" ")

col1, col2 = st.columns(2)                                                                                              # Creating 2 columns in the layout
with col1:                                                                                                              # Adding content to the first column
    st.subheader("My artist web site")                                                                                  # Adding a subheader
    st.write("- Made with Adobe Illustrator")                                                                           # Adding a text
    st.write("- And a wonderfully app name Svija")                                                                      # Adding a text
    st.write("- Come see my art")                                                                                       # Adding a text
    st.write("- Know me better")                                                                                        # Adding a text
    st.write("- I'm am a programmer, but also a artist")                                                                # Adding a text

with col2:                                                                                                              # Adding content to the second column
    st.write("https://mcrist.artiste.svija.site/")                                                                      # Adding a web link
    st.image("images/site_2.png")                                                                                       # Adding an image

st.title(" ")                                                                                                           # Adding a blank space

st.title("My Artist Setup")                                                                                             # Adding a title
st.image("images/setup.jpg")                                                                                            # Adding an image

st.write(" ")

st.components.v1.html(                                                                                                  # Adding HTML content
    """
<html>
<head>
  <style>
    body {
      background-color: #ffffff; /* Existing background color */
    }
    #vis {
      border: 2px solid #ffffff; /* Add border to the chart container */
      padding: 20px; /* Add padding */
      margin: 20px; /* Add margin */
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Add box shadow */
      display: flex ; /* Make the container inline */
      justify-content: center; /* Center the chart */
    }
    @media (max-width: 768px) {
      #vis {
        padding: 10px; /* Adjust padding for smaller screens */
        margin: 10px; /* Adjust margin for smaller screens */
      }
    }
  </style>
  <script src="https://cdn.jsdelivr.net/npm/vega@5.30.0"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@5.19.0"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6.26.0"></script>
</head>
<body>
  <div id="vis"/>
  <script>
    const spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Reproducing http://robslink.com/SAS/democd91/pyramid_pie.htm",
  "data": {
    "values": [
      {"category": "Inspiration", "value": 35, "order": 3},
      {"category": "Preparation", "value": 35, "order": 4},
      {"category": "Painting", "value": 50, "order": 5},
      {"category": "New techniques", "value": 30, "order": 1},
      {"category": "Air brush", "value": 15, "order": 2}
    ]
  },
  "mark": {"type": "arc", "outerRadius":120},
  "encoding": {
    "theta": {
      "field": "value",
      "type": "quantitative",
      "scale": {"range": [2.35619449, 8.639379797]},
      "stack": true
    },
    "color": {
      "field": "category",
      "type": "nominal",
      "scale": {
        "domain": [
          "Inspiration",
          "Preparation",
          "Painting",
          "New techniques",
          "Air brush"
        ],
        "range": [ "#44A5A5","#14FA78", "#14FAFA", "#FA6914", "#FAA614"]
      },
      "legend": {
        "orient": "none",
        "title": null,
        "columns": 1,
        "legendX": 250,
        "legendY": 50,
        "labelFontSize": 15
      }
    },
    "order": {"field": "order"}
  },
  "config": {}
};
    vegaEmbed("#vis", spec, {mode: "vega-lite"}).then(console.log).catch(console.warn);
  </script>
</body>
</html>
    """,
    height=300,                                                                                                         # Setting the height of the HTML content
)


st.write(" ")
st.title("Art's Gallery")
st.subheader("- Some of them -")                                                                                            # Adding a subheader

col1, col2, col3 = st.columns(3)                                                                                        # Creating 3 columns in the layout

with col1:                                                                                                              # Adding content to the first column
    st.image("images/g.jpg")                                                                                            # Adding an image
    st.image("images/g1.jpg")
    st.image("images/g7.jpg")

with col2:                                                                                                              # Adding content to the second column
    st.image("images/g3.jpg")                                                                                           # Adding an image
    st.image("images/g4.jpg")
    st.image("images/g9.jpg")

with col3:                                                                                                              # Adding content to the third column
    st.image("images/g2.jpg")                                                                                           # Adding an image
    st.image("images/g5.jpg")
    st.image("images/g8.jpg")

st.subheader(" ")                                                                                                       # Adding a subheader
st.write("CONTACT")                                                                                                     # Adding a text
st.title("For any inquiries, email at:")                                                                                # Adding a title
st.subheader("Artist:  mcrist.artiste@gmail.com")                                                                       # Adding a subheader
