import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './pages/Home';
import Schedule from './pages/Schedule';
import Predictions from './pages/Predictions';
import UserScore from './components/UserScore';
import './App.css';

const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <header>
          <div className='header-content'>
            <h1>UFC Fight Predictor</h1>
            <nav>
              <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/schedule">Schedule</Link></li>
                <li><Link to="/predictions">Predictions</Link></li>
              </ul>
            </nav>
            <div className='user-info'>
              <UserScore />
            </div>
          </div>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/schedule" element={<Schedule />} />
            <Route path="/predictions" element={<Predictions />} />
          </Routes>
        </main>
        <footer>
          <p>&copy; 2025 UFC Fight Predictor. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
