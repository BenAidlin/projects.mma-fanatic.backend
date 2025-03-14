import React, { useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { useDispatch } from 'react-redux';
import * as WebBrowser from 'expo-web-browser';  // Import WebBrowser
import * as Linking from 'expo-linking';  // Import Linking to handle the redirect
import { login } from '../../store/actions/userActions';
import AsyncStorage from '@react-native-async-storage/async-storage';  // Import AsyncStorage
import { Platform } from 'react-native';  // Import Platform to check for web vs mobile

const API_URL = process.env.EXPO_PUBLIC_API_URL;

const LoginScreen: React.FC = () => {
  const dispatch = useDispatch();
  
  const handleUrl = async (event: { url: string }) => {
    console.log('Checking for token in the URL...');
    const parsedUrl = new URL(event.url);
    const token = new URLSearchParams(parsedUrl.search).get("token");
    
    if (token) {
      // Save the token in AsyncStorage
      try {
        await AsyncStorage.setItem('userToken', token);
        console.log('Token saved successfully!');
      } catch (error) {
        console.log('Failed to save the token:', error);
      }
      // Dispatch login action
      dispatch(login());
      console.log('Authentication successful, token:', token);
    } else {
      console.log('No token found in the URL.');
    }
  };

  // Handle the URL when the app is opened with the token
  useEffect(() => {
    const sub = Linking.addEventListener('url', handleUrl);
    return () => {
      sub.remove();
    };
  }, [dispatch]);

  // Handle Google login action
  const handleLogin = async () => {
    const redirectUri = Platform.OS === 'web' ? window.location.href : 'yourapp://auth-callback';  // Use the current window URL on web

    // Open the browser for Google login
    const authUrl = `${API_URL}/auth/google?redirect_uri=${redirectUri}`;

    if (Platform.OS === 'web') {
      // For web, open the URL in a new window
      window.open(authUrl, '_blank');
    } else {
      // For mobile, use WebBrowser for handling auth
      const result = await WebBrowser.openAuthSessionAsync(authUrl, redirectUri);
      
      if (result.type === 'success') {
        console.log('Login successful, token should be handled by the deep link');
        if (result.url) {
          handleUrl({ url: result.url });
        }
      } else {
        console.log('Login failed or was cancelled');
      }
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome</Text>
      <Text style={styles.subtitle}>Please log in with Google to continue</Text>
      <Button title="Login with Google" onPress={handleLogin} />
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
