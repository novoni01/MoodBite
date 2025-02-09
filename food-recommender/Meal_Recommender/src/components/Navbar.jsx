import React from "react";
import { Link } from "react-router-dom"; // Import Link to add navigation

const Navbar = () => {
  return (
    <nav
      style={{
        padding: "10px 20px",
        background: "#333",
        color: "white",
        display: "flex",
        alignItems: "center",
        boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
        position: "absolute",
        top: 0,
        left: 0,
        width: "100%",
      }}
    >
      {/* Logo / Title */}
      <h2 style={{ margin: 0, fontSize: "1.8em" }}>Meal Recommender</h2>

      {/* Navigation Links */}
      <div style={{ marginLeft: "auto" }}>
        <Link
          to="/"
          style={{
            color: "white",
            textDecoration: "none",
            margin: "0 15px",
            fontSize: "1.1em",
            fontWeight: 500,
            transition: "color 0.3s",
          }}
        >
          Home
        </Link>
        <Link
          to="/results"
          style={{
            color: "white",
            textDecoration: "none",
            margin: "0 15px",
            fontSize: "1.1em",
            fontWeight: 500,
            transition: "color 0.3s",
          }}
        >
          Results
        </Link>

        <Link
          to="/FoodInputs"
          style={{
            color: "white",
            textDecoration: "none",
            margin: "0 15px",
            fontSize: "1.1em",
            fontWeight: 500,
            transition: "color 0.3s",
          }}
        >
          Food Inventory
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
