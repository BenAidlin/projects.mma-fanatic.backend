import React from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store';

const UserScore: React.FC = () => {
  const user = useSelector((state: RootState) => state.user);

  return (
    <div className="user-score">
      <h2>Welcome, {user?.data?.given_name}</h2>
      <p>Your score: {user?.data?.score}</p>
    </div>
  );
};

export default UserScore;
