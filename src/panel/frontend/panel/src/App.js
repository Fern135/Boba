// import logo from './logo.svg';

// import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';


/********** used components **********/
import Home from './components/home/component/home';
/********** used components **********/

/********** styling **********/
import './Global.scss';
/********** styling **********/

function App() {
  return (
    <Router>
      <div className="App-header">
        <Routes>
          <Route path="/" element={<Home />} />

        </Routes>
      </div>
    </Router>
  );
}

export default App;
