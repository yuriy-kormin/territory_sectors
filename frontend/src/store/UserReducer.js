import { removeTokensFromStorage, setTokensToStorage } from "./tokenStore";

const SET_USER = "SET_USER";
const SET_ANON_USER = "SET_ANON_USER";
const LOGOUT = "LOGOUT";

const initialState = {
  is_login: false,
  is_anon: false,
};

export const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_USER:
      setTokensToStorage(action.payload);
      return { ...state, is_login: true, is_anon: false, ...action.payload };
    case SET_ANON_USER:
      removeTokensFromStorage();
      return { ...state, is_anon: true, is_login: false };
    case LOGOUT:
      removeTokensFromStorage();
      return { ...initialState };
    default:
      return state;
  }
};

export const userSetAction = (payload) => ({ type: SET_USER, payload });
export const userAnonSetAction = () => ({ type: SET_ANON_USER });
export const userLogout = () => ({ type: LOGOUT });
