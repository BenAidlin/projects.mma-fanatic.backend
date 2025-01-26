import React from 'react';
import { Match } from '../types';
import PredictionButton from './PredictionButton';

interface MatchCardProps {
  fightId: string;
  match: Match;
}

const MatchCard: React.FC<MatchCardProps> = ({ fightId, match }) => {
  return (
    <div className="match-card">
      <h4>{match.nte}</h4>
      <div className="fighters">
        <div className="fighter">
          <h5>{match.awy.display_name}</h5>
          <p>Record: {match.awy.rec}</p>
          <p>From: {match.awy.country}</p>
          <PredictionButton fightId={fightId} match={match} fighter="awy" />
        </div>
        <div className="vs">VS</div>
        <div className="fighter">
          <h5>{match.hme.display_name}</h5>
          <p>Record: {match.hme.rec}</p>
          <p>From: {match.hme.country}</p>
          <PredictionButton fightId={fightId} match={match} fighter="hme" />
        </div>
      </div>
      <p>Date: {new Date(match.dt).toLocaleString()}</p>
    </div>
  );
};

export default MatchCard;
