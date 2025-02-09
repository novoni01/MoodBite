import React, { useState } from "react";
import "../pages/Home.css";

const MoodSelector = ({ onMoodSelect }) => {
  const [showMoodOptions, setShowMoodOptions] = useState(false);

  // Function to show mood options when the user agrees
  const handleMoodRequest = () => {
    setShowMoodOptions(true);
  };

  // Function to call onMoodSelect when a mood is selected
  const handleMoodSelection = (selectedMood) => {
    onMoodSelect(selectedMood); // This will pass the selected mood to the parent
  };

  return (
    <div>
      <p>Would you like to share your mood?</p>
      <button onClick={handleMoodRequest}>Yes, tell me my mood options</button>

      {showMoodOptions && (
        <div>
          <h2>What's your current mood?</h2>
          <div className="mood-buttons">
            <button onClick={() => handleMoodSelection("Happy")}>Happy</button>
            <button onClick={() => handleMoodSelection("Neutral")}>Neutral</button>
            <button onClick={() => handleMoodSelection("Sad")}>Sad</button>
            <button onClick={() => handleMoodSelection("Stressed")}>Stressed</button>
            <button onClick={() => handleMoodSelection("Bored")}>Bored</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default MoodSelector;
