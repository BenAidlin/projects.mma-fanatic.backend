import axios from 'axios';
import { Fight } from '../types';

const API_BASE_URL = 'http://localhost:8001'; // Replace with actual API URL

export const fetchFights = async (): Promise<Fight[]> => {
  const response = await axios.get(`${API_BASE_URL}/schedule`);
  return response.data;
};
