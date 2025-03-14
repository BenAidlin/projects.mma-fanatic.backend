// src/screens/MyPicks/MyPicksScreen.tsx
import React from 'react';
import { ScrollView, Text, StyleSheet } from 'react-native';

const MyPicksScreen: React.FC = () => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.text}>This is the My Picks Screen</Text>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
  },
  text: {
    fontSize: 18,
  },
});

export default MyPicksScreen;
