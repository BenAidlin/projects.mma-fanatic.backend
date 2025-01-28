import React from 'react';
import { Link } from 'react-router-dom';

const Home: React.FC = () => {
  return (
    <div className="home">
      <h1>Welcome to UFC Fight Predictor</h1>
      <p className="intro-text">
        Ready to test your UFC knowledge? Browse upcoming fights, make your predictions, and see how you stack up against other fans!
      </p>
      <nav>
        <ul>
          <li><Link to="/schedule">View Fight Schedule</Link></li>
          <li><Link to="/predictions">My Predictions</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;
