import React, { useState, useEffect } from "react";

function Notifications({ title, message, type, position = "tr", autoHideDelay = 3000 }) {
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    let timeoutId;
    if (isVisible) {
      timeoutId = setTimeout(() => {
        setIsVisible(false);
      }, autoHideDelay);
    }

    return () => {
      clearTimeout(timeoutId);
    };
  }, [autoHideDelay, isVisible]);

  const handleClose = () => {
    setIsVisible(false);
  };

  let positionClass = "";
  switch (position) {
    case "tr":
      positionClass = "position-fixed top-0 end-0";
      break;
    case "br":
      positionClass = "position-fixed bottom-0 end-0";
      break;
    case "tl":
      positionClass = "position-fixed top-0 start-0";
      break;
    case "bl":
      positionClass = "position-fixed bottom-0 start-0";
      break;
    default:
      positionClass = "position-fixed top-0 end-0";
  }

  return (
    <div className={`${positionClass} p-3`} style={{ zIndex: 11 }}>
      {isVisible && (
        <div className={`alert alert-${type} alert-dismissible fade show`} role="alert">
          <strong>{title}</strong> {message}
          <button type="button" className="btn-close" aria-label="Close" onClick={handleClose}></button>
        </div>
      )}
    </div>
  );
}

export default Notifications;