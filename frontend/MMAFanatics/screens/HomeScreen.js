import React from 'react';
import { View, Text, TouchableOpacity, FlatList, StyleSheet, Image } from 'react-native';

// Sample data for the fights with additional details (you can replace this with actual data)
const fights = [
  {
    id: '1',
    fighter1: 'Fighter A',
    fighter2: 'Fighter B',
    fighter1Details: { weight: '75 kg', height: '6\'2"', reach: '74"', record: '20-5-0' },
    fighter2Details: { weight: '80 kg', height: '6\'0"', reach: '76"', record: '15-3-2' },
    fighter1Image: 'https://via.placeholder.com/100?text=Fighter+A',
    fighter2Image: 'https://via.placeholder.com/100?text=Fighter+B',
  },
  {
    id: '2',
    fighter1: 'Fighter C',
    fighter2: 'Fighter D',
    fighter1Details: { weight: '70 kg', height: '5\'10"', reach: '72"', record: '18-6-0' },
    fighter2Details: { weight: '85 kg', height: '6\'1"', reach: '78"', record: '22-4-1' },
    fighter1Image: 'https://via.placeholder.com/100?text=Fighter+C',
    fighter2Image: 'https://via.placeholder.com/100?text=Fighter+D',
  },
  // Add more fight data as needed
];

export default function HomeScreen({ navigation }) {
  // Render item for each fight
  const renderFightItem = ({ item }) => (
    <TouchableOpacity
      style={styles.fightCard}
      onPress={() => navigation.navigate('FightDetails', { fightId: item.id })}
    >
      <View style={styles.fightHeader}>
        <Text style={styles.fightText}>{item.fighter1} vs {item.fighter2}</Text>
      </View>

      <View style={styles.fightDetails}>
        {/* Fighter 1 details */}
        <View style={styles.fighterDetails}>
          <Image style={styles.fighterImage} source={{ uri: item.fighter1Image }} />
          <Text style={styles.fighterName}>{item.fighter1}</Text>
          <Text style={styles.fighterDetail}>Weight: {item.fighter1Details.weight}</Text>
          <Text style={styles.fighterDetail}>Height: {item.fighter1Details.height}</Text>
          <Text style={styles.fighterDetail}>Reach: {item.fighter1Details.reach}</Text>
          <Text style={styles.fighterDetail}>Record: {item.fighter1Details.record}</Text>
        </View>

        {/* Fighter 2 details */}
        <View style={styles.fighterDetails}>
          <Image style={styles.fighterImage} source={{ uri: item.fighter2Image }} />
          <Text style={styles.fighterName}>{item.fighter2}</Text>
          <Text style={styles.fighterDetail}>Weight: {item.fighter2Details.weight}</Text>
          <Text style={styles.fighterDetail}>Height: {item.fighter2Details.height}</Text>
          <Text style={styles.fighterDetail}>Reach: {item.fighter2Details.reach}</Text>
          <Text style={styles.fighterDetail}>Record: {item.fighter2Details.record}</Text>
        </View>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Upcoming Fights</Text>

      {/* List of fights */}
      <FlatList
        data={fights}
        renderItem={renderFightItem}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.fightList}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F8F8F8',
    padding: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 20,
  },
  fightList: {
    width: '100%',
  },
  fightCard: {
    backgroundColor: '#FFF',
    marginBottom: 20,
    padding: 15,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 6,
    elevation: 5,
    width: '100%', // Make the card take up the full width of the screen
    marginHorizontal: 10, // Add horizontal margin to keep spacing from the sides
  },
  fightHeader: {
    marginBottom: 10,
  },
  fightText: {
    fontSize: 20,
    fontWeight: '500',
    color: '#333',
    textAlign: 'center',
  },
  fightDetails: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  fighterDetails: {
    width: '45%', // Each fighter section takes up 45% of the card width
    alignItems: 'center',
    backgroundColor: '#F9F9F9',
    padding: 10,
    borderRadius: 10,
    marginTop: 10,
  },
  fighterImage: {
    width: 100,
    height: 100,
    borderRadius: 50,
    marginBottom: 10,
  },
  fighterName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  fighterDetail: {
    fontSize: 14,
    color: '#555',
    marginBottom: 5,
  },
});
