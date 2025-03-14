// src/navigation/TabNavigator.tsx
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import ScheduleScreen from '../screens/Schedule/ScheduleScreen';
import MyPicksScreen from '../screens/MyPicks/MyPicksScreen';
import HistoryScreen from '../screens/History/HistoryScreen';
import MoreScreen from '../screens/More/MoreScreen';

const Tab = createBottomTabNavigator();

const TabNavigator: React.FC = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Schedule" component={ScheduleScreen} />
      <Tab.Screen name="My Picks" component={MyPicksScreen} />
      <Tab.Screen name="History" component={HistoryScreen} />
      <Tab.Screen name="More" component={MoreScreen} />
    </Tab.Navigator>
  );
};

export default TabNavigator;
