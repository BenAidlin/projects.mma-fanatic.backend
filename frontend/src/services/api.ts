import axios from 'axios';
import { Fight, Prediction } from '../types';

const API_BASE_URL = 'https://api.example.com'; // Replace with actual API URL

export const fetchFights = async (): Promise<Fight[]> => {
  const response = await axios.get(`${API_BASE_URL}/fights`);
  return response.data;
};

export const submitPrediction = async (prediction: Prediction): Promise<void> => {
  await axios.post(`${API_BASE_URL}/predictions`, prediction);
};
