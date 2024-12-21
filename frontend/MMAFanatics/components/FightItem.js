import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function FightItem({ fight, navigation }) {
  return (
    <View style={styles.fightItem}>
      <Text>{fight.fighter1} vs {fight.fighter2}</Text>
      <Button
        title="Place a Guess"
        onPress={() => navigation.navigate('FightDetails', { fightId: fight.id })}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  fightItem: {
    marginBottom: 15,
    padding: 10,
    backgroundColor: '#f0f0f0',
    borderRadius: 5,
  },
});
