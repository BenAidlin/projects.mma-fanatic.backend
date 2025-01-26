import React from 'react';
import { useDispatch } from 'react-redux';
import { AppDispatch } from '../store';
import { addPredictionAsync } from '../store/userSlice';
import { Match } from '../types';

interface PredictionButtonProps {
  fightId: string;
  match: Match;
  fighter: 'awy' | 'hme';
}

const PredictionButton: React.FC<PredictionButtonProps> = ({ fightId, match, fighter }) => {
  const dispatch = useDispatch<AppDispatch>();

  const handlePredict = () => {
    dispatch(addPredictionAsync({
      fightId,
      matchId: match[fighter].original_id,
      predictedWinner: match[fighter].display_name,
    }));
  };

  return (
    <button onClick={handlePredict}>
      Predict {match[fighter].display_name}
    </button>
  );
};

export default PredictionButton;
