export interface Fight {
    id: string;
    fighter1: string;
    fighter2: string;
    date: string;
    weight_class: string;
  }
  
  export interface Prediction {
    fightId: string;
    predictedWinner: string;
  }
  
  export interface User {
    id: string;
    username: string;
    score: number;
    predictions: Prediction[];
  }
  