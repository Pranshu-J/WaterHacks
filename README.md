# 🌻 FlowerAlts - Water-Efficient Alternatives for Arizona's Flowers

**FlowerAlts** is a web application created as a solution for the *WaterHacks* hackathon, focusing on sustainability and water conservation. This project suggests alternative, water-efficient flowers for Arizona that look similar to common water-thirsty flowers. By making sustainable landscaping choices, users can reduce water usage without sacrificing beauty.

## 💡 Hackathon Prompt

**Prompt:**  
*Create an idea or solution for a problem relating to sustainability in your community. Be creative when coming up with a solution. You can present a hardware/software solution or an idea!*

### Solution:  
We present an application that suggests alternatives to the 100 most common flowers in Arizona. These alternatives are similar in appearance but require significantly less water, helping communities conserve water while maintaining the aesthetics of their environment.

## 🚀 How It Works

**FlowerAlts** allows users to:
1. **Select a flower** from a list of 100 common Arizona flowers.
2. **View water requirements** for the selected flower.
3. **Explore alternative flowers** that are more water-efficient or have the same water efficiency.

### Key Features
- **Select a Flower**: Users can choose a flower from a list of 100 common flowers in Arizona.
- **View Water Requirements**: The app displays how much water the selected flower requires.
- **Explore Alternatives**: The app provides alternatives that are more water-efficient, including the percentage difference in water consumption.

### How the Code Works
1. **Data Loading**: The app loads a CSV file (`flowers.csv`) containing the flower names, their water requirements, and alternatives.
2. **User Interaction**: Users select a flower using a `Streamlit` select box.
3. **Data Processing**: The app retrieves the flower's water needs and compares them with alternatives using simple division and percentage change calculations.
4. **Efficiency Display**: It displays alternatives that are more water-efficient or equally efficient.
5. **Custom Styling**: Custom HTML/CSS is used for the header and bottom message.

### Technologies Used
- **Streamlit**: For building the web interface and handling user interaction.
- **Pandas**: For reading and manipulating CSV data.
- **HTML/CSS**: For basic custom styling of the interface.

### Example Workflow
1. The user selects "Sunflower".
2. The app displays "Sunflower requires 2 inches of water per 7 days."
3. The app lists alternative flowers like "Daisy" that are 15% more water-efficient.


## 🌱 Future Improvements
- Add more flowers to the dataset.
- Expand to other regions and climates.
- Add an interactive map for visualizing water-efficient zones.

## 🎯 Purpose and Impact
This project aims to encourage water conservation by helping Arizona communities choose aesthetically similar, water-efficient flowers. **FlowerAlts** empowers users to make informed, sustainable landscaping decisions, contributing to overall water conservation efforts.

---

By using **FlowerAlts**, you can make sustainable choices in your landscaping while preserving the beauty of your environment. Happy Planting! 🪴
