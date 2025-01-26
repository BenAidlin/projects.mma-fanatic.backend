import { configureStore } from '@reduxjs/toolkit';
import fightReducer from './fightSlice';
import userReducer from './userSlice';

export const store = configureStore({
  reducer: {
    fights: fightReducer,
    user: userReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
