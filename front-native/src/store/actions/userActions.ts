export const LOGIN = 'LOGIN';
export const LOGOUT = 'LOGOUT';

export const login = () => ({
  type: LOGIN,
  payload: {},
});

export const logout = () => ({
  type: LOGOUT,
});
