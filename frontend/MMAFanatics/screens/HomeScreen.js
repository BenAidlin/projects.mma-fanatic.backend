import React, { useState } from 'react';
import { View, Text, TouchableOpacity, FlatList, StyleSheet, Image, Dimensions, Platform, ScrollView } from 'react-native';

// Sample data for events and their respective fights
const events = [
  {
    id: '1',
    name: 'UFC 300',
    date: '2024-12-25',
    fights: [
      {
        id: '1',
        fighter1: 'Fighter A',
        fighter2: 'Fighter B',
        fighter1Details: {
          weight: '75 kg',
          height: '6\'2"',
          reach: '74"',
          record: '20-5-0',
          odds: '-155',
        },
        fighter2Details: {
          weight: '80 kg',
          height: '6\'0"',
          reach: '76"',
          record: '15-3-2',
          odds: '+500',
        },
        fighter1Image: 'https://via.placeholder.com/100?text=Fighter+A',
        fighter2Image: 'https://via.placeholder.com/100?text=Fighter+B',
      },
      {
        id: '2',
        fighter1: 'Fighter C',
        fighter2: 'Fighter D',
        fighter1Details: {
          weight: '70 kg',
          height: '5\'10"',
          reach: '72"',
          record: '18-6-0',
          odds: '-200',
        },
        fighter2Details: {
          weight: '85 kg',
          height: '6\'1"',
          reach: '78"',
          record: '22-4-1',
          odds: '+300',
        },
        fighter1Image: 'https://via.placeholder.com/100?text=Fighter+C',
        fighter2Image: 'https://via.placeholder.com/100?text=Fighter+D',
      },
    ],
  },
  {
    id: '2',
    name: 'UFC Fight Night',
    date: '2025-01-15',
    fights: [
      {
        id: '3',
        fighter1: 'Fighter E',
        fighter2: 'Fighter F',
        fighter1Details: {
          weight: '78 kg',
          height: '6\'1"',
          reach: '75"',
          record: '15-2-0',
          odds: '-120',
        },
        fighter2Details: {
          weight: '82 kg',
          height: '6\'0"',
          reach: '77"',
          record: '10-5-1',
          odds: '+250',
        },
        fighter1Image: 'https://via.placeholder.com/100?text=Fighter+E',
        fighter2Image: 'https://via.placeholder.com/100?text=Fighter+F',
      },
    ],
  },
  {
    id: '3',
    name: 'Bellator 350',
    date: '2025-02-05',
    fights: [
      {
        id: '4',
        fighter1: 'Fighter G',
        fighter2: 'Fighter H',
        fighter1Details: {
          weight: '77 kg',
          height: '6\'0"',
          reach: '73"',
          record: '19-3-1',
          odds: '-150',
        },
        fighter2Details: {
          weight: '85 kg',
          height: '6\'3"',
          reach: '80"',
          record: '20-2-0',
          odds: '+400',
        },
        fighter1Image: 'https://via.placeholder.com/100?text=Fighter+G',
        fighter2Image: 'https://via.placeholder.com/100?text=Fighter+H',
      },
      {
        id: '5',
        fighter1: 'Fighter I',
        fighter2: 'Fighter J',
        fighter1Details: {
          weight: '80 kg',
          height: '6\'1"',
          reach: '75"',
          record: '23-6-0',
          odds: '-190',
        },
        fighter2Details: {
          weight: '78 kg',
          height: '5\'11"',
          reach: '72"',
          record: '17-4-0',
          odds: '+350',
        },
        fighter1Image: 'https://via.placeholder.com/100?text=Fighter+I',
        fighter2Image: 'https://via.placeholder.com/100?text=Fighter+J',
      },
    ],
  },
  // Add more events as needed
];
const { width } = Dimensions.get('window'); // Get the screen width

export default function HomeScreen({ navigation }) {
  const [expandedEvent, setExpandedEvent] = useState(null);

  // Toggle the visibility of the fights for a given event
  const toggleEvent = (eventId) => {
    setExpandedEvent((prevEvent) => (prevEvent === eventId ? null : eventId));
  };

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
          <Text style={styles.fighterDetail}>Odds: {item.fighter1Details.odds}</Text> {/* Added odds */}
        </View>

        {/* Fighter 2 details */}
        <View style={styles.fighterDetails}>
          <Image style={styles.fighterImage} source={{ uri: item.fighter2Image }} />
          <Text style={styles.fighterName}>{item.fighter2}</Text>
          <Text style={styles.fighterDetail}>Weight: {item.fighter2Details.weight}</Text>
          <Text style={styles.fighterDetail}>Height: {item.fighter2Details.height}</Text>
          <Text style={styles.fighterDetail}>Reach: {item.fighter2Details.reach}</Text>
          <Text style={styles.fighterDetail}>Record: {item.fighter2Details.record}</Text>
          <Text style={styles.fighterDetail}>Odds: {item.fighter2Details.odds}</Text> {/* Added odds */}
        </View>
      </View>
    </TouchableOpacity>
  );

  // Render item for each event
  const renderEventItem = ({ item }) => (
    <View style={styles.eventCard}>
      <Text style={styles.eventTitle}>{item.name}</Text>
      <Text style={styles.eventDate}>{item.date}</Text>

      {/* Toggle button for event */}
      <TouchableOpacity onPress={() => toggleEvent(item.id)} style={styles.toggleButton}>
        <Text style={styles.toggleButtonText}>
          {expandedEvent === item.id ? 'Collapse Fights' : 'Expand Fights'}
        </Text>
      </TouchableOpacity>

      {/* List of fights within the event */}
      {expandedEvent === item.id && (
        <FlatList
          data={item.fights}
          renderItem={renderFightItem}
          keyExtractor={(fight) => fight.id}
        />
      )}
    </View>
  );

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Upcoming Events</Text>

      {/* List of events */}
      <FlatList
        data={events}
        renderItem={renderEventItem}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.eventList}
      />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'flex-start',
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
  eventList: {
    width: '100%',
  },
  eventCard: {
    backgroundColor: '#FFF',
    marginBottom: 20,
    padding: 15,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 6,
    elevation: 5,
    width: Platform.OS === 'web' ? width * 0.95 : '100%',
    marginHorizontal: Platform.OS === 'web' ? 15 : 10,
  },
  eventTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
  eventDate: {
    fontSize: 16,
    color: '#777',
    marginBottom: 10,
  },
  toggleButton: {
    marginVertical: 10,
    padding: 10,
    backgroundColor: '#007BFF',
    borderRadius: 5,
    alignItems: 'center',
  },
  toggleButtonText: {
    color: '#FFF',
    fontSize: 16,
  },
  fightCard: {
    backgroundColor: '#FFF',
    marginBottom: 15,
    padding: 15,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 6,
    elevation: 5,
    width: Platform.OS === 'web' ? width * 0.95 : '100%',
    marginHorizontal: Platform.OS === 'web' ? 15 : 10,
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
    width: '45%',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
    padding: 10,
    borderRadius: 8,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 3,
  },
  fighterImage: {
    width: 80,
    height: 80,
    borderRadius: 40,
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
    marginBottom: 3,
  },
});
