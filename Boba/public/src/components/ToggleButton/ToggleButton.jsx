import React, { useState } from 'react';

import "../../Global.scss";

function ToggleButton({ title }){
  const [isOn, setIsOn] = useState(false);

  const getUrl = () => {
    switch (title) {
      case 'php server':
        return isOn ? 'http://example.com/php/off' : 'http://example.com/php/on';
      case 'dns server':
        return isOn ? 'http://example.com/dns/off' : 'http://example.com/dns/on';
      case 'db server':
        return isOn ? 'http://example.com/db/off' : 'http://example.com/db/on';
      case 'config':
        return isOn ? 'http://example.com/config/off' : 'http://example.com/config/on';
      default:
        return '';
    }
  };

  const handleToggle = async () => {
    const url = getUrl();
    if (url) {
      try {
        const response = await fetch(url, { method: 'POST' });
        if (response.ok) {
          setIsOn(!isOn);
        } else {
          console.error('HTTP request failed');
        }
      } catch (error) {
        console.error('Network error:', error);
      }
    } else {
      console.error('Invalid title for URL');
    }
  };

  return (
    <button 
      onClick={handleToggle} 
      className={`btn ${isOn ? 'btn-outline-success' : 'btn-outline-danger'} btn-lg`}
    >
      {isOn ? `${title}` : `${title}`}
    </button>
  );
};

export default ToggleButton;
