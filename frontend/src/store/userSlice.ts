import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { User, Prediction } from '../types';
import { submitPrediction } from '../services/api';

interface UserState {
  data: User | null;
  isLoggedIn: boolean;
}

const initialState: UserState = {
  data: null,
  isLoggedIn: false,
};

export const addPredictionAsync = createAsyncThunk(
  'user/addPrediction',
  async (prediction: Prediction, { rejectWithValue }) => {
    try {
      await submitPrediction(prediction);
      return prediction;
    } catch (error) {
      if (error instanceof Error) {
        return rejectWithValue(error.message);
      }
      return rejectWithValue('An unknown error occurred');
    }
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser: (state, action: PayloadAction<User>) => {
      state.data = action.payload;
      state.isLoggedIn = true;
    },
    updateScore: (state, action: PayloadAction<number>) => {
      if (state.data) {
        state.data.score += action.payload;
      }
    },
    clearUser: (state) => {
      state.data = null;
      state.isLoggedIn = false;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(addPredictionAsync.fulfilled, (state, action) => {
      if (state.data) {
        state.data.predictions.push(action.payload);
      }
    });
    builder.addCase(addPredictionAsync.rejected, (_, action) => {
      console.error('Failed to add prediction:', action.payload);
    });
  },
});

export const { setUser, updateScore, clearUser } = userSlice.actions;
export default userSlice.reducer;
