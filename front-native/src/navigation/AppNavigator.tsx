// src/navigation/AppNavigator.tsx
import React, { useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import LoginScreen from '../screens/Login/LoginScreen';
import TabNavigator from './TabNavigator';
import { useSelector } from 'react-redux';

const AppNavigator: React.FC = () => {
  const user = useSelector((state: any) => state.user);  // Access user state from Redux

  return (
      <NavigationContainer>
        {user ? <TabNavigator /> : <LoginScreen/>}
      </NavigationContainer>
  );
};

export default AppNavigator;
