import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/HomeScreen';
import FightDetailsScreen from '../screens/FightDetailsScreen';

const Stack = createStackNavigator();

const AppNavigator = () => (
  <Stack.Navigator initialRouteName="Home">
    <Stack.Screen name="Home" component={HomeScreen} />
    <Stack.Screen name="FightDetails" component={FightDetailsScreen} />
  </Stack.Navigator>
);

export default AppNavigator;
