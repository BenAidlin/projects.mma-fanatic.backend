import React from 'react';
import { Match } from '../types';
import MatchCard from './MatchCard';

interface FightCardProps {
  card: Card;
}

const FightCard: React.FC<FightCardProps> = ({ card }) => {
  return (
    <div className="fight-card">
      <h3>{card.hdr}</h3>
      {card.mtchs.map((match, index) => (
        <MatchCard key={index} match={match} />
      ))}
    </div>
  );
};

export default FightCard;
