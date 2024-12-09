import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [phones, setPhones] = useState([]);
  
  useEffect(() => {
    async function fetchPhones() {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/phones');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setPhones(data);
      } catch (error) {
        console.error("Error fetching phone data:", error);
      }
    }
    fetchPhones();
  }, []);

  return (
    <div className="container">
      <h1>Welcome to Phone Price Tracker</h1>
      <div className="row">
        <table className="table table-bordered">
          <thead>
            <tr>
              <th>Website</th>
              <th>Phone Name</th>
              <th>Price</th>
              <th>Link</th>
            </tr>
          </thead>
          <tbody>
            {phones.length > 0 ? (
              phones.map((phone, index) => (
                <tr key={index}>
                  <td>{phone['Website']}</td>
                  <td>{phone['Phone Name']}</td>
                  <td>₹{phone['Price']}</td>
                  <td>
                    <a href={phone['Link']} target="_blank" rel="noopener noreferrer">
                      Visit Link
                    </a>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4" className="text-center">No phones found.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
