import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { Fight } from '../types';
import { fetchFights } from '../services/api';

export const getFights = createAsyncThunk('fights/getFights', async () => {
  return await fetchFights();
});

const fightSlice = createSlice({
  name: 'fights',
  initialState: [] as Fight[],
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(getFights.fulfilled, (_, action) => {
      return action.payload;
    });
  },
});

export default fightSlice.reducer;
