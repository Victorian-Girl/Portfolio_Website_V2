import streamlit as st


col1, col2 = st.columns(2)                                                                                              # Creating 2 columns in the layout

with col1:                                                                                                              # Adding content to the first column
    st.subheader("Hi :wave:")                                                                                           # Adding a subheader
    st.title("The Professional     Portfolio")                                                                          # Adding a title

with col2:                                                                                                              # Adding content to the second column
    st.image("assets/moi-7.png")                                                                                        # Adding an image

st.title(" ")


col1, col2 = st.columns(2)                                                                                              # Creating 2 columns in the layout
with col1:                                                                                                              # Adding content to the first column
    st.subheader("My professional web site")                                                                            # Adding a subheader
    st.write("- Made with Adobe Illustrator")                                                                           # Adding a text
    st.write("- And a wonderfully app name Svija")                                                                      # Adding a text
    st.write("- Come see it")                                                                                           # Adding a text
    st.write("- Know me better")                                                                                        # Adding a text
    st.write("- I'm am a programmer, but also a artist")                                                                # Adding a text

with col2:                                                                                                              # Adding content to the second column
    st.write("https://melissa.christiaenssens.svija.site/")                                                             # Adding a web link
    st.image("images/pro.jpg")                                                                                          # Adding an image

st.title(" ")                                                                                                           # Adding a blank space

st.title("My Professional Setup")                                                                                       # Adding a title
st.image("images/setup4.jpg")                                                                                           # Adding an image

st.write(" ")

st.title("My Skills")                                                                                                   # Adding a title


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
<head>
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
      {"category": "Python", "value": 90, "order": 3},
      {"category": "Html", "value": 50, "order": 4},
      {"category": "Css", "value": 50, "order": 5},
      {"category": "JavaScript", "value": 30, "order": 1},
      {"category": "Illustrator and Svija", "value": 25, "order": 2}
    ]
  },
  "mark": {"type": "arc", "outerRadius": 120},
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
          "Python",
          "Html",
          "Css",
          "JavaScript",
          "Illustrator and Svija"
        ],
        "range": ["#7f25E8", "#25C5EB", "#E825AE", "#21F71E", "#0055FA"]
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
st.title("Professional's Gallery")                                                                                      # Adding a title

col1, col2, col3 = st.columns(3)                                                                                        # Creating 3 columns in the layout

with col1:                                                                                                              # Adding content to the first column
    st.image("images/p1.png")                                                                                           # Adding an image
    st.image("images/p2.3.png")
    st.image("images/p4.png")

with col2:                                                                                                              # Adding content to the second column
    st.image("images/p5.1.png")                                                                                         # Adding an image
    st.image("images/p5.2.png")

with col3:                                                                                                              # Adding content to the third column
    st.image("images/p6.png")                                                                                           # Adding an image
    st.image("images/p3.png")


st.subheader(" ")                                                                                                       # Adding a subheader
st.write("CONTACT")                                                                                                     # Adding a text
st.title("For any inquiries, email at:")
st.subheader("Professional: metalomax@gmail.com")                                                                       # Adding a subheader
