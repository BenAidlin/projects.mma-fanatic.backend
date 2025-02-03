import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Schedule from './pages/Schedule';
import Predictions from './pages/Predictions';
import UserScore from './components/UserScore';
import Login from './components/Login';
import { getCurrentUser, handleAuthCallback, logout } from './services/auth';
import './App.css';

const App: React.FC = () => {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    const fetchUser = async () => {
      const userData = await getCurrentUser();
      setUser(userData);
    };
    fetchUser();
  }, []);

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
                {user ? (
                  <li><button onClick={logout}>Logout</button></li>
                ) : (
                  <li><Link to="/login">Login</Link></li>
                )}
              </ul>
            </nav>
            <div className='user-info'>
              {user ? (
                <>
                  <span>Welcome, {user.email}</span>
                  <UserScore />
                </>
              ) : (
                <span>Please log in</span>
              )}
            </div>
          </div>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/schedule" element={<Schedule />} />
            <Route path="/predictions" element={user ? <Predictions /> : <Navigate to="/login" />} />
            <Route path="/login" element={<Login />} />
            <Route 
              path="/auth-callback" 
              element={
                <AuthCallback 
                  onSuccess={(token) => {
                    handleAuthCallback(token);
                    return <Navigate to="/" />;
                  }}
                />
              } 
            />
          </Routes>
        </main>
        <footer>
          <p>&copy; 2025 UFC Fight Predictor. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
};

// AuthCallback component to handle the authentication callback
const AuthCallback: React.FC<{ onSuccess: (token: string) => React.ReactElement }> = ({ onSuccess }) => {
  useEffect(() => {
    const searchParams = new URLSearchParams(window.location.search);
    const token = searchParams.get('token');
    if (token) {
      onSuccess(token);
    }
  }, [onSuccess]);

  return <div>Processing authentication...</div>;
};

export default App;
