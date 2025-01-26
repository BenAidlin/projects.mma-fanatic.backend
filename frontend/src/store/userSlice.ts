import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { User, Prediction } from '../types';

const initialState: User = {
  id: '',
  username: '',
  score: 0,
  predictions: [], // Initialize with an empty array
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser: (state, action: PayloadAction<User>) => {
      return action.payload;
    },
    updateScore: (state, action: PayloadAction<number>) => {
      state.score += action.payload;
    },
  },
});

export const { setUser, updateScore } = userSlice.actions;
export default userSlice.reducer;
