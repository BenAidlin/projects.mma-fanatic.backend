import { LOGIN, LOGOUT } from '../actions/userActions';

interface User {
  id: string;
  name: string;
  email: string;
}

const initialState: User | null = null;

export const UserReducer = (state = initialState, action: any) => {
  switch (action.type) {
    case LOGIN:
      return action.payload;  // Set user info when logging in
    case LOGOUT:
      return null;  // Clear user info when logging out
    default:
      return state;
  }
};
