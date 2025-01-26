import React from 'react';
import { Link } from 'react-router-dom';
import UserScore from '../components/UserScore';

const Home: React.FC = () => {
  return (
    <div className="home">
      <h1>UFC Fight Predictor</h1>
      <UserScore />
      <nav>
        <ul>
          <li><Link to="/schedule">Fight Schedule</Link></li>
          <li><Link to="/predictions">My Predictions</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;
