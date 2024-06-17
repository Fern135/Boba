import { 
  BrowserRouter as Router, 
  Route, 
  Routes 
} from 'react-router-dom';
import React from 'react';

import './Global.scss';

import Home from "./pages/Home";

// import Login from "./components/Auth/Login";
// import SignUp from './components/Auth/SignUp';
// runs on port 3000

function App() {
  return (
    <Router>
      <Routes>
          <Route exact path="/" element={<Home />} /> 
          {/* <Route path="/signup" element={<SignUp />} />  */}
      </Routes>
    </Router>
  );
}

export default App;