import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [apiStatus, setApiStatus] = useState("Connecting...");

  useEffect(() => {
    const fetchApiStatus = async () => {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/health`);
        if (response.ok) {
          const data = await response.json();
          console.log(data);
          setApiStatus(data.message || "API is running");
        } else {
          setApiStatus("API is not reachable");
        }
      } catch (error) {
        setApiStatus("Error connecting to API");
      }
    };
    fetchApiStatus();
  }, []);

  return (
    <>
      <div className="container">
        <h1>{apiStatus}</h1>
        <h1>Welcome to the React App</h1>
      </div>
    </>
  );
}

export default App;
