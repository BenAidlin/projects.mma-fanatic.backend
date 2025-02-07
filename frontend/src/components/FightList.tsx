import React, { useState } from 'react';
import { Fight } from '../types';
import FightCard from './FightCard';

interface FightListProps {
  fights: Fight[];
}

const FightList: React.FC<FightListProps> = ({ fights }) => {
  const [expandedFight, setExpandedFight] = useState<string | null>(null);

  const toggleFight = (fightId: string) => {
    setExpandedFight(expandedFight === fightId ? null : fightId);
  };

  return (
    <div className="fight-list">
      {fights.map((fight) => (
        <div key={fight.id} className="fight-event">
          <h2 className="fight-event-header" onClick={() => toggleFight(fight.id)}>
            {fight.name}
            <span className="expand-icon">{expandedFight === fight.id ? '▼' : '▶'}</span>
          </h2>
          {expandedFight === fight.id && (
            <div className="fight-event-details">
              <p className="event-date">Date: {new Date(fight.event_date).toLocaleString()}</p>
              {fight.cards.map((card, index) => (
                <FightCard key={index} card={card} />
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default FightList;
