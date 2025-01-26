import React from 'react';
import { Card, Match } from '../types';
import MatchCard from './MatchCard';

interface FightCardProps {
  fightId: string;
  card: Card;
}

const FightCard: React.FC<FightCardProps> = ({ fightId, card }) => {
  return (
    <div className="fight-card">
      <h3>{card.hdr}</h3>
      {card.mtchs.map((match: Match, index: number) => (
        <MatchCard key={index} fightId={fightId} match={match} />
      ))}
    </div>
  );
};

export default FightCard;
