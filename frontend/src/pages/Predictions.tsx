import React from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store';
import { Fight, Prediction } from '../types';

const Predictions: React.FC = () => {
  const fights = useSelector((state: RootState) => state.fights);
  const userPredictions = useSelector((state: RootState) => state.user.predictions);

  if (!userPredictions) {
    return <div>No predictions available.</div>;
  }

  return (
    <div className="predictions">
      <h2>My Predictions</h2>
      {userPredictions.length === 0 ? (
        <p>You haven't made any predictions yet.</p>
      ) : (
        <ul>
          {userPredictions.map((prediction: Prediction) => {
            const fight = fights.find((f: Fight) => f.id === prediction.fightId);
            return (
              <li key={prediction.fightId}>
                {fight ? (
                  <>
                    {fight.fighter1} vs {fight.fighter2}: Predicted {prediction.predictedWinner}
                  </>
                ) : (
                  <span>Fight not found</span>
                )}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
};

export default Predictions;
