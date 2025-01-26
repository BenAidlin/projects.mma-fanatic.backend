import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { Fight } from '../types';
import { fetchFights } from '../services/api';

interface FightState {
  fights: Fight[];
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
}

const initialState: FightState = {
  fights: [],
  status: 'idle',
  error: null,
};

export const getFights = createAsyncThunk('fights/getFights', async (_, { rejectWithValue }) => {
  try {
    return await fetchFights();
  } catch (error) {
    return rejectWithValue((error as Error).message);
  }
});

const fightSlice = createSlice({
  name: 'fights',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getFights.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(getFights.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.fights = action.payload;
      })
      .addCase(getFights.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload as string;
      });
  },
});

export default fightSlice.reducer;
