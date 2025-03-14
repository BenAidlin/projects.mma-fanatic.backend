// src/App.tsx
import React from 'react';
import AppNavigator from './src/navigation/AppNavigator';
import { AppWithRedux } from './src/store';

const App: React.FC = () => {
  return <AppWithRedux>
      <AppNavigator />
    </AppWithRedux>;
};

export default App;
