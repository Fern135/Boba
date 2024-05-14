import { useState, useEffect } from "react";
import axios from "axios";

function useFetch(url, options = {}) {
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        let response;
        if (window.fetch) {
          // Use Fetch API if available
          response = await fetch(url, options);

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const responseData = await response.json();
          setData(responseData);

        } else {
          // Fallback to Axios if Fetch API is not available
          response = await axios(url, options);
          setData(response.data);
        }

      } catch (error) {
        setError(error.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [url, options]);

  return { data, isLoading, error };
}

export default useFetch;


// example usage
/*
import React from "react";
import useFetch from "./useFetch"; // Assuming you have the useFetch hook in a separate file

function MyComponent() {
  const url = "https://api.example.com/data";
  const options = {
    method: "GET", // or "POST", "PUT", "DELETE", etc.
    headers: {
      Custom headers if needed
      "Content-Type": "application/json",
      Add any other headers as needed
    },
    Additional options like body, credentials, etc.
  };

  const { data, isLoading, error } = useFetch(url, options);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      { Render your fetched data here }
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default MyComponent;


*/