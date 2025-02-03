import axios from 'axios';
import Cookies from 'js-cookie';

const API_URL = 'http://localhost:8004';

export const initiateGoogleLogin = () => {
  window.location.href = `${API_URL}/auth/google`;
};

export const handleAuthCallback = async (token: string) => {
  Cookies.set('auth_token', token);
  // Redirect to home page or fetch user data
  window.location.href = '/';
};

export const getCurrentUser = async () => {
  const token = Cookies.get('auth_token');
  if (!token) return null;

  try {
    const response = await axios.get(`${API_URL}/api/user`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching user data:', error);
    return null;
  }
};

export const logout = () => {
  Cookies.remove('auth_token');
  window.location.href = '/';
};
