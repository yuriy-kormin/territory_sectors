import { removeTokensFromStorage, setTokensToStorage } from "./tokenStore";

const SET_USER = "SET_USER";
const LOGOUT = "LOGOUT";

const initialState = {
  is_login: false,
};

export const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_USER:
      console.log('payload is ', action)
      setTokensToStorage(action.payload);
      return { ...state, is_login: true, ...action.payload };
    case LOGOUT:
      removeTokensFromStorage();
      return { ...initialState };
    default:
      return state;
  }
};

export const userSetAction = (payload) => ({ type: SET_USER, payload });
export const userLogout = () => ({ type: LOGOUT });
