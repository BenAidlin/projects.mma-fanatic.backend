// src/navigation/AppNavigator.tsx
import React, { useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import LoginScreen from '../screens/Login/LoginScreen';
import TabNavigator from './TabNavigator';

const AppNavigator: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false); // Replace with real auth logic

  return (
    <NavigationContainer>
      {isLoggedIn ? <TabNavigator /> : <LoginScreen />}
    </NavigationContainer>
  );
};

export default AppNavigator;
