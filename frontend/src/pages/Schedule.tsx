import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, RootState } from '../store';
import { getFights } from '../store/fightSlice';
import FightList from '../components/FightList';

const Schedule: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const fights = useSelector((state: RootState) => state.fights);

  useEffect(() => {
    dispatch(getFights());
  }, [dispatch]);

  return (
    <div className="schedule">
      <h2>Fight Schedule</h2>
      <FightList fights={fights} />
    </div>
  );
};

export default Schedule;
