import React from 'react';
import { Match } from '../types';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  fightId: string;
  match: Match;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, fightId, match }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        {fightId} <br></br>
        {match.hme.display_name} <br></br>
        {match.awy.display_name} <br></br>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default Modal;
