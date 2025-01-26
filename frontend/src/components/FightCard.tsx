import React from 'react';
import { Fight } from '../types';

interface FightCardProps {
  fight: Fight;
  onPredict: (fightId: string, winner: string) => void;
}

const FightCard: React.FC<FightCardProps> = ({ fight, onPredict }) => {
  return (
    <div className="fight-card">
      <h3>{fight.weight_class}</h3>
      <p>{fight.fighter1} vs {fight.fighter2}</p>
      <p>Date: {fight.date}</p>
      <button onClick={() => onPredict(fight.id, fight.fighter1)}>
        Predict {fight.fighter1}
      </button>
      <button onClick={() => onPredict(fight.id, fight.fighter2)}>
        Predict {fight.fighter2}
      </button>
    </div>
  );
};

export default FightCard;
