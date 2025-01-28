import React, {useState} from 'react';
// import { useDispatch } from 'react-redux';
// import { AppDispatch } from '../store';
// import { addPredictionAsync } from '../store/userSlice';
import { Match } from '../types';
import Modal from './Modal';

interface PredictionButtonProps {
  fightId: string;
  match: Match;
}

const PredictionButton: React.FC<PredictionButtonProps> = ({fightId, match}) => {
  // const dispatch = useDispatch<AppDispatch>();
  const [isModalOpen, setIsModalOpen] = useState(false);


  const handlePredict = () => {
    setIsModalOpen(true);
  };
  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div>
      <button className='predict-button'  onClick={handlePredict}>
        Predict Fight!
      </button>
      <Modal fightId={fightId} match={match} isOpen={isModalOpen} onClose={closeModal}>
      </Modal>
    </div>
  );
};

export default PredictionButton;
