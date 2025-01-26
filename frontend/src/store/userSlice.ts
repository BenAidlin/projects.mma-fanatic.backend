import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { User, Prediction } from '../types';
import { submitPrediction } from '../services/api';

interface UserState {
  id: string;
  username: string;
  score: number;
  predictions: Prediction[];
}

const initialState: UserState = {
  id: '',
  username: '',
  score: 0,
  predictions: [],
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
      return { ...state, ...action.payload };
    },
    updateScore: (state, action: PayloadAction<number>) => {
      state.score += action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(addPredictionAsync.fulfilled, (state, action) => {
      state.predictions.push(action.payload);
    });
    builder.addCase(addPredictionAsync.rejected, (_, action) => {
      console.error('Failed to add prediction:', action.payload);
      // You could also update the state here to show an error message to the user
    });
  },
});

export const { setUser, updateScore } = userSlice.actions;
export default userSlice.reducer;
