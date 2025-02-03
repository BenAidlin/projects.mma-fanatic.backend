import React from 'react';
import { initiateGoogleLogin } from '../services/auth';

const Login: React.FC = () => {
  return (
    <div>
      <h1>Login</h1>
      <button onClick={initiateGoogleLogin}>Login with Google</button>
    </div>
  );
};

export default Login;
