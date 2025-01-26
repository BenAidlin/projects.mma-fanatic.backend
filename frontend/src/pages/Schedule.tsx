import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '../store';
import { getFights } from '../store/fightSlice';
import FightList from '../components/FightList';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorMessage from '../components/ErrorMessage';

const Schedule: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { fights, status, error } = useSelector((state: RootState) => state.fights);

  useEffect(() => {
    if (status === 'idle') {
      dispatch(getFights());
    }
  }, [status, dispatch]);

  if (status === 'loading') {
    return <LoadingSpinner />;
  }

  if (status === 'failed') {
    return <ErrorMessage message={error || 'An unknown error occurred'} />;
  }

  return (
    <div className="schedule">
      <h2>Fight Schedule</h2>
      {fights.length > 0 ? (
        <FightList fights={fights} />
      ) : (
        <p>No upcoming fights scheduled.</p>
      )}
    </div>
  );
};

export default Schedule;
