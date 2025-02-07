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
  prediction_id: string | null;
  user_id: string;
  winner: string | null;
  method: Method;
  round: number | null;
  potential_gain: number | null;
  hme_id: string;
  awy_id: string;
}

export enum Method {
  NOT_PICKED = "NOT_PICKED",
  KO = "KO",
  SUB = "SUB",
  DEC = "DEC"
}
  
  export interface User {
    id: string | null;
    email: string | null;
    name: string | null;
    given_name: string | null;
    family_name: string | null;
    picture: string | null;
    score: number;
    predictions: Prediction[];
  }
  