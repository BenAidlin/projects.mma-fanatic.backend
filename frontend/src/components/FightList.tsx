import React from 'react';
import { Fight } from '../types';
import FightCard from './FightCard';

interface FightListProps {
  fights: Fight[];
  onPredict: (fightId: string, winner: string) => void;
}

const FightList: React.FC<FightListProps> = ({ fights, onPredict }) => {
  return (
    <div className="fight-list">
      {fights.map((fight) => (
        <FightCard key={fight.id} fight={fight} onPredict={onPredict} />
      ))}
    </div>
  );
};

export default FightList;
