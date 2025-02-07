import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store';
import { Fight, Prediction, Method, Match } from '../types';
import { getPredictions, fetchFights } from '../services/api';

const Predictions: React.FC = () => {
  const [predictions, setPredictions] = useState<Prediction[]>([]);
  const [fights, setFights] = useState<Fight[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const user = useSelector((state: RootState) => state.user.data);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        if (user?.id) {
          const [userPredictions, allFights] = await Promise.all([
            getPredictions(user.id),
            fetchFights()
          ]);
          setPredictions(userPredictions);
          setFights(allFights);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
      setIsLoading(false);
    };

    fetchData();
  }, [user?.id]);

  const findMatch = (prediction: Prediction): Match | undefined => {
    for (const fight of fights) {
      for (const card of fight.cards) {
        const match = card.mtchs.find(m => 
          prediction.awy_id === m.awy.original_id && prediction.hme_id === m.hme.original_id
        );
        if (match) return match;
      }
    }
    return undefined;
  };

  if (isLoading) {
    return <div>Loading predictions...</div>;
  }

  if (predictions.length === 0) {
    return (
      <div className="predictions">
        <h2>My Predictions</h2>
        <p>You haven't made any predictions yet. Visit the Fight Schedule to make predictions!</p>
      </div>
    );
  }

  return (
    <div className="predictions">
      <h2>My Predictions</h2>
      <ul>
        {predictions.map((prediction) => {
          const match = findMatch(prediction);
          return (
            <li key={prediction.prediction_id}>
              {match ? (
                <>
                  <strong>{match.awy.display_name} vs {match.hme.display_name}</strong><br />
                  Predicted winner: {prediction.winner}<br />
                  Method: {prediction.method !== Method.NOT_PICKED ? prediction.method : 'Not specified'}<br />
                  {prediction.round && `Round: ${prediction.round}`}
                  {prediction.potential_gain && <><br />Potential gain: {prediction.potential_gain}</>}
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
