import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';
import { User} from '../types';
interface UserState {
  data: User | null;
  isLoggedIn: boolean;
}

const initialState: UserState = {
  data: null,
  isLoggedIn: false,
};


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
});

export const { setUser, updateScore, clearUser } = userSlice.actions;
export default userSlice.reducer;
