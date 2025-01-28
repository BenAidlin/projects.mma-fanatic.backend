import axios, { AxiosInstance } from 'axios';
import { Fight, Prediction } from '../types';

const API_BASE_URL = 'http://localhost:8004'; // Replace with actual API URL

const axiosInstance: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true, // This is important for handling cookies, including those used for authentication
  maxRedirects: 5, // Allow up to 5 redirects
});
axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response && error.response.status === 302) {
      // If it's a redirect, follow it
    const redirectUrl = error.response.headers.location;
      if (redirectUrl) {
        return axiosInstance.get(redirectUrl);
      }
    }
    return Promise.reject(error);
  }
);
export const fetchFights = async (): Promise<Fight[]> => {
  const response = await axios.get(`${API_BASE_URL}/schedule`);
  return response.data;
};

export const submitPrediction = async (prediction: Prediction): Promise<void> => {
  await axios.post(`${API_BASE_URL}/predictions`, prediction);
};