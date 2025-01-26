import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '../store';
import { getFights } from '../store/fightSlice';
import FightList from '../components/FightList';
import { submitPrediction } from '../services/api';

const Schedule: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const fights = useSelector((state: RootState) => state.fights);

  useEffect(() => {
    dispatch(getFights());
  }, [dispatch]);

  const handlePredict = async (fightId: string, winner: string) => {
    try {
      await submitPrediction({ fightId, predictedWinner: winner });
      // You might want to update the user's predictions in the store here
    } catch (error) {
      console.error('Failed to submit prediction:', error);
    }
  };
  return (
    <div className="schedule">
      <h2>Fight Schedule</h2>
      <FightList fights={fights} onPredict={handlePredict} />
    </div>
  );
};

export default Schedule;