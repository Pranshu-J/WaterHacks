import streamlit as st
import pandas as pd

# Title for the app as a big heading at the top left
st.markdown("<h1 style='text-align: left;'>FlowerAlts🌻</h1>", unsafe_allow_html=True)

# Load CSV file with a specified encoding
df = pd.read_csv('flowers.csv', encoding='ISO-8859-1')

# Extract options from the first column
options = df.iloc[:, 0].tolist()

# Streamlit selectbox
selected_flower = st.selectbox('Select a flower:', options)

# Find the row where the selected flower is located and get the values from the 2nd to 6th columns
selected_row = df[df.iloc[:, 0] == selected_flower].iloc[0]

selected_flower_info_2 = selected_row[1]  # 2nd column (water inches)
selected_flower_info_3 = selected_row[2]  # 3rd column (days per inch of water)
selected_flower_info_4 = selected_row[3]  # 4th column (flower alternatives)
selected_flower_info_5 = selected_row[4]  # 5th column (water inches for alternatives)
selected_flower_info_6 = selected_row[5]  # 6th column (days per inch for alternatives)

# Function to safely split and return a list
def safe_split(value):
    if pd.notna(value) and isinstance(value, str):
        return [item.strip() for item in value.split(',')]
    else:
        return []

# Function to safely divide two numbers and return the rounded quotient
def safe_divide(val1, val2):
    try:
        return round(float(val1) / float(val2), 2)  # Convert to float and divide, round to 2 decimal places
    except (ValueError, ZeroDivisionError):  # Handle non-numeric values or division by zero
        return 'N/A'

# Function to calculate percent change
def percent_change(new_value, base_value):
    try:
        return round(((float(new_value) - float(base_value)) / float(base_value)) * 100, 2)
    except (ValueError, ZeroDivisionError):  # Handle non-numeric values or division by zero
        return 'N/A'

# Calculate the quotient for the 2nd and 3rd columns for the selected flower
selected_flower_quotient = safe_divide(selected_flower_info_2, selected_flower_info_3)

# Split the values from the 4th, 5th, and 6th columns
flower_list_4 = safe_split(selected_flower_info_4)
flower_list_5 = safe_split(selected_flower_info_5)
flower_list_6 = safe_split(selected_flower_info_6)

# Display the selected flower's water needs
st.write(f'You selected: **{selected_flower}**')
st.markdown(f'Your selected flower requires **{selected_flower_info_2}** inches of water per **{selected_flower_info_3}** days')

# Track whether we display any water-efficient alternatives or similar efficiency flowers
has_water_efficient_alternatives = False
has_similar_efficiency = False

# Check if there are any related flowers with a negative or zero percentage change
efficient_flowers = []
similar_flowers = []

for f4, f5, f6 in zip(flower_list_4, flower_list_5, flower_list_6):
    related_flower_quotient = safe_divide(f5, f6)
    percent_diff = percent_change(related_flower_quotient, selected_flower_quotient)
    
    # Only include flowers with a negative percentage change
    if isinstance(percent_diff, float) and percent_diff < 0:
        absolute_percent_diff = abs(percent_diff)  # Convert to absolute value
        efficient_flowers.append(f'**{f4}**: **{absolute_percent_diff}%** more water efficient')
    elif isinstance(percent_diff, float) and percent_diff == 0:
        similar_flowers.append(f'**{f4}** (same water efficiency)')

# Display water-efficient alternatives if any
if efficient_flowers:
    has_water_efficient_alternatives = True
    st.write("Here are some water-efficient alternatives for the flower you chose:")
    for flower in efficient_flowers:
        st.markdown(flower)

# Display similar flowers with 0% efficiency change
if similar_flowers:
    has_similar_efficiency = True
    st.write("Here is a similar flower with the same water efficiency:")
    for flower in similar_flowers:
        st.markdown(flower)

# If no water-efficient alternatives and no similar efficiency flowers were found, display a congratulatory message
if not has_water_efficient_alternatives and not has_similar_efficiency:
    st.write("You've selected the most water efficient flower! Good Job!")

# Add custom CSS for anchoring the "Happy Planting" text to the bottom and centering it
st.markdown("""
    <style>
        .happy-planting {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            text-align: center;
            font-size: 20px;
            margin-bottom: 20px;  /* Adds space between the element above and the text */
        }
    </style>
""", unsafe_allow_html=True)

# Add the "Happy Planting" statement at the bottom of the page
st.markdown("<h3 class='happy-planting'>Happy Planting 🪴</h3>", unsafe_allow_html=True)