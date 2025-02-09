import './App.css';
import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar.jsx";
import Home from "./pages/Home";
import Results from "./pages/Results";
import FoodInputs from "./pages/FoodInputs";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      {/* Include Navbar here to be displayed on all pages */}
      <Navbar />

      <div style={{ paddingTop: "60px" }}> {/* Optional padding to account for navbar */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
          <Route path="/foodInputs" element={<FoodInputs />} />

        </Routes>
      </div>
    </>
  );
}

export default App;