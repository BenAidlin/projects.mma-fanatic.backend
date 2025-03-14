// src/screens/History/HistoryScreen.tsx
import React from 'react';
import { ScrollView, Text, StyleSheet } from 'react-native';

const HistoryScreen: React.FC = () => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.text}>This is the History Screen</Text>
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

export default HistoryScreen;
