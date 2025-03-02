import React from 'react';
import { Match } from '../types';
import PredictionButton from './PredictionButton';

interface MatchCardProps {
  match: Match;
}

const MatchCard: React.FC<MatchCardProps> = ({ match }) => {
  const renderFighterDetails = (fighter: 'awy' | 'hme') => (
    <div className="fighter-details">
      <h5>{match[fighter].display_name}</h5>
      <p>Record: {match[fighter].rec}</p>
      <p>From: {match[fighter].country}</p>
      <p>Age: {match[fighter].stats.age}</p>
      <p>Height: {match[fighter].stats.ht}</p>
      <p>Weight: {match[fighter].stats.wt}</p>
      
    </div>
  );

  return (
    <div className="match-card">
      <h4 className="match-title">{match.nte}</h4>
      <div className="fighters">
        {renderFighterDetails('awy')}
        <div className="vs">VS</div>
        {renderFighterDetails('hme')}
      </div>
      <p className="match-date">Date: {new Date(match.dt).toLocaleString()}</p>
      <div>
        {match.hme.rec ? <PredictionButton match={match} /> : null}
      </div>
    </div>
  );
};

export default MatchCard;
