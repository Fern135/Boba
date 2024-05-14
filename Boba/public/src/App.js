import { 
  BrowserRouter as Router, 
  Route, 
  Routes 
} from 'react-router-dom';
import React from 'react';

import './Global.scss';

// import Login from "./components/Auth/Login";
// import SignUp from './components/Auth/SignUp';
// runs on port 3000

function App() {
  return (
    <Router>
      <Routes>
          {/* <Route exact path="/" element={<Login />} />  */}
          {/* <Route path="/signup" element={<SignUp />} />  */}
      </Routes>
    </Router>
  );
}

export default App;