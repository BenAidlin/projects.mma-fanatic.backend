// src/screens/Login/LoginScreen.tsx
import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { initiateGoogleLogin } from '../../services/authService';

const LoginScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome</Text>
      <Text style={styles.subtitle}>Please log in with Google to continue</Text>
      <Button title="Login with Google" onPress={initiateGoogleLogin} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    marginBottom: 20,
  },
});

export default LoginScreen;
