import React, { useState } from 'react';
import { View, Text, Button, TextInput, StyleSheet, TouchableOpacity } from 'react-native';

export default function FightDetailsScreen({ route, navigation }) {
  // Get the fight details from the route params
  const { fightId } = route.params;

  // Mock data for fight details (You can replace this with an API call or dynamic data)
  const fightDetails = {
    '1': { fighter1: 'Fighter A', fighter2: 'Fighter B' },
    '2': { fighter1: 'Fighter C', fighter2: 'Fighter D' },
    // Add more fight data as needed
  };

  const fight = fightDetails[fightId];
  
  // State to handle user's guess
  const [guess, setGuess] = useState('');
  
  // Function to handle placing a guess
  const handlePlaceGuess = () => {
    if (guess === '') {
      alert('Please enter a guess.');
    } else {
      // Logic to save or process the guess (e.g., store it in a database)
      console.log(`User placed a guess: ${guess} for fight ${fightId}`);
      alert(`You guessed: ${guess}`);
      navigation.goBack(); // Navigate back after placing the guess
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{fight.fighter1} vs {fight.fighter2}</Text>
      
      {/* Subtitle */}
      <Text style={styles.subHeader}>Place your guess:</Text>
      
      {/* Input for placing a guess */}
      <TextInput
        style={styles.input}
        placeholder="Enter your guess (e.g., Fighter A)"
        value={guess}
        onChangeText={setGuess}
        placeholderTextColor="#B0B0B0"
      />
      
      {/* Submit button with styling */}
      <TouchableOpacity 
        style={[styles.button, guess && styles.buttonActive]} 
        onPress={handlePlaceGuess}
        disabled={!guess}
      >
        <Text style={styles.buttonText}>Place Guess</Text>
      </TouchableOpacity>
      
      {/* Back Button */}
      <TouchableOpacity 
        style={styles.backButton} 
        onPress={() => navigation.goBack()}
      >
        <Text style={styles.backButtonText}>Go Back</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
    padding: 20,
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
  },
  subHeader: {
    fontSize: 18,
    color: '#555',
    marginBottom: 20,
  },
  input: {
    width: '100%',
    height: 50,
    borderColor: '#4CAF50',
    borderWidth: 2,
    borderRadius: 10,
    paddingHorizontal: 15,
    fontSize: 16,
    backgroundColor: '#FFF',
    marginBottom: 20,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 3 },
    shadowRadius: 5,
  },
  button: {
    width: '100%',
    height: 50,
    borderRadius: 10,
    backgroundColor: '#B0E57C',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 20,
    opacity: 0.7,
  },
  buttonActive: {
    opacity: 1,
  },
  buttonText: {
    color: '#FFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  backButton: {
    marginTop: 10,
    padding: 10,
    backgroundColor: '#FF5722',
    borderRadius: 10,
    alignItems: 'center',
  },
  backButtonText: {
    color: '#FFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
