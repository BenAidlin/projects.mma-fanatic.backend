import React from 'react';
import { Fight } from '../types';
import FightCard from './FightCard';

interface FightListProps {
  fights: Fight[];
}

const FightList: React.FC<FightListProps> = ({ fights }) => {
  return (
    <div className="fight-list">
      {fights.map((fight) => (
        <div key={fight.id} className="fight-event">
          <h2>{fight.name}</h2>
          <p>Date: {new Date(fight.event_date).toLocaleString()}</p>
          {fight.cards.map((card, index) => (
            <FightCard key={index} fightId={fight.id} card={card} />
          ))}
        </div>
      ))}
    </div>
  );
};

export default FightList;
