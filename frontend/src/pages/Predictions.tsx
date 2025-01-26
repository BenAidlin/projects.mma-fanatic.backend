import React from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store';
import { Fight, Prediction } from '../types';

const Predictions: React.FC = () => {
  const fights = useSelector((state: RootState) => state.fights);
  const userPredictions = useSelector((state: RootState) => state.user.predictions);

  const findFightAndMatch = (prediction: Prediction): { fight: Fight | undefined, matchup: string } => {
    const fight = fights.find(f => f.id === prediction.fightId);
    if (fight) {
      const match = fight.cards.flatMap(card => card.mtchs).find(m => 
        m.awy.original_id === prediction.matchId || m.hme.original_id === prediction.matchId
      );
      if (match) {
        return { 
          fight, 
          matchup: `${match.awy.display_name} vs ${match.hme.display_name}`
        };
      }
    }
    return { fight: undefined, matchup: 'Unknown matchup' };
  };

  return (
    <div className="predictions">
      <h2>My Predictions</h2>
      <ul>
        {userPredictions.map((prediction: Prediction) => {
          const { fight, matchup } = findFightAndMatch(prediction);
          return (
            <li key={`${prediction.fightId}-${prediction.matchId}`}>
              {fight ? (
                <>
                  {fight.name}: {matchup} - Predicted {prediction.predictedWinner}
                </>
              ) : (
                <span>Prediction for unknown fight</span>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default Predictions;
