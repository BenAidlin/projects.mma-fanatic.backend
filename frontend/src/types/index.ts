export interface Fighter {
  original_id: string;
  gender: string;
  country: string;
  first_name: string;
  last_name: string;
  display_name: string;
  rec: string;
  short_display_name: string;
  stats: {
    age: string;
    ht: string;
    rch: string;
    sigstrkacc: string;
    sigstrklpm: string;
    stnce: string;
    subavg: string;
    tdacc: string;
    tdavg: string;
    wt: string;
    odds: string | null;
  };
}

export interface Match {
  awy: Fighter;
  hme: Fighter;
  nte: string;
  status: string;
  dt: string;
}

export interface Card {
  hdr: string;
  status: string;
  mtchs: Match[];
}

export interface Fight {
  id: string;
  is_completed: boolean;
  postponed_or_canceled: boolean;
  event_date: string;
  name: string;
  cards: Card[];
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
  