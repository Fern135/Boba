import React, { useState, useEffect } from "react";

import "../../Global.scss";

function Spinner({ color }) {
  return (
    <div className={`spinner-border text-${color}`} role="status">
      <span className="visually-hidden">Loading...</span>
    </div>
  );
}

function Loader({ seconds }){
    const [currentColor, setCurrentColor] = useState("primary");

    useEffect(() => {
      const timer = setTimeout(() => {
        setCurrentColor((prevColor) => {
          switch (prevColor) {
            case "primary":
              return "success";
            case "success":
              return "info";
            case "info":
              return "primary";
            default:
              return "primary";
          }
        });
      }, seconds);
  
      return () => clearTimeout(timer);
    }, [currentColor, seconds]);
  
    return (
      <>
        <div className="container">
          <Spinner color={currentColor} />
        </div>
      </>
    );
}

export default Loader;