import React, {useState} from 'react';
import { Match } from '../types';
import Modal from './Modal';
import { useSelector } from 'react-redux';
import { RootState } from '../store';

interface PredictionButtonProps {
  fightId: string;
  match: Match;
}

const PredictionButton: React.FC<PredictionButtonProps> = ({fightId, match}) => {
  // const dispatch = useDispatch<AppDispatch>();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const user = useSelector((state: RootState) => state.user.data);

  const handlePredict = () => {
    setIsModalOpen(true);
  };
  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div>
      {
        user ? 
        <button className='predict-button'  onClick={handlePredict}>
          Predict Fight!
        </button>
        :
        <button onMouseEnter={()=>{}} disabled={true} className='predict-button-disabled'>Can't make predictions</button>
      }
      <Modal match={match} isOpen={isModalOpen} onClose={closeModal} userId={user?.id || ''}>
      </Modal>
    </div>
  );
};

export default PredictionButton;
