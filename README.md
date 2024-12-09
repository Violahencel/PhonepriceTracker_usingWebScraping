

### Python Dependencies (`requirements.txt`)
```
Flask
beautifulsoup4
requests
plotly
pandas
react-typed
framer-motion
```

### Project Documentation (`README.md`)
```markdown
# Phone Price Tracker

## Project Overview
Phone Price Tracker is a web application that allows users to track and compare prices for popular smartphone models from Amazon. The project includes web scraping, data visualization, and a responsive frontend.

### Features
- **Web Scraping:** Scrapes data from Amazon for different smartphone models (e.g., iPhone, OnePlus, Samsung).
- **REST API:** Serves phone price data using a Flask API.
- **Frontend:** A responsive React-based frontend that displays phone details and provides a search feature.
- **Data Visualization:** Uses Plotly to create visualizations of phone price trends.
- **Interactive UI:** Includes animations and modals for a modern user experience.

## Project Structure
```
phone-price-tracker/
├── backend/
│   ├── app.py              # Flask backend API
│   ├── scrape_amazon.py    # Web scraping script
│   ├── phone_prices.csv    # CSV file to store phone data
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   ├── public/
│   │   ├── index.html      # HTML template
│   │   └── ...
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Styles for React components
│   │   ├── index.js
    |   └── index.css (optional)
│   ├── package.json        # React project dependencies
│   └── ...
│
├── data-visualization/
│   └── visualize.py        # Script for visualizing phone data
│
└── README.md               # Project documentation
```

## Installation and Setup

### Prerequisites
- Python 3.x
- Node.js and npm

###  Create a Virtual Environment
  python -m venv venv
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  venv\Scripts\activate
  (venv) PS D:\Phone Price Tracker\frontend> 


### First always run the backend and then Frontend both in different terminal and both under virtual terminal
### Backend Setup
1. Navigate to the `backend/` directory:
   ```sh
   cd backend
   ```
2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```sh
   python app.py
   ```

### Frontend Setup
1. Navigate to the `frontend/` directory:
   ```sh
   cd frontend
   ```
2. Install the React dependencies:
   ```sh
   npm install or  npm install --legacy-peer-deps
   ```
3. Start the React development server:
   ```sh
   npm start
   ```


   ```

## Usage
- Access the application at `http://localhost:3000` after starting both the backend and frontend servers.
- Use the search bar to filter phone models.
- Click on a phone card to see more details and visit the link to purchase.

## Technologies Used
- **Backend:** Flask, BeautifulSoup, Requests
- **Frontend:** React, Bootstrap, Framer Motion, Typed.js
- **Data Visualization:** Plotly, Pandas

## License
This project is licensed under the MIT License.
```
