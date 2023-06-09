# markov_simulation
Simulation of customers behavior in a supermarket.

---

This project aims to model how customers move through different locations within the supermarket and analyze their behavior patterns.

### Project Overview

The project consists of several components:

1. **Data Loading and Preprocessing**: The project starts with loading and combining customer data from CSV files. It preprocesses the data, assigns unique customer IDs, handles missing values, and performs time resampling.

2. **EDA and Transition Matrix**: Exploratory Data Analysis (EDA) is conducted to gain insights into the customer data. A transition matrix is computed to determine the probability of customers transitioning from one location to another.

3. **Customer Class**: The `Customer` class represents an individual customer in the supermarket. Each customer has a name, current location, budget, and transition history. Customers can move to the next location based on the transition probability.

4. **Supermarket Simulation**: The `Supermarket` class simulates multiple customer instances in the supermarket. It generates new customers at random intervals and allows them to move through different locations every minute. The simulation runs for a specified duration, and the resulting data is stored in a CSV file.

5. **Visualization**: The simulation data is visualized using bar plots to show the number of customers in each location at different time intervals. These plots are saved as PNG files, and a GIF animation is created by concatenating the PNG files.

### Technologies Used

- Python
- Pandas: Data manipulation and analysis
- Faker: Generation of fake customer names
- NumPy: Random number generation
- Matplotlib: Plotting and visualization
- Seaborn: Enhanced data visualization
- ImageIO: Creation of GIF animation

### Usage

To run the simulation and visualize the results:

1. Ensure that the required dependencies are installed (Pandas, Faker, NumPy, Matplotlib, Seaborn, ImageIO).
2. Run the provided scripts in the specified order.
3. The simulation data will be saved in the `supermarket_data` folder as a CSV file.
4. The visualization plots will be saved in the `simulation_data` folder as PNG files.
5. A GIF animation combining all the PNG files will be saved in the `output` folder.

Feel free to explore the code and modify it to suit your specific requirements.

### Future Enhancements

- Adding more sophisticated customer behavior models, such as decision-making based on budget and product preferences.
- Incorporating real-time data streaming for dynamic customer movement.
- Implementing interactive visualizations and user interfaces for better exploration and analysis.

---
