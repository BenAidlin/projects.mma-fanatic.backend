// src/store/index.ts
import { configureStore } from '@reduxjs/toolkit';
import { Provider } from 'react-redux'; 
import { UserReducer } from './reducers/userReducer';
import { ReactNode } from 'react';

// Create the store using Redux Toolkit
const store = configureStore({
  reducer: {
    user: UserReducer,  // Adding user reducer to the store
  },
});

interface AppWithReduxProps {
    children: ReactNode;
  }

// Wrap the app with the Provider component to access Redux state
const AppWithRedux: React.FC<AppWithReduxProps> = ({ children }) => (
  <Provider store={store}>
    {children}
  </Provider>
);

export { store, AppWithRedux };
