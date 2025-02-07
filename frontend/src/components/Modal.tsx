import React, { useState, useEffect } from 'react';
import { Match, Prediction, Method } from '../types';
import { getPredictions, createPrediction, updatePrediction, deletePredictions } from '../services/api';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  fightId: string;
  match: Match;
  userId: string;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, fightId, match, userId }) => {
  const [prediction, setPrediction] = useState<Prediction | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (isOpen) {
      fetchExistingPrediction();
    }
  }, [isOpen]);

  const fetchExistingPrediction = async () => {
    setIsLoading(true);
    try {
      const predictions = await getPredictions(userId);
      const existingPrediction = predictions.find(
        (p) => p.hme_id === match.hme.original_id && p.awy_id === match.awy.original_id
      );
      if (existingPrediction) {
        setPrediction(existingPrediction);
      } else {
        setPrediction({
          prediction_id: null,
          user_id: userId,
          winner: null,
          method: Method.NOT_PICKED,
          round: null,
          potential_gain: null,
          card_id: fightId,
          hme_id: match.hme.original_id,
          awy_id: match.awy.original_id,
        });
      }
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
    setIsLoading(false);
  };

  const handleSubmit = async () => {
    if (!prediction) return;

    try {
      if (prediction.prediction_id) {
        await updatePrediction(prediction);
      } else {
        await createPrediction(prediction);
      }
      onClose();
    } catch (error) {
      console.error('Error submitting prediction:', error);
    }
  };

  const handleDelete = async () => {
    if (!prediction || !prediction.prediction_id) return;

    try {
      await deletePredictions([prediction]);
      onClose();
    } catch (error) {
      console.error('Error deleting prediction:', error);
    }
  };

  if (!isOpen || isLoading) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>{prediction?.prediction_id ? 'Update Your Prediction' : 'Make Your Prediction'}</h2>
        <div className="winner-selection">
          <h3>Select Winner</h3>
          <div>
            <input
              type="radio"
              id="home"
              name="winner"
              value={match.hme.display_name}
              checked={prediction?.winner === match.hme.display_name}
              onChange={(e) => setPrediction(prev => prev ? {...prev, winner: e.target.value} : null)}
            />
            <label htmlFor="home">{match.hme.display_name}</label>
          </div>
          <div>
            <input
              type="radio"
              id="away"
              name="winner"
              value={match.awy.display_name}
              checked={prediction?.winner === match.awy.display_name}
              onChange={(e) => setPrediction(prev => prev ? {...prev, winner: e.target.value} : null)}
            />
            <label htmlFor="away">{match.awy.display_name}</label>
          </div>
        </div>
        <div className="method-selection">
          <h3>Method of Victory (Optional)</h3>
          <select 
            value={prediction?.method} 
            onChange={(e) => setPrediction(prev => prev ? {...prev, method: e.target.value as Method, round: null} : null)}
          >
            <option value={Method.NOT_PICKED}>Not Picked</option>
            <option value={Method.KO}>KO/TKO</option>
            <option value={Method.SUB}>Submission</option>
            <option value={Method.DEC}>Decision</option>
          </select>
        </div>
        <div className="round-selection">
          <h3>Round (Optional)</h3>
          <select 
            disabled={prediction?.method == Method.DEC}
            value={prediction?.round || ''} 
            onChange={(e) => setPrediction(prev => prev ? {...prev, round: e.target.value ? parseInt(e.target.value) : null} : null)}
          >
            <option value="">Not Picked</option>
            <option value="1">Round 1</option>
            <option value="2">Round 2</option>
            <option value="3">Round 3</option>
            <option value="4">Round 4</option>
            <option value="5">Round 5</option>
          </select>
        </div>
        <div className="modal-actions">
          <button onClick={handleSubmit} disabled={!prediction?.winner}>
            {prediction?.prediction_id ? 'Update Prediction' : 'Submit Prediction'}
          </button>
          {prediction?.prediction_id && (
            <button onClick={handleDelete}>Delete Prediction</button>
          )}
          <button onClick={onClose}>Cancel</button>
        </div>
      </div>
    </div>
  );
};

export default Modal;
