import React from 'react';
import { Card, Match } from '../types';
import MatchCard from './MatchCard';

interface FightCardProps {
  card: Card;
}

const FightCard: React.FC<FightCardProps> = ({ card }) => {
  return (
    <div className="fight-card">
      <h3 className="card-header">
        {card.hdr} <span className="card-status">({card.status})</span>
      </h3>
      {card.mtchs.map((match: Match, index: number) => (
        <MatchCard key={index} match={match} />
      ))}
    </div>
  );
};

export default FightCard;
