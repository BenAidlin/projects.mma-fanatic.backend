import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Schedule from './pages/Schedule';
import Predictions from './pages/Predictions';
import UserScore from './components/UserScore';
import './App.css';

const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <UserScore />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/schedule" element={<Schedule />} />
          <Route path="/predictions" element={<Predictions />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
