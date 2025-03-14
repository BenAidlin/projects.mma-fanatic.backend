// src/screens/Login/LoginScreen.tsx
import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { initiateGoogleLogin } from '../../services/authService';

interface LoginScreenProps {
  setIsLoggedIn: (isLoggedIn: boolean) => void;  // Define the type for the function prop
}

const logIn = () => {
  initiateGoogleLogin();
}

const LoginScreen: React.FC<LoginScreenProps> = ({setIsLoggedIn}) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome</Text>
      <Text style={styles.subtitle}>Please log in with Google to continue</Text>
      <Button title="Login with Google" onPress={() => setIsLoggedIn(true)} />
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
